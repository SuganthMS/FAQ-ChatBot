import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

faq = """
Frequently Asked Questions

Q: Hi, Hello, Hey You, Greetings, Good Morning, Good Afternoon, Good Evening
A:  Hello,"Namaskara! 👋 Welcome to the Bengaluru Namma Metro (BMRCL) Assistant. How may I help you today?"

Q: What is Namma Metro?
A: Namma Metro is the rapid transit system operated by Bangalore Metro Rail Corporation Limited (BMRCL), serving Bengaluru.

Q: What are the operating hours of Namma Metro?
A: Metro services operate according to the official timetable published by BMRCL. Timings may change based on operational requirements and special occasions. Please check the official website for the latest schedule.

Q: Where can I check today's metro timings?
A: You can check the latest metro timings on the official BMRCL website under the Metro Timings section.

Q: What types of metro tickets are available?
A: Namma Metro offers QR Tickets, Single Journey Tokens, Smart Cards, and Day Passes.

Q: What is a QR Ticket?
A: A QR Ticket is a digital ticket that allows passengers to travel without purchasing a physical token.

Q: What is a Smart Card?
A: A Smart Card is a rechargeable contactless card that allows multiple metro journeys and offers fare discounts.

Q: Does the Smart Card provide any discount?
A: Yes. Smart Card users receive fare discounts as per BMRCL's current fare policy.

Q: What is the Smart Card deposit amount?
A: The Smart Card has a refundable security deposit as specified by BMRCL.

Q: How can I recharge my Smart Card?
A: You can recharge your Smart Card at metro stations, through the Namma Metro App, the BMRCL website, Paytm, or Amazon Pay. Online top-ups may require validation at a station.

Q: What is the maximum recharge amount for a Smart Card?
A: The Smart Card can be recharged up to the maximum value specified by BMRCL.

Q: Are Day Passes available?
A: Yes. One-day, three-day, and five-day passes are available for unlimited travel during their validity period.

Q: Can tourists purchase Day Passes?
A: Yes. Tourists and regular passengers can purchase Day Passes.

Q: Where can I buy metro tickets?
A: Tickets can be purchased from station ticket counters, ticket vending machines, or through QR ticket options.

Q: Can I use UPI to buy tickets?
A: Yes. Many stations support UPI payments for ticket purchases and recharges.

Q: Can I use debit or credit cards at stations?
A: Yes. Most metro stations accept debit and credit cards.

Q: Is parking available at metro stations?
A: Parking is available at selected metro stations. Charges vary by station.

Q: Can I carry luggage on the metro?
A: Yes. Small and medium-sized luggage is permitted, subject to BMRCL's baggage rules.

Q: Are pets allowed on Namma Metro?
A: No. Pets are generally not allowed inside metro trains or stations.

Q: Is photography allowed inside metro stations?
A: Photography may be restricted in certain areas. Please follow station guidelines and staff instructions.

Q: Are metro stations accessible for differently-abled passengers?
A: Yes. Most stations provide lifts, escalators, tactile paths, and wheelchair accessibility.

Q: Is Wi-Fi available at metro stations?
A: Wi-Fi availability depends on the station and BMRCL services.

Q: Can I eat or drink inside the metro?
A: No. Eating and drinking inside metro trains is generally prohibited.

Q: What should I do if I lose my belongings?
A: Contact the station customer care desk or BMRCL helpline immediately.

Q: What happens if I lose my Smart Card?
A: Report the loss to BMRCL customer care for assistance regarding card blocking or replacement.

Q: How do I contact BMRCL customer support?
A: You can contact BMRCL through its customer care helpline or email available on the official website.

Q: What is the BMRCL customer care email?
A: travelhelp@bmrc.co.in

Q: What is the BMRCL helpline number?
A: Toll-free helpline: 1800-425-12345.

Q: Can I file a complaint online?
A: Yes. Passengers can contact BMRCL through the official website or customer support email.

Q: Is the metro available on weekends?
A: Yes. Metro services operate on weekends, although timings may differ from weekdays.

Q: Do metro timings change during festivals?
A: Yes. BMRCL may modify metro timings during festivals, public holidays, or special events.

Q: Can I check metro fare online?
A: Yes. The latest fare chart is available on the official BMRCL website.

Q: Does Namma Metro have a mobile app?
A: Yes. The Namma Metro mobile app provides ticketing, Smart Card recharge, and other passenger services.

Q: Can I travel with children?
A: Yes. Children are allowed to travel according to BMRCL's ticketing rules.

Q: What items are prohibited inside the metro?
A: Dangerous goods, explosives, flammable materials, and other prohibited items are not allowed.

Q: What should I do during an emergency?
A: Follow announcements, use emergency communication devices if needed, and follow instructions from metro staff.

Q: Can I use the metro during heavy rain?
A: Yes. Metro services generally continue during rain unless there are operational disruptions.

Q: Is there a lost and found service?
A: Yes. Contact the station where the item was lost or BMRCL customer care.

Q: Where can I get the latest BMRCL information?
A: Visit the official BMRCL website: https://www.bmrc.co.in/

Q: How many metro lines are currently operational?
A: Namma Metro currently operates the Purple Line, Green Line, and Yellow Line. Additional lines are under construction as part of the network expansion.

Q: What is the Purple Line?
A: The Purple Line connects Whitefield (Kadugodi) to Challaghatta and runs from East Bengaluru to West Bengaluru.

Q: What is the Green Line?
A: The Green Line connects Madavara to Silk Institute and runs from North Bengaluru to South Bengaluru.

Q: What is the Yellow Line?
A: The Yellow Line connects R.V. Road to Bommasandra and provides metro connectivity to Electronics City.

Q: Which colour is the Purple Line?
A: Purple.

Q: Which colour is the Green Line?
A: Green.

Q: Which colour is the Yellow Line?
A: Yellow.

Q: Which colour is the Pink Line?
A: Pink. It is currently under construction.

Q: Which colour is the Blue Line?
A: Blue. It is currently under construction.

Q: What are the terminal stations of the Purple Line?
A: Whitefield (Kadugodi) and Challaghatta.

Q: What are the terminal stations of the Green Line?
A: Madavara and Silk Institute.

Q: What are the terminal stations of the Yellow Line?
A: R.V. Road and Bommasandra.

Q: Which metro lines are under construction?
A: Pink Line (Kalena Agrahara to Nagawara), Blue Line (Central Silk Board to Kempegowda International Airport), and other future expansion corridors.

Q: What are the metro operating hours?
A: Metro services generally start between 5:00 AM and 6:00 AM and run until around 11:00 PM to 11:55 PM. Sunday services usually begin around 7:00 AM.

Q: What is the minimum metro fare?
A: The minimum metro fare starts from ₹10.

Q: What is the maximum metro fare?
A: The maximum fare depends on the distance travelled according to the latest BMRCL fare chart.

Q: How is the metro fare calculated?
A: The fare is calculated based on the travel distance between the source and destination stations.

Q: What ticket options are available?
A: QR Ticket, Smart Card, Single Journey Token, and Day Pass.

Q: Can I buy metro tickets online?
A: Yes. Tickets can be purchased using the Namma Metro App and supported partner applications.

Q: Can I use UPI to buy metro tickets?
A: Yes. UPI payments are accepted at most metro stations.

Q: What is a Smart Card?
A: A Smart Card is a rechargeable contactless travel card for regular metro commuters.

Q: Can I recharge my Smart Card online?
A: Yes. Smart Cards can be recharged online.

Q: Where can I recharge my Smart Card?
A: At metro stations, through the Namma Metro App, the official BMRCL website, Amazon Pay, and Paytm.

Q: Are Day Passes available?
A: Yes.

Q: What Day Passes are available?
A: One-Day Pass, Three-Day Pass, and Five-Day Pass.

Q: How do I travel from Whitefield to Majestic?
A: Take the Purple Line from Whitefield (Kadugodi) to Nadaprabhu Kempegowda Station (Majestic).

Q: How do I travel from Silk Institute to Cubbon Park?
A: Take the Green Line to Majestic, then change to the Purple Line towards Whitefield and get down at Cubbon Park.

Q: Where can I interchange between the Purple Line and Green Line?
A: Nadaprabhu Kempegowda Station (Majestic).

Q: Where can I interchange between the Green Line and Yellow Line?
A: R.V. Road Metro Station.

Q: Is parking available at metro stations?
A: Parking is available at selected Namma Metro stations.

Q: I lost my belongings. What should I do?
A: Contact the station control room or BMRCL Customer Care immediately.

Q: Are lifts available at metro stations?
A: Yes.

Q: Are escalators available at metro stations?
A: Yes.

Q: Is wheelchair access available?
A: Yes. Most metro stations are accessible for differently-abled passengers.

Q: What is the BMRCL customer care number?
A: Toll-Free: 1800-425-12345.

Q: What is the BMRCL customer support email?
A: [travelhelp@bmrc.co.in](mailto:travelhelp@bmrc.co.in).

Q: Does Namma Metro have a mobile app?
A: Yes. The Namma Metro App allows passengers to purchase QR tickets, recharge Smart Cards, check fares, and access metro information.

Q: Can I carry luggage on the metro?
A: Yes. Small and medium-sized luggage is allowed as per BMRCL rules.

Q: Are pets allowed on the metro?
A: No. Pets are generally not permitted inside metro stations and trains.

Q: Is eating allowed inside metro trains?
A: No. Eating and drinking inside metro trains are prohibited.

Q: Is photography allowed inside metro stations?
A: Photography may be restricted in certain areas. Please follow BMRCL guidelines.

Q: What items are prohibited inside the metro?
A: Explosives, flammable materials, dangerous chemicals, weapons, and other prohibited items are not allowed.

Q: What should I do during an emergency?
A: Follow station announcements, use emergency communication systems if necessary, and follow the instructions of BMRCL staff.

Q: Can I check metro fares online?
A: Yes. The latest fare chart and fare calculator are available on the official BMRCL website.

Q: Where can I find the latest BMRCL updates?
A: Visit the official BMRCL website at https://www.bmrc.co.in.

Q: Are lifts available at metro stations?
A: Yes.

Q: Are escalators available?
A: Yes.

Q: Is wheelchair access available?
A: Yes. Most metro stations are accessible for differently-abled passengers.

Q: Does Namma Metro have a mobile app?
A: Yes. The Namma Metro mobile app allows passengers to purchase QR tickets, recharge Smart Cards, check fares, and access metro information.

Q: Which metro lines are under construction?
A: The following metro lines are under construction:

Pink Line – Kalena Agrahara ↔ Nagawara
Blue Line – Central Silk Board ↔ Kempegowda International Airport
Red Line – Proposed Sarjapur ↔ Hebbal Corridor (Planning Stage)

Q: How many metro lines are currently operational?
A: Namma Metro currently operates the Purple Line, Green Line, and Yellow Line. Additional lines are under construction as part of the network expansion.

Q: What is the Purple Line?
A: Purple Line connects Whitefield (Kadugodi) to Challaghatta and runs east to west across Bengaluru.

Q: What is the Green Line?
A: Green Line connects Madavara to Silk Institute and runs north to south.

Q: What is the Yellow Line?
A: Yellow Line connects R.V. Road to Bommasandra, providing metro access to Electronics City.

Q: What is the minimum metro fare?
A: The minimum fare starts at approximately ₹10.

Q: What is the maximum metro fare?
A: The maximum fare depends on the distance travelled and BMRCL's current fare structure. Use the official fare calculator for the latest amount.

Q: How is the fare calculated?
A: Fare is calculated based on the distance travelled between the origin and destination stations.

Q: What ticket options are available?
A:

• QR Ticket

• Smart Card

• Single Journey Token

• Day Pass

Q: Can I buy tickets online?
A: Yes. Tickets can be purchased using the Namma Metro App and supported partner apps.

Q: Can I use UPI?
A: Yes.

Q: I lost my bag. What should I do?
A: Contact the station control room or BMRCL customer care immediately.

Q: How do I travel from Whitefield to Majestic?
A: Take the Purple Line from Whitefield (Kadugodi) to Nadaprabhu Kempegowda Station (Majestic).

Q: How do I travel from Silk Institute to Cubbon Park?
A: Take the Green Line to Majestic and interchange to the Purple Line toward Whitefield. Get down at Cubbon Park.

Q: Where can I interchange between Purple and Green Lines?
A: Nadaprabhu Kempegowda Station (Majestic).

Q: Where can I interchange between Green and Yellow Lines?
A: R.V. Road.

Q: Thankyou, Bye, Enough, That's all, I am done, I have no more questions, I have no further queries, I have no more queries, I have no more questions for now, I have no further questions, I have no further queries for now
A:  "Thank you for choosing Namma Metro. Wishing you a safe and comfortable journey. Have a wonderful day! 🚇😊
     If you have any more questions in the future, feel free to ask. Have a great day!
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    prompt = f"""
You are an FAQ chatbot.

Answer ONLY using the FAQ below.
If the answer is not available, reply:
"Sorry, I couldn't find that information."

FAQ:
{faq}

User Question:
{user_message}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)