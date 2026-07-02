# GetOutline + Project Briefs + Documenting AI Skills

## Attendees

- Tonda Kmoch <tonda@oakslab.com>
- Daniela Heczkova <daniela.heczkova@oakslab.com>
- Anastasiia Rudenko <anastasiia.rudenko@oakslab.com>
- Andy Powell <andy@oakslab.com>
- Manuel Monteiro <manuel@oakslab.com>
- Jakub Šlambora <jakub@oakslab.com>
- Michal Strapaty <michal.strapaty@oakslab.com>
- Denisa Lorencova <denisa@oakslab.com>
- Vilem Hujnak <vilem@oakslab.com>
- Kryštof Šraier <krystof@oakslab.com>
- Tamas Hajdu <tamas@oakslab.com>
- Matej Novak <matej@oakslab.com>

## Summary

Meeting records [Transcript](https://www.google.com/url?q=https://docs.google.com/document/d/1TGbsZ8CnD1xrD1XkGoDU1QB_MRc7hLMzkE6kJ-pjtkk/edit?usp%3Ddrive_web%26tab%3Dt.helv9kjsensk&sa=D&source=editors&ust=1776857163551513&usg=AOvVaw1TsRmsB6DzmZd97TMHb__k) (Some recordings unavailable)

### Summary

Meeting focused on adopting Outline for documentation to improve AI context sharing and standardize project processes.

Transitioning to Outline platform

Adopting Outline facilitates better AI context usage compared to Confluence or raw Git files. The team finalized the decision to use Outline as the primary documentation tool.

Standardizing project documentation

Projects must include a standardized brief and a central index of skills. This approach ensures high visibility for project goals and reusable technical assets.

Skill library implementation strategy

Skills remain stored in project repositories to maintain integrity while Outline serves as the searchable index. Documentation for project briefs and parent README files is due May 6.

### Next steps

-   \[The group\] Create Collection: Ensure a Get Outline collection exists for npm, Learning Spring, and Intake projects.
-   \[The group\] Download Skills: Download the skill zip file located in the AI skills library for use in steps 2 and 3.
-   \[The group\] Finalize Briefs: Finish Project Brief generation/creation for all 4 required projects. Aim to complete the task by May 6.
-   \[Tonda Kmoch\] Review Intake Brief: Manually go through the Intake project brief to ensure accuracy and fix all spotted mistakes.
-   \[The group\] Implement Product Syncs: Start using Outline functionality for product sync reporting. Implement this this week for Learning Spring and Intake projects.
-   \[The group\] Review Parent Readme: Review and complete the parent readme MD file documentation (signpost) for all cloud configuration and skills. Complete the task by the end of this sprint.
-   \[The group\] Document Skills: Complete individual skill readme MD files for every skill/command. Finish documentation within 1 month from now.
-   \[Tonda Kmoch\] Create Tickets: Create and assign Linear tickets for all discussed activities.

### Details

-   Introduction to the Outline Tool and AI Context: The meeting was initiated to provide context and instruction regarding a new activity involving the 'get outline' tool, which is closely connected to AI activities. The shift away from Confluence was triggered by the need to provide AI with sufficient context to perform well, as AI requires a great context to produce amazing outputs ([00:00:00](#h.vbxxh0v45m57)). Originally, exploring the use of only MD files within Git presented challenges, especially when collaborating with clients, as working with Git is not smooth for non-technical people and MD files lack features like online collaboration or history ([00:01:20](#h.2ybqwvdog271)).
-   Exploring Outline as a Documentation Solution: The challenges with MD files led to exploring other options, which coincided with the need to adjust the "Oakslab way," which was designed for humans before the AI era, to be consumable by AI as well. Utilizing a platform like Confluence results in a huge token overhead, whereas a tool using MD files, like Outline, is more straightforward and effective for AI consumption. Outline natively works with MD files, effectively utilizes tokens without XML parsing overhead, offers live collaboration, and provides easily presentable outputs, leading to the decision to deepen its usage moving forward ([00:02:44](#h.l6l680b1pl8o)).
-   Connecting Project Assets and Documentation Goals: Projects typically use Outline for documentation, Linear or Jira for tasks, and a Git repository for code and skills ([00:05:27](#h.n7mvsjfo2n9g)). A few essential pieces of information need to be standardized and shared across all projects, which involves two main activities ([00:06:42](#h.jefwoje0aom1)). The first activity is to have a project brief on all projects to describe key information like the goal and timeline, which is essential for the team, the digital management team, and for providing context to the AI. The second activity is documenting and sharing the great skills, commands, and configurations developed on projects to determine which are reusable across the company and can be moved to the "Oakslab way" ([00:08:06](#h.w2mhk89pomi2)).
-   Process for Documenting and Sharing AI Skills: A skill was created to help document existing project skills and push this information into the Outline structure, creating a single place for all skill documentation. The goal is to review these documented skills and choose what should be promoted to an "AI Skills Library," which will serve as a starting point for future projects to prevent them from creating essential skills from scratch ([00:09:50](#h.r1x5kbkks05f)) ([00:12:40](#h.no8orfnvwp8o)). Tonda Kmoch has created initial skills for generating the project brief and creating documentation, which will be used in this activity ([00:11:15](#h.aewidsfqsxfe)). The desired output is to have documentation for every skill, including a README MD file describing what the skill does, alongside the skill itself ([00:13:59](#h.37mnxd7dfy7c)).
-   Project Assignments and Deadlines for Project Briefs: Participants are asked to ensure that a 'get outline' collection exists for their projects (npm, learning spring, and intake) and to download a provided zip file containing two skills: one for generating the project brief and one for creating documentation ([00:15:29](#h.qj87aead5je3)). The recommended method for creating the first version of the project brief involves using an existing A4 page from Confluence, transforming it into a markdown file, and then using the "generate project brief" skill, providing the markdown file as a source for links and asking the AI to generate the brief based on the project structure ([00:16:50](#h.cje7xdqkcqct)). All project briefs for the four discussed projects are requested to be finished and put into Outline by the end of the current sprint, which is May 6 ([00:18:11](#h.q8dtupo5alll)).
-   Assignment and Timeline for Skill Documentation: The most complex piece of work is documenting the existing skills on the projects using the provided skill for documentation generation and Outline upload ([00:19:53](#h.3t8ajsdjgvj8)). Two levels of documentation are required: the first is a single parent README MD file for the whole cloud configuration and all skills/commands, serving as a signpost for using AI on the project, which needs to be reviewed and completed by the end of the current sprint. The second level involves generating a README MD file for every individual skill, and these individual skill documentations should be completed within one month from the meeting date ([00:21:06](#h.qj1qzm88wrp1)).
-   Clarification on Storage and Source of Truth: When questioned about storing skills in a repository, Tonda Kmoch clarified that the skill regenerates the README MD files, which remain in the repo, and the skill also puts them into Outline for visual representation and discoverability. The source of truth for the skills themselves must remain in the project's repository, as Outline can misformat the skill content when visualizing it. Outline serves as the index or signpost, but if someone wants to use a skill, they must take it manually from the respective project's repository and may need to speak with the skill creator ([00:23:36](#h.i831g5yaubco)) ([00:26:09](#h.f3mu1wyem7hh)).
-   Handling Skills Stored in the Cloud and Prioritizing Documentation: A concern was raised about skills stored in the cloud (like those shared via Clowd), which offer more flexibility for editing and refinement, rather than just being in a local repository ([00:24:58](#h.ddtipg1wwa1j)). The expectation is that the Outline must contain an index of all skills, regardless of where they are physically stored (like in the cloud or a repo) to ensure their discoverability, and the skill for documentation may need adjustment to accommodate this ([00:27:08](#h.72d5gj5pz9a)). It was noted that the parent README file, which describes the overall working process and tools like "superpowers," is considered the most valuable documentation, even more so than the documentation for granular skills ([00:28:23](#h.1gs774b5e195)).

---

## Transcript

**00:00:00**

- Tonda Kmoch: screen and let's jump to that. Do you see my screen?
- Kryštof Šraier: Yes.
- Tonda Kmoch: Awesome.
- Matej Novak: Yes.
- Tonda Kmoch: So, so the guys the the reason why I wanted to meet with you is that uh we
- Kryštof Šraier: Yes.
- Tonda Kmoch: have asked on you where we need your help and I shared the slack message but I understand that it's probably like challenging to understand that just from that like slack message. So I wanted to give you more context to like what we are trying to achieve and uh instruct you how exactly uh we need the help from you. So in the beginning I would like to give you a little bit more context about this
- Anastasiia Rudenko: Cool.
- Tonda Kmoch: get outline activity because we were always on the AISG. We were more discussing obviously the AI activities and not so much about the outline but it's like extremely connected. So yeah I wanted to give you some some context. So obviously all of us know that the AI is producing amazing
- Anastasiia Rudenko: Oops.
- Tonda Kmoch: outputs only when the AI has a great context and the AI really like understand the project and like understand the situation and so on.

**00:01:20**

- Tonda Kmoch: So, so the first need like when it comes uh why we started to decide where to potentially move from from Confluence was like uh triggered by by that need to actually for the AI get the context so the AI can do a great job. And originally in the beginning if you if you remember we were like exploring the option to actually not even have any confluence and have just the MD files as a part of the gate. But when we were using this on the on the projects, we experienced a lot of challenges. Uh for example, that like people always needed to have some like we were and that would be potentially fine for our team because we would just like train them like how to do that. But a lot of challenges were coming whenever we started collaborating with with the clients because sharing with them the MD files or like exporting the MD files and then somehow incorporating that feedback and so on was really like nightmare and also like working with git is not like the the most like smooth uh activity for nontechnical uh nontechnical people and plus like MD files are just MD files they are like lacking a lot of like good features like uh online collabor uh collaborative mode or like seeing like history or like seeing comments and and stuff like that.

**00:02:44**

- Tonda Kmoch: So that was actually the trigger when we started exploring like what are the options and what we can do about that. And one additional piece in in in that puzzle was that uh we have the Oakslab way. What was originally built before the AI era and it was built mainly for humans like mainly like for us. But now with like AI uh we believe that we will get like much better results if the au if the oaks love way will be like
- Kryštof Šraier: I don't
- Tonda Kmoch: adjusted in a way that it can be consumed not only by humans but also by
- Kryštof Šraier: think
- Tonda Kmoch: uh by AI. what means that having that like in confluence where there is like huge token like over overhead and so on might be like challenging and having that in something like let's say MD files will be like much more like straightforward for the AI. So, so with like all these like let's say activities we came to start exploring the get outline tool uh where the huge benefit of the outline is that it natively works uh with the content as the MD files what means that it's not uh it's very effectively utilizing the tokens because there is like no overhead with like parsing some like XML files and so on.

**00:04:13**

- Tonda Kmoch: It has like the live collaboration and it's very easily the outputs are presentable to to the stakeholders. It has also the MCP and so on. And uh yeah, we we learned with with with Kuba and that's that's also how we are like using that currently on on learning spring is that we even don't need to have the MD files locally in as a part of the repo.
- Kryštof Šraier: Amazing.
- Tonda Kmoch: we can have just like everything directly in the in the outline where we have like the history where we see all the changes and so on. So that's that's the moment when we started exploring the uh using uh using the outline and uh based on all the feedback so far we believe that it's very likely the tool we will like use like moving forward and because of that we would like to deepen the the usage right now. So if there are any like obstacles or like concerns we can like address them now and not like in the moment when we will transform the whole company. So that's a little bit context to the to the outline and like working with with AI and together with uh with outline.

**00:05:27**

- Tonda Kmoch: Uh here it's just like from from the outline documentation that I will share with you the the links just in fact the same what what I was saying like before that before we were like having the oaks club way in a way that we are consuming the uh the content there. Now we need to adjust that in a way that in future our oaks lab way will be something that will be consumable through people but also through the AI tools and that's the topic that I will be discussing with you today. So I put together this like crazy diagram and I will walk you through that like in in directly in mirror to explain you what exactly we are trying to achieve like today or like what what what's the activity like about so
- Kryštof Šraier: Oops.
- Tonda Kmoch: here in this box I have an example of of a project and project uh will be moving forward using the outline for for like some of the documentation Then the the project is obviously using like linear or like Jira for for like the user stories and like for bugs and like the development tasks and so on.

**00:06:42**

- Tonda Kmoch: And the project also has the like the git repo with like code and like skills and so on. And uh obviously like every project is like different. So maybe some projects will have more stuff here in like repo. Some other other projects will have maybe more like in the outline and so on and that definitely for now we are leaving on on projects to decide like where is what but there will be let's say few essential information where we need to let's say share it uh share it across projects uh and and that's like the place where we need to like uh like agree on and that's actually like two activities. So one is that we would like on all the projects have a project brief that is describing the key information about about the project because this information is essential not only to the team itself but it's also very helpful for for us as a like digital management team or like any like team member in in in Oaklab. because yeah obviously like when you want to learn about some project this would be your like starting point.

**00:08:06**

- Tonda Kmoch: So our like my or my first like ask that we will like discuss in a second like more in detail is that we need to start putting together for all our projects the project brief because if we will have the good description of like why we are doing that project, what is the goal, what is the timeline and so on. then it will be easier also for the team because uh the AI will have the context and it will be also easier for us as like digital management team because we will not need every one of us have like let's say own version of uh of the description of the project. So that's activity activity number one. And activity number two is that uh over the last months we put together like great uh skills and like commands and like great configuration of uh on on the projects. uh but it's kind of let's say invisible or like there is very hard way of actually like learning what we have where and how exactly we are like
- Andy Powell: There's
- Tonda Kmoch: utilizing that and that's uh what Andy was mentioning on the previous AI steering group that we would like to document uh this and find a way how to share it like let's say across the company so we will be able to start choosing what of those skills or commands or agents or like approaches are reusable like across the whole company and then start actually like moving that to the oak slab way.

**00:09:50**

- Tonda Kmoch: So the idea here is that uh I created a skill that will like help you to document like what you have like so far and that will push this information to the outline structure. So we will have on one place all the documentation of all the skills and then in future we will like introduce some process where we will like go through these like skills and like
- Kryštof Šraier: Okay.
- Tonda Kmoch: features and like tools and scripts and like everything that we have on the projects and we will from that choose what should go either to the Oaklab way more like from the sense of like let's say documentation or like uh let's say the content or what should go to something that I don't know we will maybe call like I don't know some like AI skills library what will be the let's say starting point for all the future projects so there will not they will not start with like creating all the skills from scratch but they will start uh with like create that they will get some like let's say essential ski uh skills uh in in the beginning as a part of the oaks lab way So in other words from all the projects we need the documentation of what they have and then we will start like we will like together with you like understand like what is like overlapping and what makes sense to

**00:11:15**

- Anastasiia Rudenko: What's
- Tonda Kmoch: maintain from like one place or maybe where we just want to like get uh the inspiration and so on. So as everything will be here on one place, it will be much easier to actually choose what to start uh using on on the projects
- Andy Powell: What?
- Tonda Kmoch: and then it will get uh it will get promoted to this let's say AI skill library that we will be then able to take to the to the uh to the projects and uh I created in fact the first like two or three scales that potentially will be part of this like uh AI skills library that you will like now use as a part of this uh this activity and one skill is uh the skill for generating that project brief and second skill is actually for uh create helping to create the documentation and put the documentation to the outline. Everything clear so far or or any questions? Okay. So, uh maybe to show you because yeah, I understand that now it's maybe like let's say hard to understand what that exactly means.

**00:12:40**

- Tonda Kmoch: So, I will show you the the output in a second. So uh let's say alternative diagram of this what I was just like explaining is is here that there will be in future some uh skills library in oaks lab that will from where the projects will be able to take take the data or like take take the take the example.
- Andy Powell: Okay.
- Tonda Kmoch: So this like top part we don't have yet because we need to do first this
- Anastasiia Rudenko: Oops.
- Tonda Kmoch: like second part is that we need to take all those skills and like commands and uh what you created on the projects and we need to put them on one place with some like essential documentation. So then we can choose what of these things in that let's say shared library of everything will get promoted to or like will get to the to this like let's say common part that we will say yes on every project we need to generate a product sync for example and it makes sense to have that product sync as a starting point as as like one scale so we don't uh let's say uh recreate that on every project from scratch and then it will get here and from here the projects will be able to uh to take

**00:13:59**

- Kryštof Šraier: Oat.
- Tonda Kmoch: it. So how looks the output uh like for for now for now I put here as example uh the for example the the open loop so what what's the what's the goal is to have the documentation of all the skills and of for like every skill the documentation what the skill is doing together with the skill itself. So how that uh skill that that helps to create this works is that it AI generates the readme MD file for like every skill that's here on the on the top of the page and then here on the bottom is the skill like itself. So this like bottom part was prepared by probably Denisa and Kate. This top part is for now just AI generated and uh we will need to obviously uh validate or like uh check it manually if it's uh if it's correct. So the goal in future is that here in the AI skills library we will have all the projects and some of them will get promoted to some like let's say common part that will be actually somewhere in some like repo from where we will be taking the uh the data.

**00:15:29**

- Tonda Kmoch: So now in last 12 minutes let's jump on what exactly I need from you.
- Anastasiia Rudenko: Awesome.
- Tonda Kmoch: So first step is that for the projects that we are discussing npm learning spring and intake I would like to ask you to make sure that uh that there is a get outline collection for your project and uh please download the scale for like what will help you to do the step two and step three. So it's in that SL like message that I was sharing or it's in the AI skills library like itself here that in this like skills zip that will actually help you with with step two and uh step three and that that will give you two skills. First one is generating the project brief. So the skill itself that you will get uh from that zip file is described uh described here. So uh also with the way like how to use it.
- Kryštof Šraier: Please
- Tonda Kmoch: So you need to uh what I I found that is the easiest way to actually like create the first version of the project brief is that you take the

**00:16:50**

- Kryštof Šraier: keep
- Tonda Kmoch: existing A4 page that we created earlier manually in uh in Confluence because here are all the valid like links and like everything what of course AI cannot like guess. So what worked for me is to download that as a
- Anastasiia Rudenko: Okay.
- Tonda Kmoch: document, save it as a like mark uh use Google documents to transform that to the markdown file and just like save it like somewhere in in your repo as a let's say initial version with with the links and then you take that that skill that I created this like generate project brief where you will ask hey generate me the project brief for this project going through all the MD files that you see in the project structure and blah blah blah and for links take the links from from that export that is coming from that like A4 where where are those uh those links and when you if you do
- Kryštof Šraier: We
- Tonda Kmoch: this what you will get is that it will generate
- Kryštof Šraier: hope.
- Tonda Kmoch: the uh the project brief and I believe that it will also put it to the to uh outline and uh yeah.

**00:18:11**

- Tonda Kmoch: So this is the structure of uh of that document and uh obviously please like adjust that to your like project specifics and so on. And now for example on like intake it's a task on me to actually go through that like manually and like make sure that everything is like accurate and like correct and like fix it because obviously the if the AI didn't have like any like correct context then it's uh not like super like precise. So I already spotted like few uh few mistakes here. So that's uh that's activity number number one and I would like to ask you if we can aim to finish this project brief for all these uh four projects by end of this sprint what is on May 6. So we will have it in outline already and we will be able to start using that not only on the projects but also for us uh as a digital management team. Also small heads up uh we will also very soon start using the uh the outline for the product things because AI can help us a lot in putting uh all the things like together and probably we can again like create in future some scale that will like take data from linear and so on and like create the uh uh the product uh report for This week we agreed with learning spring and intake that we will uh we will do it even this

**00:19:53**

- Tonda Kmoch: this week and very likely in two weeks we will ask also you on the other projects uh to to do the same if if it will work well for the Linux and intake. And last piece and probably the or definitely the the most like
- Andy Powell: Cool.
- Tonda Kmoch: complex is that we would like to document the existing skills that you have on the project. So again in that zip file that you will download you will get the skill for generating that documentation for the
- Kryštof Šraier: on the
- Tonda Kmoch: uploading that to uh to outline.
- Kryštof Šraier: door.
- Andy Powell: Yeah.
- Tonda Kmoch: So if you will just run this scale it will do like everything for you but obviously it it doesn't know that that context. So uh what will be the result is that it will everything like here but you will need to review that and make sure that it's like let's say accurate and like correct and we would like to do two uh let's say two levels of documentation. So one is the readme MD file that will be generated

**00:21:06**

- Anastasiia Rudenko: Okay.
- Tonda Kmoch: automatically for the whole project for that like cloud configuration and all your like skills and commands. So like let's say that like signpost of like let's say everything that you have uh that you have in your repo and that should be definitely the most like important thing because that should be the starting point for like anyone when it comes to using the AI on your projects. So for this first readme MD file what is just like one file I would like to ask you to uh review that readme MD file and like
- Kryštof Šraier: Please.
- Tonda Kmoch: complete that by end of this sprint and then second thing what that uh skill is doing is that it takes every skill or every command that you have in in uh in your like cloud configuration on the project and it generates the readme MD D file for uh for like that every scale and for these readme MD files uh what will be like as many as many skills you have I would like to ask you to complete that in fact within one month from from now.

**00:22:25**

- Tonda Kmoch: So we will have the documentation for uh for every scale and we will be able to actually start like comparing like how those skills like differs and
- Kryštof Šraier: Just Thank
- Tonda Kmoch: what's to potentially take to that like common part that we will use on all the
- Anastasiia Rudenko: That's
- Kryštof Šraier: you.
- Anastasiia Rudenko: perfect.
- Tonda Kmoch: projects and yeah that's that's everything from from my side. So uh just like in in the summary downloading that zip file because uh for now we don't have that like approach uh this let's say top part. So you need to download that like manually put it to your repo and use two those two skills that will help you to create first version of the project brief and first version of the
- Anastasiia Rudenko: Peace.
- Tonda Kmoch: documentation of your skills. But majority of the work will be obviously going to those uh project brief MD file and the readme MD files of of of the scales and manually like reviewing
- Andy Powell: s\*\*\*.
- Tonda Kmoch: that and like making sure that it uh contains all the essential information.

**00:23:36**

- Tonda Kmoch: Any questions, comments, thoughts, concerns? Yes, Danny.
- Daniela Heczkova: So does it make sense to actually like store the skills in a repo?
- Kryštof Šraier: question.
- Daniela Heczkova: Because right now like um so we shared the
- Anastasiia Rudenko: Okay.
- Tonda Kmoch: Yeah. So yeah, sorry. Sorry if I if I explained that like wrong.
- Daniela Heczkova: skill
- Tonda Kmoch: So everything is in the repo. So what that skill is doing is it just regenerates the readme MD files but they are in the repo. So everything is in the repo. What is it doing on the top on top of that?
- Anastasiia Rudenko: Oh.
- Andy Powell: That's crazy.
- Tonda Kmoch: it that it also puts to outline because then it would be so hard to actually like let's say start pulling uh seven 10 projects on like one place that one place where is just that like visual representation or like that visual part of the readme MD files will will be in the outline but if someone will decide that hey I actually saw that on learning spring they have a great skill I want to use it no one can take it actually from the outline because outline uh let's say misformat uh the stuff when when it gets like to this like visual representation in that moment you will need to go to the repo of uh of learning spring and get that skill

**00:24:58**

- Anastasiia Rudenko: That's what I
- Tonda Kmoch: manually
- Daniela Heczkova: because uh so we have a skill that I created it's in clot you can share it from
- Anastasiia Rudenko: meant.
- Daniela Heczkova: clot so that like that means that you can either share it with your team you can share it with oaks live like with the whole company that means that it gives you more flexibility when you need to edit and keep editing and kind of like um refining that skill. So it like is live. It's not like some kind of like screenshot of that skill, but you can kind of work with it and also at the same time share it with
- Tonda Kmoch: Yeah. Exactly. Yes. Yes.
- Daniela Heczkova: everyone.
- Tonda Kmoch: So how what what will happen is that once you will do that here will appear like learning spring here one of those skills will be those like skill that you are like let's say proud of or like that we are like now like discussing here will be that like let's say documentation and if anyone will be interested in like hey actually this is a great skill I want to have it as well he will not take it from here because you see that for example this like let's this this formatting is broken because it's that YAML part of the of the top of the scale and unfortunately saving that here it breaks that.

**00:26:09**

- Tonda Kmoch: So if anyone wants to use it,
- Anastasiia Rudenko: Easy.
- Tonda Kmoch: we'll know okay I need to speak with Danny. It's from like learning spring. I want to get this skill and we'll get that skill like let's say directly from the treo. So this is really like just the signpost. It's just that like let's say index but the source of truth is always in the in those readme MD files.
- Denisa Lorencova: updates that skill in the repo.
- Kryštof Šraier: Wind.
- Denisa Lorencova: That means that it will also be like updated here automatically. Say you don't have
- Daniela Heczkova: skill in repo anymore because we decided to just have an incl. involved. What is what does it
- Jakub Šlambora: It's like shared assert cloud skill the team shared skill on cloud
- Kryštof Šraier: So like you
- Daniela Heczkova: mean? Okay.
- Jakub Šlambora: level.
- Daniela Heczkova: Which makes it easier because like right now we have been refining the skill for a while like for a month and there has been a you know many different versions and you kind of like get lost in it.

**00:27:08**

- Daniela Heczkova: Uh and I think like this is yeah I think like this kind of works in our team right now.
- Tonda Kmoch: Yeah. So I think that Kuba you will like find out right how to do that. So the goal or the ask is that in outline needs to be the index of all the skills. If you have it on your USB drive or like co-work or like wherever it's not important what is important is that it needs to get here because otherwise it would not have like any like discoverability. We would not be aware that such a good asset like exist. So you will probably just need to adjust that scale to actually like upload it here because it's probably taking from like some other other place. But I guess that in the end it's anyways Arimme file on the local uh on on the hard drive. So probably it will work out of the box. Yes.
- Jakub Šlambora: One more question t do you have any preference on because currently let's say
- Tonda Kmoch: Kuba
- Jakub Šlambora: with with our setup on learning spring uh we are like majority of skills we are using for engineering comes from plugins specifically superpowers would it be do you have any preference how this should be present presented on the signpost.

**00:28:23**

- Jakub Šlambora: Like if
- Tonda Kmoch: Yeah, please if you can and yeah that this is great question.
- Jakub Šlambora: if
- Tonda Kmoch: So that's why I believe that the most valuable documentation are not those like granular like skills. Maybe there is not much to like document or like explain because maybe the skill itself is like let's say clear like enough like what is it doing and so on but what is the most important is this like that parent readme that that that is like describing like everything. So for example here in in uh open loop it's it's this like readme md file. So I think that here in the readme you should really like spend the time like explaining how you are working with that like why or like that that's we are using superpowers and so on guys
- Jakub Šlambora: Makes sense. Thank you.
- Tonda Kmoch: I very recommend uh like using like for example whisper flow like something that that like just record the the voice. So yeah, how I work with like this like stuff is that I create a new MD file. I just like hit the recording and I just like speak like how we do that, why blah blah blah and very like in a totally unstructured and like let's say howic mode and then I just like ask the AI like hey here is the like thoughts create from that like structure document.
- Anastasiia Rudenko: Okay, thank you
- Tonda Kmoch: Any other
- Anastasiia Rudenko: for
- Tonda Kmoch: questions or any concerns or anything? If not, I will create the linear tickets for like these uh activities that that we discussed and like assign it on you. So we will have it somewhere like documented and yeah I will if you will have any questions or anything just let me know and Thank you a
- Daniela Heczkova: Thanks.
- Tonda Kmoch: lot.
- Matej Novak: Thank you.
- Anastasiia Rudenko: Thank you.
- Tonda Kmoch: Thank you.
- Jakub Šlambora: Thanks.
- Tonda Kmoch: Have a great day.
- Matej Novak: Thank you.
- Tonda Kmoch: See you.
- Jakub Šlambora: Thank you guys.
- Vilem Hujnak: Bye-bye.
- This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

---

## Metadata

- **Date**: 2026-04-22
- **Source**: Gemini | [Open in Google Docs](https://docs.google.com/document/d/1TGbsZ8CnD1xrD1XkGoDU1QB_MRc7hLMzkE6kJ-pjtkk)
- **meeting_id**: 1TGbsZ8CnD1xrD1XkGoDU1QB_MRc7hLMzkE6kJ-pjtkk
- **owner**: Tonda Kmoch <tonda@oakslab.com>
- **gemini_doc_id**: 1TGbsZ8CnD1xrD1XkGoDU1QB_MRc7hLMzkE6kJ-pjtkk
- **meeting_time**: 10:29
- **meeting_timezone**: CEST
