from dotenv import load_dotenv
import os
from langchain_core.prompts import  PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama



load_dotenv()




def main():
    
    print("Hello from langchain!")
    # print(os.environ.get("OPENAI"))
    
    information = """ 
    "Gandhi" redirects here. For other uses, see Gandhi (disambiguation).
Mahātmā
Mohandas Gandhi

Gandhi in 1931
Born	Mohandas Karamchand Gandhi
2 October 1869
Porbandar, Kathiawar Agency, India
Died	30 January 1948 (aged 78)
New Delhi, India
Cause of death	Assassination by gunshot
Monuments	
Raj Ghat, Delhi
Gandhi Smriti, New Delhi
Other names	Bāpū (father), Rāṣṭrapitā (the Father of the Nation)
Alma mater	
Samaldas Arts College[a]
University College London[b]
Inns of Court School of Law
Occupations	
Lawyeractivistpolitician
Years active	1893–1948
Known for	
Leadership of the campaign for India's independence from British rule
Nonviolent resistance
Political party	Indian National Congress (1920–1934)
Spouse	Kasturba Gandhi
​
​(m. 1883; died 1944)​
Children	
HarilalManilalRamdasDevdas
Parents	
Karamchand Gandhi
Putlibai Gandhi
Relatives	Gandhi family
President of the Indian National Congress
In office
December 1924 – April 1925
Preceded by	Maulana Azad
Succeeded by	Sarojini Naidu
Mahatma Gandhi's voice
Duration: 6 minutes and 5 seconds.6:05
Gandhi's spiritual message to the world
Recorded 17 October 1931
Signature
Signature of Gandhi
Mohandas Karamchand Gandhi[c] (2 October 1869 – 30 January 1948)[2] was an Indian lawyer, anti-colonial activist, and political ethicist who employed nonviolent resistance to lead the successful campaign for India's independence from British rule. He inspired movements for civil rights and freedom across the world. The honorific Mahātmā (from Sanskrit, meaning great-souled, or venerable), first applied to him in South Africa in 1914, is used worldwide.[3]

Born and raised in a Hindu family in coastal Gujarat, Gandhi trained in the law at the Inner Temple in London and was called to the bar at the age of 22. After two uncertain years in India, where he was unable to start a successful law practice, Gandhi moved to South Africa in 1893 to represent an Indian merchant in a lawsuit. He went on to live in South Africa for 21 years. Here, Gandhi raised a family and first employed nonviolent resistance in a campaign for civil rights. In 1915, aged 45, he returned to India and soon set about organising peasants, farmers, and urban labourers to protest against discrimination and excessive land tax.

Assuming leadership of the Indian National Congress in 1921, Gandhi led nationwide campaigns for easing poverty, expanding women's rights, building religious and ethnic amity, ending untouchability, and, above all, achieving swaraj or self-rule. Gandhi adopted the short dhoti woven with hand-spun yarn as a mark of identification with India's rural poor. He began to live in a self-sufficient residential community, to eat simple food, and undertake long fasts as a means of both introspection and political protest. Bringing anti-colonial nationalism to the common Indians, Gandhi led them in challenging the British-imposed salt tax with the 400 km (250 mi) Dandi Salt March in 1930 and in calling for the British to quit India in 1942. He was imprisoned many times and for many years in both South Africa and India.

Gandhi's vision of an independent India based on religious pluralism was challenged in the early 1940s by a Muslim nationalism which demanded a separate homeland for Muslims within British India. In August 1947, Britain granted independence, but the British Indian Empire was partitioned into two dominions, a Hindu-majority India and a Muslim-majority Pakistan. As many displaced Hindus, Muslims, and Sikhs made their way to their new lands, religious violence broke out, especially in the Punjab and Bengal. Abstaining from the official celebration of independence, Gandhi visited the affected areas, attempting to alleviate distress. In the months following, he undertook several hunger strikes to stop the religious violence. The last of these was begun in Delhi on 12 January 1948, when Gandhi was 78. The belief that Gandhi had been too resolute in his defence of both Pakistan and Indian Muslims spread among some Hindus in India. Among these was Nathuram Godse, a militant Hindu nationalist from Pune, western India, who assassinated Gandhi by firing three bullets into his chest at an interfaith prayer meeting in Delhi on 30 January 1948.

Gandhi's birthday, 2 October, is commemorated in India as Gandhi Jayanti, a national holiday, and worldwide as the International Day of Nonviolence. Gandhi is considered to be the Father of the Nation in post-colonial India. During India's nationalist movement and in several decades immediately after, he was also commonly called Bapu, an endearment roughly meaning "father".
    """

    summary_template= """

    Given the information {information}  about a person i want to you to create 
    1. A short summary 
    2, two interesting facts about them 

    """


    summary_promot_temmplate = PromptTemplate(
        input_variable=["information"], template=summary_template
    )


    # llm = ChatOpenAI(temperature=0, model="gpt=5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    
    
    chain = summary_promot_temmplate | llm
    response = chain.invoke(input={"information": information})
    
    print(response.content)
    



if __name__ == "__main__":
    main()
