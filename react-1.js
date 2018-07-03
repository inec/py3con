class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Initial State'
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    // change code below this line
    handleClick() {
      // change code below this line
      this.setState({
        name:'React Rocks!'
      });
      // change code above this line
    }
    // change code above this line
  }
  render() {
    return (
      <div>
        <button onClick={this.handleClick}>Click Me</button>
        <h1>{this.state.name}</h1>
      </div>
    );
  }
};//https://learn.freecodecamp.org/front-end-libraries/react/set-state-with-this-setstate
