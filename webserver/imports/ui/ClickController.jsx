import React, { Component, PropTypes } from 'react';
import ReactDOM from 'react-dom';

import Map from './Map.jsx';
import About from './About.jsx';

export default class ClickController extends Component {
	constructor(props) {
		super(props);
		this.state = {hasClicked: false};
	}

	render() {
		if (hasClicked) {
			elementToRender = <Map />
		} else {
			elementToRender = <About />
		}
		return (
			{elementToRender}
		)
	}
}