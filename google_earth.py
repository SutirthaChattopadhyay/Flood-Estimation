import ee

# Initialize the Earth Engine library
ee.Initialize()

# Define the region of interest (ROI) polygon
roi = ee.Geometry.Polygon(
    [[[106.5311175986817, 14.88401360239504],
      [106.70144574301412, 14.88567468158789],
      [106.68221660149186, 14.996475939738637],
      [106.67432540134314, 15.050880175819685],
      [106.61113258648004, 15.046083385875264],
      [106.53764487153217, 15.035961287202868],
      [106.52682423644103, 14.968444128060433]]])

# Add the ROI polygon to the map
Map.addLayer(roi, {}, 'ROI')

# Center the map view on the ROI
Map.centerObject(roi, 8)
