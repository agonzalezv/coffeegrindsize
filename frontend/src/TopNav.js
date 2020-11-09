import React from 'react';
import useGlobal from './store'
import {
  Container,
  Dropdown,
  Menu,
  Input
} from 'semantic-ui-react'

export default function TopNav() {
  const [globalState, globalActions] = useGlobal();

  return (
    <Menu
      canvas={globalState.canvas}
      fixed='top'
      inverted
    >
      <Container>
        <Menu.Item as='a' header>
          CoffeeGrindSize
        </Menu.Item>
        <Menu.Item>
          <Input
            type="file"
            id="upload-button"
            onChange={globalActions.setCanvasURL}
          />
        </Menu.Item>
        <Menu.Item as='a'>Select Reference Object</Menu.Item>
        <Menu.Item as='a'>Select Analysis Region</Menu.Item>
        <Menu.Item as='a'>Launch Particle Detection</Menu.Item>
        <Menu.Item as='a'>Erase Clusters</Menu.Item>
        <Menu.Item as='a'>Create Histogram</Menu.Item>

        <Dropdown item simple text='Dropdown'>
          <Dropdown.Menu>
            <Dropdown.Item>List Item</Dropdown.Item>
            <Dropdown.Item>List Item</Dropdown.Item>
            <Dropdown.Divider />
            <Dropdown.Header>Header Item</Dropdown.Header>
            <Dropdown.Item>
              <i className='dropdown icon' />
              <span className='text'>Submenu</span>
              <Dropdown.Menu>
                <Dropdown.Item>List Item</Dropdown.Item>
                <Dropdown.Item>List Item</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown.Item>
            <Dropdown.Item>List Item</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      </Container>
    </Menu>
  )
}
