import React from 'react';

const college = {
  street: 'Oxford',
  number: 54,
  city : 'London',
  country: 'England'
}

const getCollegeAddress = ({street, number}) => {
   return street + ' ' + number;
}
 

const App = () => {
  return <h1>Address: {getCollegeAddress(college)}</h1>
}

export default App;