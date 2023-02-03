# import module
import codecs

# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """
<html>
    <meta charset="utf-8" />
		<title>ICCN Switch 7028</title>
		<style>
			p {
				text-align: justify;
			}
			body {
				font-size:16px;
				font-family:Arial, Helvetica, san-serif ;
			}
			ul {
				list-style-type: upper-alpha;
			}
			.blue {
				color: blue;
			}
			.Special-words {
				color:green;
			}
			nav ul {
				list-style:none;
			}
			nav li {
				display:inline;
			}
			nav a:link, nav a:visited {
				background-color:red;
				color:white;
			}
			nav a:hover {
				background-color:blue;
			}
		</style>
	</head>
	
	<body>
		<nav>
			<a href="" style="font-size: 25px;">Home</a>
			<a href="https://iccnetworking.com/products/" style="font-size: 25px;">ICCN Devices</a>
			<a href="" style="font-size: 25px;">Roasting</a>
			<a href="" style="font-size: 25px;">Drinks</a>
			<a href="" style="font-size: 25px;">Grinding</a>
			<a href="" style="font-size: 25px;">Survey</a>
		</nav>
		<h1>ICCN Switch 7028</h1>
		<aside>
			<h4>List of Images</h4>
			These are the following images:
			<ul style="list-style-type: none;">
				<li class="blue">Unpicked Coffee Berries</li>
				<li>Fresh Coffee Beans</li>
				<li>Roasted Beans</li>
			</ul>
			<figure>
				<img src="images/coffee-berries.jpg" width="120" height="120" />
				<figcaption>Unpicked Coffee Berries</figcaption>
			</figure>
			<figure>
				<img src="images/fresh-beans.jpg" width="120" height="120"/>
				<figcaption>Fresh Coffee Beans</figcaption>
			</figure>
			<figure>
				<img src="images/roasted-beans.jpg" width="120" height="120"/>
				<figcaption>Roasted Beans</figcaption>
			</figure>
		</aside>
		<section>
			<figure>
				<img src="images/commercial-roaster.jpg" width="300" height="400"/>
				<figcaption>Commercial Roaster</figcaption>
			</figure>
			<h2>Sample</h2>
			<p style="color: rgba(256,0,0, 0.5);"><span class="Special-words">Roasting coffee</span> transforms the chemical and physical properties of green coffee beans. When roasted, the green coffee bean expands to nearly double its original size, changing in color and density. As the bean absorbs heat, its color shifts to yellow, then to a light "cinnamon" brown, and then to a rich dark brown color. During roasting, oils appear on the surface of the bean. The roast will continue to darken until it is removed from the heat source.</p>
			<p class="blue"><span class="Special-words">Coffee</span> can be roasted with ordinary kitchen equipment (frying pan, grill, oven, popcorn popper) or by specialised appliances. A coffee roaster is a special pan or apparatus suitable to heat up and roast green coffee beans.</p>
			<p class="blue">The vast majority of coffee is roasted commercially on a large scale, but small-scale commercial roasting has grown significantly with the trend toward "single-origin" coffees served at specialty shops. Some coffee drinkers even roast coffee at home as a hobby in order to both experiment with the flavor profile of the beans and ensure themselves of the freshest possible roast.</p>
		</section>
	</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

# viewing html files
# below code creates a
# codecs.StreamReaderWriter object
file = codecs.open("GFG.html", 'r', "utf-8")

# using .read method to view the html
# code from our object
print(file.read())
