export const setCanvasURL = (store, e) => {
  const imgUrl = e.target.files.length
    ? URL.createObjectURL(e.target.files[0])
    : ''
  store.setState({ canvas: { bgURL: imgUrl } })
}
