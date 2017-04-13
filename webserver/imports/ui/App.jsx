import React, { Component, PropTypes } from 'react';
import ReactDOM from 'react-dom';

import Map from './Map.jsx';
import About from './About.jsx';

// Whole app here
export default class App extends Component {
	constructor(props) {
		super(props);
		this.state = {hasClicked: false};
		this.toggleView = this.toggleView.bind(this);
	}

	toggleView() {
		if (this.state.hasClicked) {
			this.setState({hasClicked: false});
		} else {
			this.setState({hasClicked: true});
		}
	}

	render() {
		let elementToRender = null;
		if (this.state.hasClicked) {
			elementToRender = <About />
		} else {
			elementToRender = <Map />
		}

		return(
			<div className="app">
				<div className="container-fluid">
					<nav className="navbar navbar-default navbar-fixed-top" role="navigation">
						<div className="container-fluid">
							<div className="navbar-header">
            		    		<button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            		    		    <span className="sr-only">Toggle navigation</span>
            		    		    <span className="icon-bar"></span>
            		    		    <span className="icon-bar"></span>
            		    		    <span className="icon-bar"></span>
            		    		</button>
								<a className="navbar-brand" href="#" onClick={this.toggleView}>Quali'B</a><small>alpha</small>
							</div>
            				<div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            				    <ul className="nav navbar-nav">
            				        <li>
            				            <a href="#" onClick={this.toggleView}>A propos</a>
            				        </li>
            				        <li>
            				            <a href="mailto:contact@jonathanperron.fr?subject=QualiB">Contact</a>
            				        </li>
            				    </ul>
							</div>					
						</div>
					</nav>
					<div className="container-fluid">
						<div className="row">
							<div className="col-md-12">
								{elementToRender}
							</div>
						</div>
					</div>
				</div>
			</div>
		)
	}
}