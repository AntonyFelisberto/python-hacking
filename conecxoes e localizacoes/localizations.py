#pip install pygeocoder
from pygeocoder import Geocoder
endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder("CHAVE_DA_API_DO_GOOGLE").geocode(endereco).coordinates)
endereco = 'avenida paulista,100 sao paulo'
resultado = Geocoder("CHAVE_DA_API_DO_GOOGLE").geocode(endereco)
print()
resultado = Geocoder("CHAVE_DA_API_DO_GOOGLE").geocode(endereco).state
resultado = Geocoder("CHAVE_DA_API_DO_GOOGLE").geocode(endereco).postal_code
resultado = Geocoder("CHAVE_DA_API_DO_GOOGLE").geocode(endereco).country
resultado = Geocoder("CHAVE_DA_API_DO_GOOGLE").reverse_geocode(-23.5703022,-46.6451267)