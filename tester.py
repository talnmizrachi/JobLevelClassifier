# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import json
import os
from dotenv import load_dotenv
load_dotenv()


def create_user_content(job_title, job_summary):
	return json.dumps({
		"job_title": job_title,
		"job_summary": job_summary
	})


def get_response(title_, summary_):
	"""
	With is_analyst
	:param title_:
	:param summary_:
	:return:
	"""
	client = OpenAI(
		api_key=os.environ['API_KEY'],  # this is also the default, it can be omitted
	)

	response = client.chat.completions.create(
		model="gpt-3.5-turbo-1106",
		response_format={"type": "json_object"},
		messages=[
			{
				"role": "system",
				      "content": "You are a helpful assistant designed to output JSON, you will receive a JSON object that looks like this:\n{\n\"job_title\": a title (string),\n\"job_summary\": the description of the job (string)\n}\n\nYour output JSON should look like this:\n{\n\"is_entry\": boolean,\n\"is_analyst\": boolean,\n\"specifics\": string,\n\"level\": float\"\n}\n\n\"is_entry\" represents if this job is entry-level.\n\"is_analyst\" represents if this job is an analyst position\n\"specifics\" represent the title name of any past role that the candidate must have that is not an analyst (examples - stock trader, dentist, marketing manager); this can be None.\n\"level\" - how sure are you with the decision that this is an entry-level position"
			},
			{
				"role": "user",
				"content": create_user_content(title_, summary_)
			},
			{
				"role": "assistant",
				"content": "{\"is_entry\": bool, \"is_analyst\": bool, \"specifics\": string, \"level\": float}"

	}
		],
		temperature=0.5,
		max_tokens=256,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)
	return response


if __name__ == '__main__':

	title = "data scientist"
	summary = "data scientist (entry level), us/canada residents only, full-time, salary $60k-$70k\nminimum 1 year of work experience - fully remote position. freshers are also encouraged to apply.\nabout us:\n the future of ai is patterned we are a stealth-mode technology startup that is revolutionizing the way ai is used. our platform uses pattern recognition to train ai models that are more accurate, efficient, and robust than ever before.\nwe are backed by top investors and we are hiring for almost everything! if you are passionate about ai and want to be a part of something big, then we want to hear from you.\nmake a positive impact on the world. be a part of a fast-growing startup. if you are interested in learning more, please visit our website.\nwe are looking for people who are\npassionate about ai.\nexcellent problem solvers.\nteam players.\ndriven to succeed.\nrequirements\nresponsibilities:\npartner with engineers, product managers, and business partners to identify algorithmic problems, brainstorm possible approaches, and recommend the best path forward.\ndevelop algorithms iteratively, building in the right level of complexity to solve the business problem at hand and support future improvements.\ndefine success criteria for your models so that you can measure impact and changes over time. you'll be expected to communicate findings and drive continuous improvements.\ncollaborate with software engineers to implement algorithms in production that scale gracefully.\ncollaborate with stakeholders to prioritize projects and define requirements.\ncarry out analysis of data produced by our hardware systems and create insightful visualizations to share your findings.\ncontribute to internal libraries to help other teams with their data science needs including visualization, prediction, optimization, and inference.\nrequirements & experience\nadvanced proficiency with python and libraries commonly used for data analysis, e.g., pandas, numpy, scipy, and matplotlib.\nstrong understanding of data modeling and statistical analysis.\nknowledge of optimization and predictive modeling techniques and experience applying them to real-world problems.\nskilled at translating a general question or problem into a clearly defined algorithmic solution.\nability to communicate clearly with both technical and non-technical audiences.\nability to work independently and manage multiple projects simultaneously.\nnice to haves\n1-year experience with data bricks or pyspark\n1 year experience with product ionizing data models\nexperienced in sql scripts and python programming language.\nbenefits\nspecial benefits you will love:\nflexible vacation, unlimited paid holidays, and paid sick days\n401(k) with up to 2% employer match\nhealth, vision, and dental insurance\nwhy patterned learning ai?\npatterned learning ai is made up of incredibly bright, mission-driven coworkers who are passionate about using technology to solve real-world problems---and we're growing quickly. in order to continue building an engaging and dynamic organization, we're committed to giving everyone the support they need to do great work.\nwe believe diverse perspectives and backgrounds are critical to building great technology, and our goal is to cultivate an environment where people feel equally valued and respected. patterned learning ai is proud to be an equal opportunity workplace, and we welcome applicants from all backgrounds regardless of race, color, ancestry, religion, gender identity or expression, sexual orientation, marital status, age, citizenship, socioeconomic status, disability, or veteran status.\n      \n\n\n\n        show more\n\n        \n\n\n\n\n\n        show less"

	resp = get_response(title, summary)


	print(resp)