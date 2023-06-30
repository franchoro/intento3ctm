import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Registrate from './Registrate';
import Iniciar_sesion from './Iniciar_sesion';
import Contactanos from './Contactanos';
import Button from 'react-bootstrap/Button';
import '../mark.css'
function NavBar3() {
  return (
    <Navbar bg="secondary" expand="lg">
      <Container>
        

        <Navbar.Brand>Nombre Alumno</Navbar.Brand>

        <Button href="/App">Cerrar Sesion</Button>


      </Container>
    </Navbar>
  );
}

export default NavBar3;