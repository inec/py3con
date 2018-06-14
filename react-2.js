class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visibility: false
    };
    // change code below this line
 this.toggleVisibility = this.toggleVisibility.bind(this);
    // change code above this line
  }
  // change code below this line toggleVisibility(){
    this.setState({
     visibility: !this.state.visibility
    });
  }
  // change code above this line
  render() {
    if (this.state.visibility) {
      return (
        <div>
          <button onClick={this.toggleVisibility}>Click Me</button>
          <h1>Now you see me!</h1>
        </div>
      );
    } else {
      return (
        <div>
          <button onClick={this.toggleVisibility}>Click Me</button>
        </div>
      );
    }
  }
};//https://learn.freecodecamp.org/front-end-libraries/react/use-state-to-toggle-an-element