import React, { Component } from 'react';
import { ThemeProvider } from 'styled-components';
import { Button, themeDefault, Divider, Text, Input } from 'aiq-design-system';
import axios from 'axios'

class Screen extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: "",
      blocks: ""
    };

  }

  addDataBlock = async () => {
    try {
      const r_add = await axios.post(`http://localhost:7777/blocks`, JSON.stringify({ 'data': this.state.data }), { headers: { 'Content-Type': 'application/json' } });
      const r = await axios.get(`http://localhost:7777/blocks`, { headers: { 'Content-Type': 'application/json' } });
      this.setState({
        blocks: r.data
      });
    } catch (error) {
      alert("Wrong input data");
    }
  }

  dataBlock = (e) => {
    const d = e.target.value;
    this.setState({
      data: d
    });
  }


  render() {
    return (
      <div>
        <Input variant='outlined' type="text" name="data" label="data" onChange={this.dataBlock} />
        <Button palette="primary" variant="contained" onClick={this.addDataBlock} >ADD TO BLOCKCHAIN</Button>
        {
          this.state.blocks &&
          <div>
            <Divider margin={10} height={5} color={'secondary'} />
            <ul >
              {this.state.blocks.map(block => (
                <div>
                  <Divider width={'100%'} color={'primary'}><Text paddingRight={10} paddingLeft={10}>BLOCK</Text></Divider>
                  <ul >
                    <div>{JSON.stringify(block)}</div>
                  </ul>
                </div>
              ))
              }
            </ul>
          </div>
        }
      </div>
    );
  }
}




function App() {
  return (
    <div className="App">
      <ThemeProvider theme={themeDefault}>
        <Screen />
      </ThemeProvider>
    </div>
  );
}

export default App;
