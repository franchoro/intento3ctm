import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Registrate from './Registrate';
import Iniciar_sesion from './Iniciar_sesion';
import Contactanos from './Contactanos';
import '../mark.css'
function NavBar2() {
  return (
    <Navbar bg="secondary" expand="lg">
      <Container>
        
        <Navbar.Brand href="#home">
        <Nav.Link href="https://www.instagram.com/poto_uaint/"> <p class="text-light ">Contactanos</p></Nav.Link>
         </Navbar.Brand>
        <Registrate/>
        

        
           

        <Iniciar_sesion/>
      </Container>


    </Navbar>
  );
}

export default NavBar2;