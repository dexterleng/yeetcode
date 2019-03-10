import React, { Component } from 'react';
import AceEditor from 'react-ace';
import Button from '@material-ui/core/Button';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';
import { Done, Clear } from "@material-ui/icons";
import 'brace/theme/monokai';
import 'brace/mode/python';
import { CardHeader } from '@material-ui/core';

class Question extends Component {
  state = {
    code: "",
    loading: false,
    testcases: this.props.testcases,
    title: null,
    description: null
  }

  componentDidMount = async () => {
    const res = await axios.get(this.props.apiUrl);
    const { title, description } = res.data;
    this.setState({
      title,
      description
    });
  }

  onRunCode = async () => {
    this.setState({
      loading: true
    });
    const res = await axios.post(this.props.apiUrl, {
      code: this.state.code
    });
    const result = res.data.testcases;
    const lookup = {};
    result.forEach(result => {
      lookup[result.name] = result.correct;
    })
    this.setState({
      loading: false,
      testcases: this.state.testcases.map((testcase) => {
        if (lookup[testcase.name] !== undefined) {
          return { ...testcase, correct: lookup[testcase.name] }
        } else {
          return { ...testcase, correct: false }
        }
      })
    })
  }

  render() {
    return (
      <div>
        <Paper>
          <CardHeader
            title={this.state.title}
            subheader={this.state.description}
          />
          <AceEditor
            mode="python"
            theme="monokai"
            value={this.state.code}
            onChange={(newValue) => this.setState({ code: newValue })}
            width="100%"
            minLines={20}
            maxLines={20}
            showPrintMargin={false}
          />
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Testcase</TableCell>
                <TableCell>Expression</TableCell>
                <TableCell>Expected Output</TableCell>
                <TableCell>Correct</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {
                this.state.testcases.map(testcase => {
                  const doneComponent = testcase.correct === true ? <Done/> : <Clear/>
                  return (
                    <TableRow key={testcase.name}>
                      <TableCell component="th" scope="row">
                        {testcase.name}
                      </TableCell>
                      <TableCell>{testcase.expression}</TableCell>
                      <TableCell>{testcase.expected}</TableCell>
                      <TableCell>{doneComponent}</TableCell>
                    </TableRow>
                  )})
              }
            </TableBody>
          </Table>
        </Paper>

        <Button
          variant="contained"
          color="primary"
          onClick={this.onRunCode}
          disabled={this.state.loading}
          style={{ margin: "10px 0px" }}
        >
          Run Code
        </Button>
      </div>
    );
  }
}

export default Question;
