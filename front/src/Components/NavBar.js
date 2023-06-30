import Nav from 'react-bootstrap/Nav';
import Registrate from './Registrate';
import Iniciar_sesion from './Iniciar_sesion';
import Contactanos from './Contactanos';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';
function NavBar() {
  return (
    <Nav className="justify-content-center" activeKey="/home" bg="secondary">
        <Nav.Item>
        <Container>
      <Row>

        <Col xs={6} md={4}>
          <Image src="https://static.thenounproject.com/png/19085-200.png" roundedCircle />
        </Col>
       
      </Row>
    </Container>
        </Nav.Item>
        <Nav.Item>
            
        </Nav.Item>
        <Nav.Item>
          <Registrate/>
        </Nav.Item>
        <Nav.Item>
      <h1> </h1>
        </Nav.Item>
        
        <Nav.Item>
          <Iniciar_sesion/>
        </Nav.Item>       
      </Nav>
  );
}

export default NavBar;