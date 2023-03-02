import React from 'react';

function Counter(props){
  return <h1>{props.count}</h1>;
};

export default class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      count: 0,
    };
  }
  
  render() {
    return (
      <div>
        <button onClick={() => this.setState({count: this.state.count + 1})}>Increase</button>
        <Counter count={this.state.count} />
      </div>
    );
  }
}
