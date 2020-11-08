import React, { useRef, useEffect } from 'react';
import './css/canvas.css';


const Board = () => {
  const canvasRef = useRef(null);
  const colorsRef = useRef(null);

  useEffect(() => {

    // --------------- getContext() method returns a drawing context on the canvas-----

    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');

    // ----------------------- Colors --------------------------------------------------

    const colors = document.getElementsByClassName('color');
    // set the current color
    const current = {
      color: 'black',
    };

    // helper that will update the current color
    const onColorUpdate = (e) => {
      current.color = e.target.className.split(' ')[1];
    };

    // loop through the color elements and add the click event listeners
    for (let i = 0; i < colors.length; i++) {
      colors[i].addEventListener('click', onColorUpdate, false);
    }
    let drawing = false;

    const getMousePos = (e) => {
      const rect = canvas.getBoundingClientRect();
      return {
          x: (e.clientX - rect.left) / (rect.right - rect.left) * canvas.width,
          y: (e.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height
      };
  }

    // ------------------------------- create the drawline ----------------------------

    const drawLine = (x0, y0, x1, y1, color, emit) => {
      context.beginPath();
      context.moveTo(x0, y0);
      context.lineTo(x1, y1);
      context.strokeStyle = color;
      context.lineWidth = 2;
      context.stroke();
      context.closePath();

      if (!emit) { return; }      
    };

    // ---------------- mouse movement --------------------------------------

    const onMouseDown = (e) => {
      drawing = true;
      const pos = getMousePos(e)
      current.x = pos.x
      current.y = pos.y
    };

    const onMouseMove = (e) => {
      if (!drawing) { return; }
      const pos = getMousePos(e)
      drawLine(current.x, current.y, pos.x, pos.y, current.color, true);
      current.x = pos.x
      current.y = pos.y
    };

    const onMouseUp = (e) => {
      if (!drawing) { return; }
      const pos = getMousePos(e)
      drawing = false;
      drawLine(current.x, current.y, pos.x, pos.y, current.color, true);
    };

    // ----------- limit the number of events per second -----------------------

    const throttle = (callback, delay) => {
      let previousCall = new Date().getTime();
      return function() {
        const time = new Date().getTime();

        if ((time - previousCall) >= delay) {
          previousCall = time;
          callback.apply(null, arguments);
        }
      };
    };

    const onResize = () => {
      canvas.width = document.getElementById("MainCanvas").clientWidth;
      canvas.height = document.getElementById("MainCanvas").clientHeight;
    };

    window.addEventListener('resize', onResize, false);
    onResize();

    // -----------------add event listeners to our canvas ----------------------

    canvas.addEventListener('mousedown', onMouseDown, false);
    canvas.addEventListener('mouseup', onMouseUp, false);
    canvas.addEventListener('mouseout', onMouseUp, false);
    canvas.addEventListener('mousemove', throttle(onMouseMove, 10), false);

    // Touch support for mobile devices
    canvas.addEventListener('touchstart', onMouseDown, false);
    canvas.addEventListener('touchend', onMouseUp, false);
    canvas.addEventListener('touchcancel', onMouseUp, false);
    canvas.addEventListener('touchmove', throttle(onMouseMove, 10), false);

  }, []);

  // ------------- The Canvas and color elements --------------------------

  return (
    <>    
      <canvas ref={canvasRef} className="whiteboard" />
      <div ref={colorsRef} className="colors">
        <div className="color black" />
        <div className="color red" />
        <div className="color green" />
        <div className="color blue" />
        <div className="color yellow" />
      </div>
    </>
  );
};

export default Board;