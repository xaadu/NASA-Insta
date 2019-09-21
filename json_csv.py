import csv

# Keys to get exact info from NASA-Dict
data_locations = ["title", "url", "date", "copyright", "hdurl", "explanation", "media_type", "service_version"]

data = [{
    "copyright": "Giorgia HoferCortina Astronomical Association",
    "date": "2019-09-16",
    "explanation": "What are those colorful rings around the Moon? A corona. Rings like this will sometimes appear when the Moon is seen through thin clouds. The effect is created by the quantum mechanical diffraction of light around individual, similarly-sized water droplets in an intervening but mostly-transparent cloud. Since light of different colors has different wavelengths, each color diffracts differently. Lunar Coronae are one of the few  quantum mechanical color effects that can be easily seen with the unaided eye.  The featured lunar corona was captured around full Moon above Turin, Italy in 2014.  Similar coronae that form around the Sun are usually harder to see because of the Sun's great brightness.",
    "hdurl": "https://apod.nasa.gov/apod/image/1909/LunarCorona_Hofer_3264.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "A Lunar Corona over Turin",
    "url": "https://apod.nasa.gov/apod/image/1909/LunarCorona_Hofer_960.jpg"
}, {
    "date": "2019-09-17",
    "explanation": "Where else might life exist?  One of humanity's great outstanding questions, locating planets where extrasolar life might survive took a step forward recently with the discovery of a significant amount of water vapor in the atmosphere of distant exoplanet K2-18b. The planet and it parent star, K2-18, lie about 124 light years away toward the constellation of the Lion (Leo). The exoplanet is significantly larger and more massive than our Earth, but orbits in the habitable zone of its home star. K2-18, although more red than our Sun, shines in K2-18b's sky with a brightness similar to the Sun in Earth's sky.  The discovery was made in data from three space telescopes: Hubble, Spitzer, and Kepler, by noting the absorption of water-vapor colors when the planet moved in front of the star.  The featured illustration imagines exoplanet K2-18b on the right, its parent red dwarf star K2-18 on the left, and an unconfirmed sister planet between them.",
    "hdurl": "https://apod.nasa.gov/apod/image/1909/K218b_ESAKornmesser_6000.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Water Vapor Discovered on Distant Exoplanet",
    "url": "https://apod.nasa.gov/apod/image/1909/K218b_ESAKornmesser_1080.jpg"
}, {
    "copyright": "Min Xie",
    "date": "2019-09-19",
    "explanation": "Delicate in appearance, these filaments of shocked, glowing gas, are draped across planet Earth's sky toward the constellation of Cygnus.",
    "hdurl": "https://apod.nasa.gov/apod/image/1909/veilXie.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Along the Western Veil",
    "url": "https://apod.nasa.gov/apod/image/1909/veilXie1100.jpg"
}, {
    "date": "2019-09-20",
    "explanation": "",
    "hdurl": "https://apod.nasa.gov/apod/image/1909/LastRingPortrait_Cassini_4472.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Saturn at Night",
    "url": "https://apod.nasa.gov/apod/image/1909/LastRingPortrait_Cassini_1080.jpg"
}, {
    "copyright": "Robert Eder",
    "date": "2019-09-21",
    "explanation": "Framing a bright emission region, this telescopic view looks out across a pretty field of stars along the plane of our Milky Way Galaxy, toward the nebula rich constellation Cygnus the Swan. Popularly called the Tulip Nebula, the reddish glowing cloud of interstellar gas and dust is also found in the 1959 catalog by astronomer Stewart Sharpless as Sh2-101. About 8,000 light-years distant and 70 light-years across the complex and beautiful nebula blossoms near the center of this composite image. Ultraviolet radiation from young energetic O stars at the edge of the Cygnus OB3 association, ionizes the atoms and powers the emission from the Tulip Nebula.",
    "hdurl": "https://apod.nasa.gov/apod/image/1909/Tulip_CropRobertEder.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "The Tulip in the Swan",
    "url": "https://apod.nasa.gov/apod/image/1909/Tulip_CropRobertEder1024.jpg"
}]

with open('nasa_data.csv', 'r+') as nasa:
    d_data = csv.DictWriter(nasa, restval="-", fieldnames=data_locations)
    d_data.writeheader()
    d_data.writerows(data)