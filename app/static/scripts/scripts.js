function createMap() {
	var map = new mapboxgl.Map({
		container: 'map',
		style: 'https://tiles.stadiamaps.com/styles/alidade_smooth.json',
		center: [39.1441, 75.4345],
		zoom: 16
	});

	mapboxgl.setRTLTextPlugin('https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.2.1/mapbox-gl-rtl-text.js');

	// Add zoom and rotation controls
	map.addControl(new mapboxgl.NavigationControl());
}