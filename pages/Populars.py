import requests
import streamlit as st
import random
headers = {
     "accept": "application/json",
     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjFlZTViODIxYzk4NTkyZTRkM2FlNjkxYzE3NzM4NiIsInN1YiI6IjY1NzQwOWI3Y2FkYjZiMDgxMDRkOWNmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.h9zEVuN7wJ1upBticpv1EcoS442a4NZDLCMKHq5qhwk"
    }



def popular(ty,tx):
     global y, y1 ,y2,y3,y4,y5
     global poster,p
   
     url=f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={tx}"
     response = requests.get(url, headers=headers)
     p=response.json()
     x=p["results"]
     
     poster=x[ty]["poster_path"]
     y=x[ty]["original_title"]
     y1=x[ty]["release_date"]
     y2=x[ty]["vote_average"]
     y3=x[ty]["vote_count"]
     y4=x[ty]["id"]
     url2=f"https://api.themoviedb.org/3/movie/{y4}?language=en-US"
     response2 = requests.get(url2, headers=headers)
     p1=response2.json()
     y5=p1['imdb_id']

st.title("Movie Recommendations POPULARS")


hero=(st.button("get movie"))

url3= f"https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

response4 = requests.get(url3, headers=headers)
p4=response4.json()
a=p4["total_pages"]
if a<=500:
  tx=random.randint(1,a)
else:
    tx=random.randint(1,500)
ty=random.randint(1,10)

if hero:
 
    popular(ty,tx)
    
    
    
    st.markdown(f"""
        <div style="background-color: grey-black;width:600px;height:300px; ; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0, 0, 0, 1), -2px -2px 5px rgba(0, 0, 0, 1);">
                 <img src="https://image.tmdb.org/t/p/w500{poster}" style="border: 1px solid Lightgrey; width:250px; height:250px; margin-left:5px; margin-top:20px; float:left;">
                 <p style= "text-align:center;font-family:courier;padding-top:30px;">Title:<strong>{y}</strong></p>
                 <p style= "text-align:center;font-family:courier;">Release-date:<strong>{y1}</strong></p>
                 <p style= "text-align:center;font-family:courier;">Vote-Average:<strong>{y2}</strong></p>
                 <p style= "text-align:center;font-family:courier;">Vote-Count:<strong>{y3}</strong></p>
                 <p style= "text-align:center;font-family:courier;"><a href="https://www.imdb.com/title/{y5}/">IMDB Link</a></p>
                 
                 
            
        </div>
    """, unsafe_allow_html=True)
