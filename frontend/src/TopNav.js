import React from 'react'
import {
  Container,  
  Dropdown,
  Menu,  
} from 'semantic-ui-react'


export default function TopNav() {
  return (
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as='a' header>          
          CoffeeGrindSize
        </Menu.Item>
        <Menu.Item as='a'>Open Image</Menu.Item>
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
