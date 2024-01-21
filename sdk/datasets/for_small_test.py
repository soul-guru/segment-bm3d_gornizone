messages_40_words = [
    "Hey there, I was wondering if you could help me out with my computer. It's been acting really strange lately, not turning on properly and sometimes freezing for no reason. I've tried restarting it and checking the cables, but nothing seems to work.",
    "I'm planning a surprise birthday party for our friend next weekend. We need to organize a venue, decorations, a cake, and invite all our friends without her finding out. It's going to be a challenge, but I think we can pull it off.",
    "I recently started a new diet and exercise routine to improve my health. It involves waking up early for a jog, followed by a breakfast of oats and fruits. Lunch is usually a salad, and dinner is protein-rich with vegetables. I also drink plenty of water.",
    "Can you believe how quickly technology is advancing these days? Just yesterday, I read about a new smartphone with amazing features like a 108MP camera, 5G connectivity, and an AI assistant that can practically read your mind. It's incredible, but also a bit scary.",
    "I had a really interesting conversation with my neighbor about climate change and its impact on our planet. We discussed renewable energy sources, carbon footprint reduction, and how each individual's efforts can make a difference. It was quite enlightening.",
    "I'm struggling with this new project at work. It requires a lot of data analysis and creative problem-solving, which is usually my forte, but I'm hitting a wall. Maybe I need a fresh perspective or someone to brainstorm ideas with.",
    "I just finished reading a fascinating book about the history of ancient civilizations. It's amazing to think about how societies were formed, the innovations they made, and how their discoveries influence our lives today. It really puts things into perspective.",
    "My friend is going through a tough time with her family. They've been having disagreements and it's putting a strain on their relationships. I've been trying to offer support and advice, but it's a delicate situation that needs careful handling.",
    "I've been thinking a lot about our environmental impact and how we can live more sustainably. Simple changes like reducing plastic use, recycling more, and using public transport can make a big difference. It's all about being more conscious of our choices.",
    "Planning a vacation can be so stressful but also exciting. I have to book flights, hotels, and figure out the itinerary. I want to make sure we have a good mix of relaxation and adventure. It's a lot to think about but I can't wait."
]

messages_20_words = [
    "Do you have any recommendations for good restaurants nearby? I'm looking for something with a cozy atmosphere and delicious food.",
    "I'm thinking of taking up a new hobby, like painting or photography. I want something creative to relax and express myself.",
    "My laptop has been really slow lately. I think it might be a virus or maybe it's just old and needs replacing.",
    "I'm trying to organize a group outing for next weekend. Maybe a hike or a picnic in the park. Any interest?",
    "I watched an incredible movie last night. It was full of suspense and had a twist ending that I didn't see coming.",
    "I'm feeling a bit overwhelmed with all the work I have. Deadlines are approaching and I need to focus and prioritize.",
    "The weather has been so unpredictable lately. One minute it's sunny and the next it's pouring rain. Hard to plan anything.",
    "I'm looking for a good book to read. Something gripping and thought-provoking. Any genre is fine, just need a good story.",
    "Have you heard the latest album by that new artist? It's a great mix of genres and really catchy tunes.",
    "My garden is finally starting to bloom. The flowers look beautiful and there's a sense of peace watching them grow."
]

messages_10_words = [
    "Can you send me the report by this afternoon, please?",
    "Thinking of going for a run later, want to join?",
    "Had the best coffee today at a new café downtown.",
    "Can't find my keys, have you seen them anywhere?",
    "Need to buy groceries. Anything specific you want for dinner?",
    "The meeting got rescheduled to Thursday, just letting you know.",
    "Feeling under the weather today, might take a day off.",
    "What time is our reservation tonight? I forgot to check.",
    "Could you help me study for my exam tomorrow?",
    "Saw a cute dog at the park today, made my day."
]

short_messages = [
    "How's your day going?",
    "Loved the movie last night!",
    "What's for dinner?",
    "Miss you a lot.",
    "Need any help?",
    "Great job on that!",
    "Let's catch up soon.",
    "Safe travels!",
    "Good morning!",
    "Feeling much better, thanks."
]


def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


ranked_messages = [
    short_messages,
    messages_10_words,
    messages_20_words,
    messages_40_words
]

all_messages = flatten_list(ranked_messages)