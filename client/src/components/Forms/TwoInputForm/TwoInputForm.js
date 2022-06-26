import React, { Component } from "react";
import { ReactDOM } from "react";
import { Button, Form } from "react-bootstrap";
import classes from "./TwoInputForm.module.css";

class TwoInputForm extends Component {
  render() {
    return (
      <div className={classes.flexContainer}>
        <Form.Group className={`mb-3 ${classes.flexItem}`}>
          <Form.Label className={classes.FormLabels}>
            {this.props.label[0].label}
          </Form.Label>
          <Form.Control
            value={this.props.label[0].val}
            onChange={(e) =>
              this.props.onChange(e.target.value, this.props.label[0].label)
            }
            type="text"
            required
          />
        </Form.Group>
        <Form.Group className={`mb-3 ${classes.flexItem}`}>
          <Form.Label className={classes.FormLabels}>
            {this.props.label[1].label}
          </Form.Label>
          <Form.Control
            value={this.props.label[1].val}
            onChange={(e) =>
              this.props.onChange(e.target.value, this.props.label[1].label)
            }
            type="text"
            required
          />
        </Form.Group>
      </div>
    );
  }
}

export default TwoInputForm;
