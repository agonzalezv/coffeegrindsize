import React from 'react'
import {
  Container,
  Header,
} from 'semantic-ui-react'
import Canvas from './Canvas'

export default function MainContainer() {
  return(
    <Container id="MainCanvas" fluid>      
      <Canvas/>      
    </Container>
  )
}