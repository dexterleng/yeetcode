import React, { Component } from 'react';
import TwoSum from "./Question";

class App extends Component {
  render() {
    return (
      <div>
        <TwoSum
          testcases={[
            { name: "test_public_01", expression: "two_sum([2, 7, 11, 15], 9)", expected: "[0, 1]", correct: null },
            { name: "test_public_02", expression: "two_sum([2, 7, 11, 15], 100)", expected: "-1", correct: null }
          ]}
          apiUrl="http://localhost:5000/two_sum/"
        />
      </div>
    );
  }
}

export default App;
