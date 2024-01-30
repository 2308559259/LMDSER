import json
import openai
openai.api_key = "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"

import os
os.environ["http_proxy"]="127.0.0.1:7890"
os.environ["https_proxy"]="127.0.0.1:7890"


def step_enhancement(D):
    task_instruct="Identify the parts of Step-A that can supplement Step-B.\n"
    example2="title: How to Buy on Ticketmaster\npart: Steps\nheadline: Create a Ticketmaster account.\ntext: This will enable you to do more than just recovering passwords and order histories, etc. It helps you save personal information (such as credit/debit card information), as well as the ability to print out receipts and tickets as soon as they are purchased.\nheadline: Specify your city.\ntext: This will allow you to filter specific categories and events related to what is planned in the future.\nheadline: Find your event category.\ntext: Search and browse around from sports games to rock concerts or family friendly events. If you know of a future event but Ticketmaster does not show it in the search, please know that tickets are not going to be available until a later date. If the option \”Find Tickets\” is enabled, it means that tickets are on sale.\nheadline: Look at the top right for specific information.\ntext: This informs the public of the on-sale dates and times (including any exclusive pre-sale dates/times), price ranges for all tickets, and extra details concerning the specific event (such as ticket limits per household, etc).\nheadline: Study the seating chart.\ntext: This can not be expressed enough. Even if it's in the same arena/venue, the seating charts will not be the same as another show/event (for example, concert vs. basketball game). You need to know how close or how far you will be away from the main entertainment or stage, as well as different levels (if applicable), as there is a clear difference between a floor seat and balcony seat (bleeder or near the ceiling).\nLots of venue websites, especially the ones located in metropolitan cities, have their own seating chart for different events.\nheadline: Choose your ticket amounts, price of the tickets you're willing to pay, and seat area for that price.\ntext: If you're a beginner to Ticketmaster or want the site to choose for you for flexibility, then choosing \”Best Price\” is preferable. Also, for events that are in demand or very popular, you might want to go through that route instead of trying to get the best seats. Click on the red \”Find Tickets\”.\nheadline: Go through Ticketmaster's CAPTCHA.\ntext: This is a tool to discourage bots from using the website in order to gain tickets in a non-human method.\nheadline: Review the seating ticket on the next screen.\ntext: It might look like a lot, thus why it's very important to look at the seating chart. This will give you a preview of what specific seat you are paying for, the specific price for it, etc. You need to know that every ticket reviewed as a \”timer\” in the bottom right hand corner. This is the amount of time you have to make a decision if you want the seat(s) or change your mind. You can either \”Continue\” on to purchase it if you're satisfied or \”Search Again\”. Searching again will then bring you back to the main ticket page for the event and place your old review back into the queue for anyone else to grab.\nKnow that when the general public is allowed to purchase tickets and depending on the demand/popularity of the event, you may/may not receive a better ticket than the last, so be careful how much time you spend on each ticket review.\nheadline: Continue on with purchasing.\ntext: You'll need to enter your credit card information or how you will be paying for the tickets. Having an account has it's perks, as you wouldn't need to worry about inputting information every time. This page also has it's own unique timer, so please be sure that you have everything in front of you beforehand.\nheadline: Choose your delivery method.\ntext: Shipping methods look exactly like as if you're purchasing any other item online. Depending on where you live, you might find ground shipping to be the most efficient. If the event date is closer than a month or you wish to have the tickets immediately, choose the option of printing your tickets out or picking them up at the local box office. When printing tickets out, they will be an actual ticket, just on a 8\”x11\” paper instead of regular ticket stubs - remember to bring the entire paper with you to the event! Please summarize the flowchart of the above sentences briefly.\nScript: 1. Create a Ticketmaster account to save personal information and print receipts and tickets.\n2. Specify your city to filter specific categories and events.\n3. Find your event category and check if tickets are on sale.\n4. Look at the top right for specific information about on-sale dates, times, and ticket limits.\n5. Study the seating chart to choose your preferred seat area.\n6. Choose your ticket amounts, price, and seat area for that price.\n7. Go through Ticketmaster's CAPTCHA to discourage bots.\n8. Review the seating ticket on the next screen and make a decision within the timer.\n9. Continue on with purchasing by entering your payment information.\n10. Choose your delivery method.\ntitle: How to Choose a Crystal That Works for You\npart: Steps\nheadline: Open your mind to the idea that each crystal has an exclusive 'energy medicine' that can assist you in your life right now.\ntext: Remember, the Ancients have known about the power of crystals for centuries!\nheadline: Allow yourself to be intuitive to the process of choosing a crystal, instead of thinking too much about it.\ntext: So 'think less and feel more'!\nheadline: Be specific about your issue before choosing a crystal.\ntext: So take some time to write down the problem that you want some healing energy assistance with.\nheadline: Ask the Universe just before you are about to pick a crystal 'reveal to me directly, which crystal I need right now to help me (with this issue I am having / working through)'?\ntext: \nheadline: Let the crystal reveal itself to you!\ntext: I know this sounds weird, but after you've asked your question, be open to the crystal you need in your life right now, being more profound than the rest, as if it's jumping out at you.\nheadline: Use your hands to feel the energy of the crystals to know which ones you are more sensitive to.\ntext: You may feel energy pull from the crystals to your palm (like your hand becomes a magnet), this often means this is the right crystal for you.\nheadline: If you are buying crystals online and can't have the hands-on experience of feeling the energy of a crystal you might want to work with, simply write the name of several crystals you are interested in on pieces of paper.\ntext: Put these in a box and pull out a paper at random. Whatever the crystal is you select, this is the one you will use first.\nScript: 1. opening your mind to the idea of crystal energy.\n2. being intuitive instead of overthinking.\n3. being specific about the issue you want help with.\n4. asking the universe for guidance.\n5. letting the crystal reveal itself.\n6. feeling the energy with your hands.\n7. if buying online, selecting at random from a list of crystals you're interested in."
    example1="title: How to Buy on Ticketmaster\npart: Steps\nheadline: Create a Ticketmaster account.\ntext: This will enable you to do more than just recovering passwords and order histories, etc. It helps you save personal information (such as credit/debit card information), as well as the ability to print out receipts and tickets as soon as they are purchased.\nheadline: Specify your city.\ntext: This will allow you to filter specific categories and events related to what is planned in the future.\nheadline: Find your event category.\ntext: Search and browse around from sports games to rock concerts or family friendly events. If you know of a future event but Ticketmaster does not show it in the search, please know that tickets are not going to be available until a later date. If the option \”Find Tickets\” is enabled, it means that tickets are on sale.\nheadline: Look at the top right for specific information.\ntext: This informs the public of the on-sale dates and times (including any exclusive pre-sale dates/times), price ranges for all tickets, and extra details concerning the specific event (such as ticket limits per household, etc).\nheadline: Study the seating chart.\ntext: This can not be expressed enough. Even if it's in the same arena/venue, the seating charts will not be the same as another show/event (for example, concert vs. basketball game). You need to know how close or how far you will be away from the main entertainment or stage, as well as different levels (if applicable), as there is a clear difference between a floor seat and balcony seat (bleeder or near the ceiling).\nLots of venue websites, especially the ones located in metropolitan cities, have their own seating chart for different events.\nheadline: Choose your ticket amounts, price of the tickets you're willing to pay, and seat area for that price.\ntext: If you're a beginner to Ticketmaster or want the site to choose for you for flexibility, then choosing \”Best Price\” is preferable. Also, for events that are in demand or very popular, you might want to go through that route instead of trying to get the best seats. Click on the red \”Find Tickets\”.\nheadline: Go through Ticketmaster's CAPTCHA.\ntext: This is a tool to discourage bots from using the website in order to gain tickets in a non-human method.\nheadline: Review the seating ticket on the next screen.\ntext: It might look like a lot, thus why it's very important to look at the seating chart. This will give you a preview of what specific seat you are paying for, the specific price for it, etc. You need to know that every ticket reviewed as a \”timer\” in the bottom right hand corner. This is the amount of time you have to make a decision if you want the seat(s) or change your mind. You can either \”Continue\” on to purchase it if you're satisfied or \”Search Again\”. Searching again will then bring you back to the main ticket page for the event and place your old review back into the queue for anyone else to grab.\nKnow that when the general public is allowed to purchase tickets and depending on the demand/popularity of the event, you may/may not receive a better ticket than the last, so be careful how much time you spend on each ticket review.\nheadline: Continue on with purchasing.\ntext: You'll need to enter your credit card information or how you will be paying for the tickets. Having an account has it's perks, as you wouldn't need to worry about inputting information every time. This page also has it's own unique timer, so please be sure that you have everything in front of you beforehand.\nheadline: Choose your delivery method.\ntext: Shipping methods look exactly like as if you're purchasing any other item online. Depending on where you live, you might find ground shipping to be the most efficient. If the event date is closer than a month or you wish to have the tickets immediately, choose the option of printing your tickets out or picking them up at the local box office. When printing tickets out, they will be an actual ticket, just on a 8\”x11\” paper instead of regular ticket stubs - remember to bring the entire paper with you to the event! Please summarize the flowchart of the above sentences briefly.\nScript: 1. Create a Ticketmaster account to save personal information and print receipts and tickets.\n2. Specify your city to filter specific categories and events.\n3. Find your event category and check if tickets are on sale.\n4. Look at the top right for specific information about on-sale dates, times, and ticket limits.\n5. Study the seating chart to choose your preferred seat area.\n6. Choose your ticket amounts, price, and seat area for that price.\n7. Go through Ticketmaster's CAPTCHA to discourage bots.\n8. Review the seating ticket on the next screen and make a decision within the timer.\n9. Continue on with purchasing by entering your payment information.\n10. Choose your delivery method."
    example="title: How to Go Adventuring as a Teen\npart: Steps\nheadline: Teens, let's read the first step.\ntext: Gather all the essentials and store them properly in a backpack. If you don't have a backpack, buy one. The things stored in your essentials should be\u00a0:\nA few ropes\nHooks Dry and warm clothes Synthetic or light clothes A good pair of shoes\na 600ml water bottle\nsome amount of food Magnifier a mirror or a signaling deviceBinoculars\nA map of the jungle or the area you are going\nheadline: After gathering the essentials, you have to learn some techniques.\ntext: Some of them are\u00a0:\nMaking water Outdoor Fire Skills\nAbility to survive in the wild\nTo find water and food in the wild\nSkills to make shelter\nAbility to identify snakes and dangerous insects\nCatching fishes\nMake use of nature\nTo Predict the weather using clouds\nheadline: Make sure you have all the essentials and practised all the techniques.\ntext: Take parental guidance and adult supervision before doing an adventure. If you feel you are not safe, do adventures in a group of four or five. Your friends could be your source of success. Do adventures and have fun.\nscript: 1. gather all the essentials and store them properly in a backpack.\n2. you must learn some techniques, such as making water, outdoor fire skills, and the ability to survive in the wild.\n3. After gathering the essentials and practicing the techniques, take parental guidance and adult supervision before doing an adventure.\n4. It's important to do adventures in a group of four or five for safety, and friends can be a source of success.\ntitle: How to Deprogram a Religious Cult Member1\npart: Understanding the Situation\nheadline: Notice signs of a cult.\ntext: Some religions are very community-based or unusual, but this does not automatically make the group a cult.\nThey spend time only with other members, pushing everyone else away\nThey don't trust anyone other than their \"superiors\" within the group\nThey try to convince family and friends to be a part of their group\nThey don't have normal conversations about anything other than \"God,\" their group leaders, or the \"salvation\" available only within the group\nheadline: Recognize that good, reasonable people can end up in cults.\ntext: Vulnerable people are at risk. Many of them are lonely and lacking in confidence, and are naive and idealistic. Many people who fall victims to cults are well-adjusted.Someone facing instability in their lives\nBright people with no sense of direction\nPeople facing problems such as a bad breakup or personal failure\nPeople with problems at home\nheadline: Research cults.\ntext: It can help to have a better understanding of the institution that your loved one has fallen victim to. Find out how cults work, so you know what the person is facing. Please summarize the flowchart of the above sentences briefly.\nscript: 1. notice signs of a cult, such as spending time only with other members, not trusting anyone outside the group, and trying to convince others to join.\n2. It's important to recognize that good, reasonable people can end up in cults due to vulnerability, instability, or personal problems.\n3. Researching cults can also help in understanding the situation."
    model ='text-davinci-003'
    script=[]

    for i in range(0,300):
        prompt=task_instruct+"\n"+example+"\n"+example1+example2+D[i]['text']+"\nscript: "


        try:
            response = openai.Completion.create(
                model= model,
                prompt=prompt,
                temperature=0,
                max_tokens=500,
                frequency_penalty=0.2,
                presence_penalty=0.15,
                stream=True,
            )
            # print(self.bot,response)
            script.append({"title":D[i]["title"],"text":D[i]["text"],"script":response["choices"][0]["text"].strip()})
            print(i)
            print(response["choices"][0]["text"].strip())


        except Exception as exc:
            print(i,exc)

        if (i+1)%500==0:
            with open("./data/script"+str(i)+".json","w") as f:
                json.dump(script,f)

    with open("./data/script"+str(i)+".json","w") as f:
        json.dump(script,f)



with open("./data/hierarchy.json",'r',encoding='utf-8')as fp:
    D = json.load(fp)
    enhancement_script=enhancement(enhancement)

    json.dump(enhancement_script, '../data_process/enhancement_script.json')


