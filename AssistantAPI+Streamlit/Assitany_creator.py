from openai import OpenAI
client = OpenAI(api_key=" ")

file="/Users/jiapannan/PycharmProjects/pythonProject/pythonProject/1000 Assistant API/assistant_api/SeoulTourismPlaces.html"

def file_upload(file):
    file = client.files.create(
        file=open(file, "rb"),
        purpose="assistants")
    
    # print(file)  # file-6Dd5teLybO6sqa9yJa53dZeq
    return file.id

# file_id = file_upload(file)        
    
def assistant_creator():
    my_assistant = client.beta.assistants.create(
        instructions="""
        TO-DO: 
        - You are an expert in making travel plans for Seoul based on your LLM model and the given Retrieval file SeoulTourismPlaces.html. 
        - For every suggested place that you've mentioned in the reply message, you will add a clickable link to the suggested places by using the links in the SeoulTourismPlaces.html.

        Expected outcome:
        - A day-to-day travel internity for planning request
        -further explore links provided for suggested places by using the given file SeoulTourismPlaces.html  
        - When the user asks for additional information about a place, provide the full url address from the SeoulTourismPlaces.html and give a short summary
        - Output example: 
        "1일차:첫째 날은 서울의 대표적인 자연 경관 중 하나인 남산을 방문하여 서울의 전경을 조망해 보세요. [남산 서울타워 정보 보러가기](explorer_URL for 남산 서울타워)

        About SeoulTourismPlaces.html: 
        - For the provided Retrieval file SeoulTourismPlaces.html, it contains 3 types of information: place_name,  explorer_URL, and service_type.
        - The service_name is the hotels, attractions, and restaurant names in Seoul
        - The explorer_URL is a webpage URL to help users explore additional information. When the user accesses the website can get up-to-date information and increase the visibility of a place. 
        - The service_type identifies whether the place is an attraction, restaurant, or hotel. 
        - the restaurant_menu is special for restaurants 
        - the tag_of_attraction is special for attraction and has identified the attraction's features     
        """,
        name="Travel Panda Seoul Expert",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=["file-6Dd5teLybO6sqa9yJa53dZeq"],
    )
    print(my_assistant) # asst_FPlHYRozJhMRSNBZoC8qgusB
    
    return my_assistant.id

# my_assistant_id = assistant_creator()

empty_thread = client.beta.threads.create()
print(empty_thread) # thread_NhwJvYxk1zDrs5CzyyLO8q4s

