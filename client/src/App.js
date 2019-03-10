import React, { Component } from 'react';
import Question from "./Question";

class App extends Component {
  render() {
    return (
      <div>
        <Question
          apiUrl="http://localhost:5000/two_sum/"
        />
        <Question
          apiUrl="http://localhost:5000/fib/"
        />
        <Question
          apiUrl="http://localhost:5000/squares_of_sorted_array/"
        />
      </div>
    );
  }
}

export default App;
