from dotenv import load_dotenv
import os, requests, json

load_dotenv()

API_KEY = os.getenv("API_KEY")

def message_handler_main_function(input_text):
    message = str(input_text).lower()
    

    # greet message command
    if message in ['/greet', '/Greet', '/hello', '/hoi', '/hey']:
        return "Waddup nerd 🤓"
    
    # crypto info command
    if 'crypt_info' in message:
        coins = message.split()[1:]
        formatted_ids = ""
        for id in coins:
            formatted_ids += id.upper()+','
        formatted_ids = formatted_ids[:-1]
        try:
            response = requests.get("https://api.nomics.com/v1/currencies/ticker?key=" + API_KEY + "&ids=" + formatted_ids + "&interval=1d&convert=INR&per-page=100&page=1")

        except Exception as e:
            return "Error: " + e
        data = response.text

        json_file = json.loads(data)
        if len(json_file) < 1:
            return "Enter a valid coin name!"
        # print(json.dumps(json_file, indent = 3))
        
        final_response = ""
        for coin_idx in range(len(formatted_ids.split(','))):
            final_response += "Coin ID:" + "\t" +  formatted_ids.split(',')[coin_idx] + "\n"
            final_response += "Coin name:" + "\t" + json_file[coin_idx]['name'] + "\n"
            final_response += "Coin price:" + "\t₹" + str(round(float(json_file[coin_idx]['price']), 2)) + "\n"
            final_response += "Coin rank:" + "\t" + json_file[coin_idx]['rank'] + "\n"
            final_response += "Coin change in rank:" + "\t" + json_file[coin_idx]['rank_delta'] + "\n"
            final_response += "\n\n"

        return final_response
    
    return "Sorry I do not understand that!"