if (process.env.NODE_ENV == 'development'){
	var loaders = ['react-hot-loader','babel-loader?presets[]=es2015,presets[]=react'];
} else {
	var loaders = ['babel-loader?presets[]=es2015,presets[]=react'];
}

module.exports = {
	entry : './main.jsx',
	output : {
		path : __dirname + '/public/dist',
		filename : 'bundle.js',
		publicPath : '/dist/',
	},
	devtool: 'eval',
	resolve : {
		extensions: ['.js', '.jsx']
	},
	module : {
		loaders : [{
			test : /\.jsx?$/,
			loaders : loaders,
			exclude: /node_modules/
		}]
	}
};