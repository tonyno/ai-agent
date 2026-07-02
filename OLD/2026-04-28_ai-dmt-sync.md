# AI DMT Sync

## Attendees

- Tonda Kmoch <tonda@oakslab.com>
- Matej Novak <matej@oakslab.com>
- Andy Powell <andy@oakslab.com>
- Jan Barta <jan.barta@oakslab.com>
- Denisa Lorencova <denisa@oakslab.com>
- Kryštof Šraier <krystof@oakslab.com>

## Summary

Meeting records [Transcript](https://www.google.com/url?q=https://docs.google.com/document/d/1aQ5iAM9wy5VsZQ8JJHGY3wjSwIKGymSoE0W-FzG5ifs/edit?usp%3Ddrive_web%26tab%3Dt.djj9gdnbabwc&sa=D&source=editors&ust=1777457247236353&usg=AOvVaw1kw3CpTGqWVMgDjDI2wbEs) 

### Summary

Meeting focused on migrating content to Outline and optimizing centralized AI-driven project documentation with resource planning.

Outline Migration and Strategy

Migration to the Outline platform is confirmed for content storage on Google Cloud Platform. Stakeholders must be alerted that comments will be lost during this transition.

Centralizing Product Sync Documentation

Product sync tasks and transcripts will move to Outline to centralize information. Product leads should establish independent project structures to foster individual ownership.

AI Integration and Resourcing

The team will build a centralized AI knowledge base for project scripts and presentations. Management is prioritizing the hiring of 3 new technical leads.

### Next steps

-   \[Matej Novak\] Schedule Migration: Organize a detailed discussion call to plan the Outline and Confluence content migration details.
-   \[Tonda Kmoch\] Check FigJam: Determine the current pricing structure for FigJam software.
-   \[Tonda Kmoch, Andy Powell\] Discuss Tool Strategy: Discuss the future collaboration tool strategy, choosing between Mirror, Excalidraw, or FigJam.
-   \[Tonda Kmoch\] Save Transcripts: Ensure all product sync meeting transcripts are consistently saved within the Outline folder.
-   \[Andy Powell\] Share Prompts: Provide the specific prompts used for processing action points derived from product sync meetings.
-   \[Tonda Kmoch\] Reschedule Syncs: Reschedule all product sync meetings in the calendar.
-   \[Tonda Kmoch\] Enable Transcription: Turn on transcription functionality for all rescheduled product sync meetings.
-   \[Tonda Kmoch, Matej Novak\] Deploy Sync Script: Discuss the deployment location and automated running schedule for the intake script, feeding product sync data into Outline.
-   \[Tonda Kmoch\] Move AISG Projects: Move the NPM and EP (AISG projects) to Outline for product syncs starting next week.
-   \[Tonda Kmoch\] Update Kuba: Meet with Kuba this week to provide necessary project updates regarding his involvement.
-   \[Matej Novak\] Create AI Repo: Create the central repository for AI functionalities knowledge base and define the strategy (e.g., branching, shared skills) for its usage across projects.
-   \[Tonda Kmoch\] Define AI Process: Define documentation standards and the necessary process for submitting content to the central AI repository.
-   \[Matej Novak\] Prepare Documentation: Work with Danny to compile product documentation for the Learning Spring project.
-   \[Matej Novak\] Monitor Claude Usage: Develop a strategy to monitor and understand individual Claude usage consumption data.
-   \[The group\] Review DMT Docs: Review the current DMT documents owned by Andy Powell to assess centralization feasibility and ensure perspective alignment.

### Details

-   Initial Outline Deployment and Content Migration: Hanza provided an update regarding the Outline platform, confirming it is online and open-source to the public under the team's control on GCP ([00:00:00](#h.u7x6c42ms2ti)). The primary discussion centered on migrating content from an existing zip file, which includes all collections and attachments, and the technical implementation on GCP, which uses Cloud Run and a Superbase Postgres database for content storage ([00:01:44](#h.c46lraqlkt5j)). A critical point raised by Andy Powell is that comments will be lost during the migration, suggesting that people should be informed before the change ([00:03:53](#h.y2o50ptmi2zn)).
-   Migration Planning and Coordination: The team agreed that the migration step requires careful planning and coordination, ensuring all teams are aware before proceeding ([00:02:37](#h.2pka2n5erwdf)). Tonda Kmoch suggested not rushing the process and executing the transition only after a final decision has been made, with a set date for everyone to move to the new instance ([00:04:55](#h.atnjvjomb0ov)). Andy Powell confirmed they will follow up on the recommended backup strategy, which involves daily server snapshots and database replication for additional backup ([00:03:53](#h.y2o50ptmi2zn)).
-   AISC Meeting Topics and Meeting Structure: Tonda Kmoch proposed using the upcoming AISG meeting to share the "clo design demo," provide reminders about recent agreements, and discuss the future of the current recurring meeting. They suggested keeping the regular meeting in the calendar as a placeholder, which will be periodically canceled but available when immediate coordination is needed ([00:05:48](#h.vyjkb326opds)).
-   Digital Management Team Task Management: Tonda Kmoch advised against making immediate changes to the digital management team's task management and suggested keeping tasks in Asana for the moment. They noted that this decision is temporary, as the team is a small subset at the end of the project chain, and it is more important to focus on shifting projects and product sync tasks toward Linear ([00:07:16](#h.eovtqyqhg7s)).
-   Exploration of Excal and FigJam: The team discussed the exploration of Excal, a front-end-only, mirror-like tool being used by an individual, mainly for product diagrams and quick sketches ([00:07:16](#h.eovtqyqhg7s)). The tool is being tested because an AI can generate the necessary JSON structure for the diagrams. Tonda Kmoch also plans to check the pricing for FigJam to potentially evaluate it as an alternative to Mirror ([00:08:37](#h.bscgtukorxqi)).
-   Centralizing Product Sync Tasks in Outline: Tonda Kmoch proposed moving tasks from product syncs into Outline documents, noting that the product leads were not actively using Asana for this purpose ([00:09:44](#h.a1y0cnf7dus)). This suggestion is part of a broader effort to centralize information and move away from the current scattered approach ([00:12:22](#h.nme5mekw537h)). Andy Powell, who currently manages this process, agreed to continue leading the synthesis of this content until a more scalable solution is decided upon ([00:11:14](#h.2kjpexmbg2kz)).
-   Automating Product Sync Transcripts and Action Points: Tonda Kmoch committed to taking responsibility for ensuring meeting transcripts automatically get stored in the appropriate Outline folder. Andy Powell will share the prompts used for processing action points to help prepare this process for Johan or a future manager ([00:13:28](#h.q92e4exwjm7f)). Matej Novak recommended that product leads should set up their own project structures in Outline to foster ownership and understanding of the process ([00:14:37](#h.b9heeheytzwl)).
-   Transitioning Projects to Outline: Tonda Kmoch confirmed the plan to reschedule all product sync meetings, turn on the transcription feature, and involve Honza in setting up a script that automatically runs to upload these transcripts to Outline ([00:16:59](#h.mpm2wiqhfsab)). Additionally, Tonda Kmoch will move all AISG projects—RCM, Learning Spring, Intake, NPM, and EP—to Outline for the product syncs starting next week ([00:18:54](#h.7m0rtt3gv84w)).
-   Kuba Involvement and Tech Lead Hiring: Tonda Kmoch plans to meet with Kuba this week to update them on project matters, acknowledging the challenge of their increasing workload. Andy Powell stated that the financial agreement for a replacement has been secured, and the next step is planning the specific replacement, likely during a squad roster discussion next week, with three tech leads already in the hiring roadmap ([00:19:57](#h.odjjz7xwe7ig)).
-   Developing a Centralized AI Functionality Knowledge Base: Tonda Kmoch stressed the necessity of creating a knowledge base or starting pack of AI functionalities for all projects, including scripts for presentations and meeting processing. Honza was tasked with not only creating the repository but also developing a strategy for how these skills will be managed, potentially through version control or as shared organizational plugins ([00:21:02](#h.bf2762xkymka)).
-   Standardizing AI Implementation and Communication Strategy: The team needs to organize a process for submitting content to the central knowledge base, defining standards for documentation and communication ([00:22:15](#h.fj4zpuyv5xji)). Andy Powell advised being strategic about the communication and rollout of new AI tools, prioritizing quick wins like the presentation skill that are easy for teams to install and feel helpful ([00:23:28](#h.ttus2yx731lu)).
-   Tracking and Managing AI Usage and Costs: The team discussed the difficulty in tracking the consumption of Claude, noting that currently, there is no reliable solution for monitoring individual usage. Jan Barta suggested using a third-party solution, such as a Sentry plugin, to gather this data ([00:28:48](#h.en51shi0ziw8)). Honza was tasked with developing a strategy to understand consumption patterns to ensure people are using the appropriate tier (e.g., standard vs. premium) ([00:30:05](#h.dxprhvwrlmpy)).
-   Ownership of the DMT Centralized View: Matej Novak confirmed ownership of the Digital Management Team (DMT) projects and status documents ([00:30:05](#h.dxprhvwrlmpy)). Andy Powell, whose role involves central synthesis, agreed to continue owning the process of synthesizing project status for DMT visibility. The team agreed that these are highly important pages, and everyone should review the content to determine if a centralized structure is realistic ([00:31:05](#h.aq0n5kkwxzs8)).
-   Business Model and Client Billing: Tonda Kmoch suggested continuing the current model of having one person double-billed to recover costs, given the perceived efficiency gains from AI. Andy Powell noted they are already building this to clients and this financial strategy helps mitigate pushback on the AI budget ([00:26:50](#h.5h6bx0oy5gxt)). The group agreed that the person who is double-billed should likely be an engineer or QA ([00:28:48](#h.en51shi0ziw8)).

---

## Transcript

**00:00:00**

- Kryštof Šraier: What is this
- Tonda Kmoch: Do we
- Kryštof Šraier: running?
- Tonda Kmoch: know she's
- Andy Powell: the design chapter. So, I guess she's like coming down from it.
- Tonda Kmoch: on
- Andy Powell: So, let's jump to that.
- Tonda Kmoch: So I would like to continue on the through the like the topics that I put together but we didn't manage to finish that on Friday and I injected few topics like yes as as like some like let's say updates and then let's use the meeting next time to actually like check the progress and uh I'm creating the liner tickets for like everything. So everything should be like in line art. Uh so maybe first if we can start Hanza you wanted to share some update about like what you managed to do so far this get outline. Yeah. So the you have the I
- Andy Powell: Basically we have
- Tonda Kmoch: start
- Andy Powell: uh
- Tonda Kmoch: I
- Matej Novak: online.
- Andy Powell: Oh,
- Matej Novak: So it's online. Uh it's the open source to public.
- Tonda Kmoch: uh posted version on

**00:01:44**

- Matej Novak: So it's all under our control.
- Tonda Kmoch: GCP.
- Matej Novak: So I think now now the biggest question is uh how do you want to migrate the content from where
- Andy Powell: that's
- Matej Novak: when uh I did an export. So basically from from the or from the existing zip I have like 600 megaby zip which should be just one to one
- Kryštof Šraier: I can just import and in theory. the
- Matej Novak: replication and then save of all
- Tonda Kmoch: collections.
- Matej Novak: the uh I haven't tried
- Tonda Kmoch: Yes, all the collections, all the attachments, everything because I think I I would have to manually delete it. I try so I didn't but I expect it will just create collections. Not sure about like history or edits or whatever. I think.
- Matej Novak: It will be marked. Yeah, everything should be there.
- Tonda Kmoch: So I can do it if if we if we say
- Andy Powell: The cleanest like a
- Kryštof Šraier: So we don't lose much and
- Tonda Kmoch: something.
- Andy Powell: quick
- Matej Novak: You can look like the I don't know if everything else should stay or there is any cleanup already

**00:02:37**

- Kryštof Šraier: then
- Matej Novak: needed or not, but I would maybe do it in the in the new
- Kryštof Šraier: so
- Tonda Kmoch: Before we actually do this step, we obviously will need to like plan it and like all the teams will need to be aware and so on. So that would probably like require some like coordination and before we do that, yeah, likely there will be like some some like questions that needs to be clarified. So for example, yeah that like whole like architecture like how is it like put together that includes I don't know backups and really like let's say everything that we will be we will be like using or you plan to add that like later. So, so it is on
- Matej Novak: uh on on GCP on the
- Tonda Kmoch: uh
- Andy Powell: Let me say so that's
- Matej Novak: manage uh storage for
- Kryštof Šraier: There is
- Tonda Kmoch: uh there is a cloud run
- Andy Powell: like
- Matej Novak: the files.
- Tonda Kmoch: functions
- Matej Novak: It's all managed for so it's all
- Tonda Kmoch: it
- Matej Novak: in storage
- Tonda Kmoch: and for content itself there is a super base postgress database like

**00:03:53**

- Matej Novak: other stuff. Um, yeah, I'm
- Tonda Kmoch: abusers
- Andy Powell: following up because we discussed this on my call with the guy from outline.
- Matej Novak: just
- Andy Powell: He suggested to just snapshot. He said what most people do is snapshot the entire server once a day and replicate the database as an additional backup. He said like that's what they recommend that all their clients do.
- Tonda Kmoch: like a server because it's done in there
- Andy Powell: Yeah.
- Tonda Kmoch: for
- Matej Novak: So I think the only thing we will care about are data which is the super page.
- Tonda Kmoch: uh and and the and uh everything else can be just spilled off. So I I can looking to get a bit more% sure that we don't lose
- Matej Novak: No. So this
- Tonda Kmoch: anything but other than that we don't need anything. One other topic to the mic.
- Andy Powell: ation.
- Matej Novak: flight
- Andy Powell: So obviously it takes over all of your pages and collections etc. And obviously it doesn't take over users but also what it's comments.
- Tonda Kmoch: doesn't take

**00:04:55**

- Andy Powell: So I it might just be worth telling people that before I make that change. So if anyone has like documents with lots of comments on them, we will lose those comments when we make that shift. Interesting. I
- Tonda Kmoch: Okay. Because it's not in the market,
- Andy Powell: know.
- Matej Novak: comments are like in my topic on top of that I guess.
- Tonda Kmoch: right?
- Andy Powell: Okay. Okay.
- Tonda Kmoch: So,
- Andy Powell: Awesome.
- Tonda Kmoch: yeah, Hanza, let's let's discuss it probably like more in detail.
- Matej Novak: Yeah.
- Tonda Kmoch: Also we need to plan to that that migration from confluence. Yeah. So so what would be next? Should I ask you to call you? Yeah. Yeah, that would be awesome. Okay. And to Yeah. I think that Yeah. We should not like let's say super like rush it because I think that we should do it in the moment when we will already make that decision and we will say okay we are really like moving.

**00:05:48**

- Tonda Kmoch: We know who is moving and so on because I want to prevent that. we will have like so many like PC so it's already amazing that a lot of people are using that we should make that decision and we'll say okay we validate that we know blah blah blah here is the date when we will do that transition and from that moment everyone is already on the new instance and like everything awesome so if we can move on the next topics about the AISG tomorrow so I would suggest to keep it to use it as the opportunity for uh sharing if you will have ready that uh clo design demo. Yes. And also like use it as as once more like a reminder for like all the activities that we agreed like lately and mainly like tell what is what is going to happen with this meeting and to be honest I would suggest that we will keep it in the calendar as a like placeholder. we will like call it placeholder and we will be periodically like cancelling that in fact like almost every time almost every time but on the other hand when we have something I want to avoid the situation that we will be for four days like searching for some date when when people will have time for for joining okay so then the and and yeah a lot of these topics we already like partially like discussed and maybe a lot of have like changed.

**00:07:16**

- Tonda Kmoch: So when it comes to the digital management team tasks, I would suggest that for now we will not do any change and we will just keep like for for now in Asana before we will actually yeah because we are almost like in the end of the chain right it's more like important where are the projects that's probably moving towards like linear where are the product syncs uh tasks and then like we we are almost the smallest like subset. So that's why I would suggest to postpone with with this for a second and let not do any changes. Uh also just for information for everyone to be like aware uh will started like exploring using Excal on on the project mainly Excal you don't know. I don't know. So excal it's interesting project. It's the uh this like kind of mirror but front end only. It doesn't have any storage anything. It's just like in the browser and it's for like quick like sketches. Uh-huh. The main reason why he is using this or like trying this is that uh no no

**00:08:37**

- Kryštof Šraier: This is actually
- Tonda Kmoch: it's not it's not at all for design it's more for product.
- Kryštof Šraier: Okay. Okay.
- Tonda Kmoch: So he's like
- Kryštof Šraier: Okay. Everyone
- Tonda Kmoch: trying that is that AI generate the JSON that is like the structure of this. So actually the AI is generating all the diagrams for him what mirror is kind of let's say tricky slash impossible. So just like sharing this that we are like exploring that but I also had the chat with with uh Andy like what's the plan or potential like future with like mirror so I will check what is the pricing of fig jam and we will like and maybe I will speak with you and we will like potentially like discuss if we are staying for now in mirror or like maybe that excal or maybe fig jam and so on. Uh yes. What? You can have a local instance of that as well. Yes. Yes. Yes. Exactly. Yes.
- Andy Powell: build a whole

**00:09:44**

- Tonda Kmoch: It's like super easy to like host it like Yes.
- Andy Powell: self-hosted
- Tonda Kmoch: The the disadvantage is that this is like super like like simple. So you cannot do like super like complex things in this. Uh yeah and also like it's
- Kryštof Šraier: uh it doesn't it's not it doesn't have any resistance layer right that's what you can build
- Tonda Kmoch: yourself. So they are so they have this excal plus what is a paid version and that's they are giving the back end for you or this is open source you can like run it locally and there are already hundreds of projects online that people are building different back ends. For example, the storage can be Google documents. So you can save those diagrams to Google documents for example. Like you just need to save those.
- Kryštof Šraier: Jason's right. Exactly. Exactly.
- Tonda Kmoch: Awesome. Let's move on. So one thing that I would and and and in fact like before I managed to propose that he already started doing that I would suggest that we might try having the tasks from the product syncs in outline because yeah of course it's disadvantage is that it's like document but on the other hand with like AI and like everything it can be like easier to use than than like in Asana, what are the leaders anyways not using at We were I I'd moved

**00:11:14**

- Andy Powell: black anyway which is even worse because well at least it's visible like at least it's visible but they weren't using asana understandably I think so yeah what I've moved to is on those parent pages and I actually did it for confluence as well so we have a parent page for the products in confluence an MCB for that as well so yeah I can share with you that prompt At the moment it's part of a skill that is processing the whole product sync into my dossas etc. But it basically just yeah I can send it to you. Yeah, to be honest,
- Tonda Kmoch: I think that as I'm as we are going through these topics I more and more see that the biggest issue
- Andy Powell: I
- Tonda Kmoch: is not the skills or like technicality and so on but it's more like the alignment between us like how we will do that and maybe that's where that Johan can actually like play the role in this that we will not everyone is doing something but it will be Yan who will always make sure that this like happens.

**00:12:22**

- Matej Novak: And I'm happy that.
- Tonda Kmoch: Yeah.
- Andy Powell: in like the interim I think it can just continue to be me because I have like most of like well now it's extremely easy we need to scale it but I mean until like we come up with some other
- Tonda Kmoch: But then we need
- Andy Powell: solution. Yeah.
- Tonda Kmoch: I think that we need to kind of let's say upgrade this what we have to like let's say official solution because it's like let's say almost like a lot of like uh proof of concepts or like some things that are like let's say half the way to the final solution and I think that that's why I was like proposing that I believe that type of the task that is like making everything black or white. What I always like prefer is task like this like let's remove everything from asana for the teams and let's put it to the to those like pages. So everything from like the next week is only there no like no more asana. So at least like one thing is like ticked and we know okay whenever I go for tasks they are always like there because now it's like kind of everywhere.

**00:13:28**

- Andy Powell: Hey, heat. Hey.
- Matej Novak: Hat.
- Tonda Kmoch: Yeah.
- Kryštof Šraier: Um,
- Tonda Kmoch: Uh when it comes to the product sync, so you know that we explored the using outline for two product syncs. Uh I would like to take that part that I will cover the part that the transcripts from the meetings will get to the folder of the transcripts of like product syncs in like outline. So we will not need like hey I'm like running I'm not and so on but no everything will be just in the outline what should be like the uh the end goal and yeah and if you can share your like prompts or for processing those like action points so we can like start preparing that for Johan or like someone who would be like running this like in in future. I could add it to so maybe awesome.
- Andy Powell: We should there
- Tonda Kmoch: I can add the info to have it as a plugin
- Andy Powell: already
- Matej Novak: They can call it marketplace.
- Tonda Kmoch: available.
- Matej Novak: place.
- Denisa Lorencova: Because that

**00:14:37**

- Andy Powell: to share it. I have I don't think we need that. Well, it's just a file that you just like installed. Sorry. Okay,
- Tonda Kmoch: Yes. So you just said that you you will do this yourself.
- Andy Powell: cool.
- Matej Novak: with the call up to now you you had a I think really good strategy of asking the product leads to do those concrete steps in setting up the projects in outline such as you know creating the A4 page uploading the skills like each of them doing it for themselves uh don't you want to keep the line so that they
- Tonda Kmoch: set it up themselves. They will have no ownership.
- Matej Novak: understand how it was done. It sort of increases the ownership. It's not like Tonda setting up setting up a structure for all of us and us trying to understand how it actually works and what is where. Yeah. So yeah, let's get a
- Tonda Kmoch: So what I want to do is that as we are meeting with all the team all these like four priority team or like those four AISG teams I want to learn from them how they are processing those meetings because unfortunately I am afraid that no one is like kind of let's say discipline in this and kind of let's say yeah there is some script yeah we can do that but no one is like daytoday like using that only maybe except like van that he's maybe

**00:15:53**

- Tonda Kmoch: like very technical so that's why he's doing that so I agree with you that for all the meetings happening on the project it should be like on them but I believe that maybe us demonstrating that there is there there is a way how to make it as a let's say reliable day-to-day working solution that at least those product things are like resolved this way. So then they when they will see it in action they might come to us and they might say hey Hanza we want to have the same thing on our project please can you turn on that script or whatever. So it's like happening because yeah I think that now now everyone is like looking on that from like kind of selfish perspective that hey I finished my meeting okay I take it from granola and so on and everyone is like let's say isolated we need to have that knowledge base where is like everything so anytime you remember oh we were uh having the kickoff of that project and I want to use my AI to actually learn what we agreed on those like kickoff it cannot be that you go to someone ask for permissions and so on.

**00:16:59**

- Tonda Kmoch: No, that needs to be everything on on one place. And that's why I I think that starting with the uh product syncs is a great like starting point when people will see that there is a way that is happening just like automatically. So specifically I will reschedu all the product sync meetings. I will turn the transcript like on on all of them and I will probably speak with Honza that that script that that we have and we are using on intake and like works like reliably where we will like put it. So it will like every day I don't know seven times or 10 times like run and like put those meetings of the product things to to outline and no one will ever need to worry about that because it will just get there like automatically. Or can can we give it a
- Matej Novak: So, we have those four meetings this week that you scheduled. I will be with you on all of those meetings. Let's let's try to give it a shot and at least do it together.

**00:17:53**

- Matej Novak: Like, this is actually very fast. All of those things that you asked for are very simple and very quick. And if you're ready for the kind
- Tonda Kmoch: not technical. So I cannot imagine that I will ask Danny like hey install NodeJS like do here do environment variables blah blah blah. It can be like oh I didn't know you need to install how else it will get to the outline. I thought it was just
- Matej Novak: having the space in repo uploading the skills there.
- Tonda Kmoch: about
- Matej Novak: Oh, it mean I
- Tonda Kmoch: I believe that the only way how we can do that is through the script really like code because let's say on some
- Andy Powell: If you want to do
- Tonda Kmoch: like quality level if you want to hey it's doing something then yeah of course you can like ask
- Andy Powell: it,
- Tonda Kmoch: the MCP but you will always get to slightly like different results because sometimes it will take from maybe Gemini sometimes from granola sometimes it will have full transcript
- Matej Novak: Of

**00:18:54**

- Tonda Kmoch: something everyone will be using that slightly different I think that there should be a standard what is a meeting transcript and what's the structure and how it gets there but the creation of a
- Matej Novak: course themselves yes and those using those basically free skills that
- Tonda Kmoch: for
- Matej Novak: you've created. Yes. Yes. And on that we will be checking with them this week. Yes. which will which will I think is the buy in that we are actually doing this transformation together. Yes.
- Tonda Kmoch: can help me with that. That would be awesome. No, I will.
- Matej Novak: Yes.
- Tonda Kmoch: And last to the product thing. So, I would like to now move all the projects to outline all these at least these um uh from AISG uh projects to to outline with the products. So from from we will not do only like RCM and learning spring and like intake but we will do also npm and EP in in outline for for the product links next week. So the project

**00:19:57**

- Matej Novak: It's it's four projects in total. Yeah.
- Tonda Kmoch: so
- Matej Novak: AISG projects EP learning spring open loop area uh
- Tonda Kmoch: update about Kubas involvement. So yeah,
- Matej Novak: small
- Tonda Kmoch: I would like yeah it's it's like challenging with Kuba because the workload of like things on him is like more like growing with this like milit situation but however I want to involve him. So I will meet with him probably this week uh and uh like update him on on everything and uh yeah and the onu is just making sure that uh so I have like agreement financially accept
- Andy Powell: from every relevant person and now it's actually just about making it happen which means having a replacement. So so like what is the specific plan? So really that'll be a probably a squad roster discussion for next week because I want to get like final agreement with the exacts next week squad roster but it's already in the hiring road map that we hiring three tech leads. Yeah. So then the
- Tonda Kmoch: topic is that and Hanzo already mentioned that that we will need in

**00:21:02**

- Andy Powell: next
- Tonda Kmoch: future have some like let's say knowledge base or like starting pack of AI functionalities for all our projects. And maybe part of that will be script for generating the presentations. It will be maybe script for processing the meetings. It will be skills for preparing for productioning blah blah blah. And yeah, we need to have some like strategy or like how we will do that. So then like the not only that when you kick off the project you can take take the data but already as you are running the project when there is a new version of that skill for creating the presentation you can somehow like pull it to to your repo and and you can also like deviate from that when you want to like adjust that for for your needs. So Honzai, it would be amazing if you can not only create that repo but also like think about this like whole like strategy of like I don't know branching or like whatever or maybe even maybe maybe even not doing that through the repo maybe through some this like shared skills across organization and so on.

**00:22:15**

- Tonda Kmoch: That's why the plugin does make sense.
- Andy Powell: this level once we have like enough that it is just some plugin that people everyone installs on board because that's just a plugin is just a set a bunch of skills together.
- Tonda Kmoch: Okay. And one uh like key task what or like activity that needs to happen is that I want to start organizing that process for like how the things will get to that like center point. So it should not be that just like everyone has an idea okay let's put it there but probably there should be some like alignment that we will like define some standards what it means to put something like there that is like documented that we know that it's it's it will be somehow communicated to the teams and and so on. So this I will put together and uh yeah next to that I think that we that's like a huge like generally like a huge topic is like to start thinking like what's the future like oklab way so if it's like this or if it's something like different or if it's like implement it through the AI or like what exactly it is so but is this with some like

**00:23:28**

- Andy Powell: layer that a human can understand on top of it if that makes sense. Because we're building it, we built it for humans. Now we're changing that to it's made for LLMs. Then we need some human layer on top of that bit to explain how to work with the work that works with the LLMs. And is this
- Matej Novak: activity related to the plug-in that villain created the oxlap way plugin. I don't think so because
- Tonda Kmoch: He kind of let's say took whatever was there and he was trying to use it. This is more about changing that source of truths that like beginning. So it's it's and and this is more like let's say for future. So I believe that first we need to learn from the projects how they are using them. We need to first like uh create some like let's say foundation and so on and then in future we need to just like think about and I also
- Andy Powell: I also think that something that we need to be smart about is h like how we communicate and roll out things because I think we we will only have so much like to be honest like capital with to like give them and teach them things that they feel are helpful.

**00:24:38**

- Andy Powell: So my point is like when we first roll out some things, let's make sure we choose ones that are like like for example, I think this presentation one is good because it like helps everyone quickly and it's like it's like easy to install. It's like separate. So I think we need to be smart about not the first like few things not being like oh you have to orchestrate 20 different things for to make it work. Like I think to be honest, we need to give the team some quick wins to like start building that like muscle that that they feel like, "Oh wow, this is making my life easier." Like the first few things we roll out should be like, "Oh, this is great. I wish I'd had this a while ago." Your skill is now
- Matej Novak: for everyone who just the slides.
- Andy Powell: accessible
- Matej Novak: No, I will like share
- Andy Powell: people. So you did actively share it with me.
- Matej Novak: it.
- Andy Powell: That's how it got I shared it with you Kristoff then because we used it the other day and and then you today with your uh with your template you know uh I'll share that with everyone.

**00:25:36**

- Andy Powell: It's uh it's funny. So if
- Matej Novak: initiative on the oak way is not connected to any of your thinking yet because I try I tried to I
- Andy Powell: you
- Matej Novak: installed it in the command line cloud and I played with it a little bit I very quickly got discouraged because it's sort of difficult to use it's it's a set of skills uh basically just will probably
- Kryštof Šraier: just took a oak slab way and like you know hey turn this into this
- Andy Powell: blunt force with AI to be honest
- Tonda Kmoch: In a lot of cases the lab is like over using the AI a lot. So okay. Yeah. So last two minutes. Uh here is that note on you mate to work with Danny and like putting together this uh stuff for like the product work that we on the learning spring that we discussed earlier. Yes. Yeah. We had a first on this. This is not like for this week. This is more like that I will create a task for you and you will be like assigned on that and you will like tell like when when something is like realistic on this because this

**00:26:50**

- Matej Novak: It's a broad topic. Uh today we had a really difficult meeting on this.
- Tonda Kmoch: is
- Matej Novak: So yeah, let's just chat more about this. But yeah, keep the task there definitely. That's
- Tonda Kmoch: and last and maybe almost the most like important topic is about like the business model.
- Matej Novak: a
- Tonda Kmoch: So thank you Andy for sharing the table and so on. I just like wonder or I would maybe still like or yeah there should be some like let's say revenue part of of of that like AI and I was just like thinking if we just don't want to like continue this mode that we have like one person that is like double built because in fact we are not cheating right well we are 50% or maybe even more like efficient. So, and that can be the way how we will for now get the money back and hopefully get that budget for like whatever tool we will like need. Well, that's why we're getting
- Andy Powell: push back on budget even though I'm going to start building it to the clients.

**00:27:43**

- Tonda Kmoch: no
- Andy Powell: That's why we're getting no push back because well those two people and open loop from my perspective are like a good portion of that ROI from AI work. Yeah. So yes, yes, we will continue to do this even if it's also like QA on on on learning spring now or yeah
- Kryštof Šraier: be it's not because of AI right or that those people are like you know double builds the last not in a
- Andy Powell: ridiculous. Yeah, I didn't I just like
- Kryštof Šraier: detail but I remember that the discussion was like well on RCM there are no like let's say requirements so that was like a situation one month ago but when you look on
- Tonda Kmoch: the whole like open loop as a client.
- Kryštof Šraier: the
- Tonda Kmoch: Yes, on RCM there were not like requirements but on the intake the velocity like what we developed like it's like I don't know three times four times more than we were like able to do before and everyone is saying that for for for like those features. So,
- Matej Novak: Yeah, maybe

**00:28:48**

- Tonda Kmoch: so like three people on one client is of course like too much like double those three people as as we were like in this moment for for a few days but like having one person overall in the whole company is probably like totally fine and that one person in fact will pay for all the cloth bills right
- Kryštof Šraier: should be definitely either engineer or QA. Most likely engineer,
- Tonda Kmoch: So
- Kryštof Šraier: right?
- Andy Powell: And it seems like Claude, by the way,
- Kryštof Šraier: Okay.
- Andy Powell: has fixed that analytical issue because it's now separating out those PRs that are done with core code versus all those PRs. So you we actually have a leaderboard. Uh and we still
- Tonda Kmoch: don't so we still don't know how much people are using the the cloth right for this. There is no solution. No, this is like lines or requests. I mean like
- Andy Powell: I'm going to like consumption.
- Jan Barta: You need a third party solution for that.
- Tonda Kmoch: uh
- Jan Barta: I was checking for example, Sentry has a plug-in which everybody needs to install or enable but through that we could Yeah.

**00:30:05**

- Jan Barta: So
- Tonda Kmoch: Hanza this on you again. This is not like super urgent like immediately but I think that we should have some strategy where we will understand how
- Jan Barta: I
- Tonda Kmoch: much because maybe someone is on premium and standard would be enough for him and maybe someone like exact opposite. So we need to like see this. I mean the opposite we
- Jan Barta: usually because people will reach out if they need to upgrade,
- Tonda Kmoch: know
- Jan Barta: but obviously not for the downgrade. So, yeah. Yeah. Awesome.
- Tonda Kmoch: anything else guys this is amazing.
- Andy Powell: Maybe the only the only thing that I'm a little unsure of is that maybe isn't covered here is that
- Tonda Kmoch: So, who is going to
- Andy Powell: that DMT. So we can only have DMT and then the project instead live underneath it.
- Tonda Kmoch: own
- Andy Powell: who is like keeping that up to date if that makes
- Matej Novak: I own that.
- Andy Powell: sense. So we have those product syncs, we have where those projects are and then we have theation

**00:31:05**

- Tonda Kmoch: client
- Andy Powell: and ideally we need to synthesize and maybe I can own this as a topic because ultimately this is my role right but ideally we need to synthesize that into some central here's where our projects are here's what the status of this project is that we that we say from the DMT perspective that's what I've tried to do so far does it make sense that I just continue to own that right now Because to be honest that's where so much of the content that I am doing is coming from. It's like having that central synthesis not the team's perspective not the client's perspective my perspective and for
- Tonda Kmoch: visibility only.
- Andy Powell: DM
- Tonda Kmoch: Yes, I think that's the most important pages that we have.
- Andy Powell: well for me it is anyway. and the challen that's why
- Tonda Kmoch: said that the biggest like challenge is not the tools, not even the skills,
- Andy Powell: Nice.
- Tonda Kmoch: but that like collaboration. No, not not not how but that collaboration. So I think that a great action point would be that if everyone can have a look what you put there like so far and really like review it from like everyone's perspective because everyone's perspective can be like different than yours and maybe we might come up that actually there will need to be and document and document maybe or maybe it will be just sections or like something.

**00:32:29**

- Tonda Kmoch: So yeah, it would be great if everyone will have a look on those documents so we will understand if it should be if it if it's even realistic to have it centralized. You mean in this structure? Yeah,
- Matej Novak: All
- Tonda Kmoch: you're not uh product projects and
- Andy Powell: list of documents projects.
- Matej Novak: those
- Tonda Kmoch: they're like statuses. It's under DMT and yeah,
- Kryštof Šraier: Is that
- Tonda Kmoch: sorry. See you. So the additional
- Andy Powell: It gives you nothing on Yeah, I think I have a Do I have a meeting now? No, I don't. Okay. So, does it have the user level? Yeah, only for clawed code only. But that's what the others know. This is this is people that you wouldn't have this data. This is such an important and basic data like individual usage is to broken down by something. How will we ever learn to be efficient with AI use if we don't have the data? Jesus. It's just active users. Maybe cloud is not incentivized to share this information. So that yeah can be like this is co work. Okay, this is very basic. This is very basic analytics. Yeah, this is the most detailed I think. Yeah, I just And the traffic would Yeah, maybe they are just they have no motivation to provide that data.
- This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

---

## Metadata

- **Date**: 2026-04-28
- **Source**: Gemini | [Open in Google Docs](https://docs.google.com/document/d/1aQ5iAM9wy5VsZQ8JJHGY3wjSwIKGymSoE0W-FzG5ifs)
- **meeting_id**: 1aQ5iAM9wy5VsZQ8JJHGY3wjSwIKGymSoE0W-FzG5ifs
- **owner**: Tonda Kmoch <tonda@oakslab.com>
- **gemini_doc_id**: 1aQ5iAM9wy5VsZQ8JJHGY3wjSwIKGymSoE0W-FzG5ifs
- **meeting_time**: 15:01
- **meeting_timezone**: CEST
