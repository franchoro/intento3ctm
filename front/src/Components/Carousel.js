import React, { useState } from 'react';
import Carousel from 'react-bootstrap/Carousel';

import '../mark.css'
function Carrusel() {
  const [index, setIndex] = useState(0);
  const link1="https://www.niehs.nih.gov/health/assets/images/safewater_og.jpg";
  const link2="https://kanehr.co.uk/wp-content/uploads/2017/04/2203_Kane-Features1-2000x600.jpg";
  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  return (
    <Carousel activeIndex={index} onSelect={handleSelect}>
     
      <Carousel.Item>
        <img
          className="d-block w-100"
          src="https://kanehr.co.uk/wp-content/uploads/2017/04/2203_Kane-Features1-2000x600.jpg"
          alt="First slide"
        />
        <Carousel.Caption>
          <h1><mark>Pasantias UAI</mark></h1>
          
        </Carousel.Caption>
      </Carousel.Item>
      

        
    </Carousel>
  );
}

export default Carrusel;