import React from 'react'
import { Container, Grid } from 'semantic-ui-react'
import Canvas from './Canvas'

export default function MainContainer () {
  return (
    <Grid columns={2}>
      <Grid.Row>
        <Grid.Column width={3}>
          <br />
          <br />
          <br />
          <br />
          Stats here
        </Grid.Column>
        <Grid.Column width={13}>
          <Container id='MainCanvas' className='canvas-container' fluid>
            <Canvas />
          </Container>
        </Grid.Column>
      </Grid.Row>
    </Grid>
  )
}
