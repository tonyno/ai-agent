My colleagues shared following feedback. The feedback is coming from Andy, who is the COO, and also from Denisa, who is head of the design:


andy  [11:35 AM]
I don't know what to say other than this is outstanding. This is a pretty clear vision which incorporates everything we've been moving towards over the last few months. I love it!

Few initial thoughts:


Transcripts:
Would love to dive into where we use Granola vs Gemini a bit more, particularly for management roles.
Specific question: In that scenario where we use Granola, how does processing of, for example, DMT meeting work. We'd only want one person to process that meeting ideally if it's going to a shared folder.
As another example, I wouldn't be a big fan of daily processing. I often process immediately after a meeting.
I think you ask the question of if we should even move these sensitive meetings to outline, and I think it may make sense to keep them in Granola...

Architecture
This context is going to get enormous, and before executing on everything we should probably do some research into if a md structure in Outline can really handle this level of content and how the architecture/instructions would need to work so that it knows where to go and the context doesn't get too big. For example, I see that some people are moving to a database and semantic search over their MD files to enable this to work properly at scale. 

Outline
We are going to face some challenges with the security (see attached) and I don't think it's one we should take lightly given almost all sensitive info (client, people, company) will be stored in Outline. Self-hosting may be the best option.

Staffing
We need support on top of us to make this happen. We have Kuba, Johan, would be good to think about how their roles play into this structure


--------------------

image.png denisa  [12:51 PM]
@tonda What do you think about separating decisions? With references to original transcript? This is what I was trying to achieve on EPP, as the meetings are on various topics, to kind of distill decisions made there into streams where they belong. So that when we go work on something, AI does not have to sift through a bunch of transcripts on various topics, but almost has an "index" to go through first.

@andy to your point on daily vs manual processing and the potential duplicities

I had a skill which was scheduled to run daily, but it also could be run on demand if earlier processing was neeeded
It checked the meeting transcript for potentially sensitive information that should not be uploaded to shared repo (people topic) and asked if it was not sure
It checked the target folder for duplicities in case someone else had done the sync already on theirs



-------------

MY PROPOSAL HOW TO INCORPORATE / SOLVE THESE ASKS. PLEASE ASK ME FOLLOWUP QUESTIONS, SO EVERYTHING IS CLEAR AND UPDATE THE OUTLINE DOCUMENTS, PLUS GENERATE THE SUMMARY AS ANSWER FOR BOTH DENISA AND ANDY HOW THOSE COMMENTS WHERE INCORPORATED.

To first comment from Andy. We should go with everything with the priority for Gemini. So we should have a rule that we are using Gemini absolutely everywhere. And the only excuse when we are not using Gemini is the case when we cannot use it. That will be cases when the clients are using Zoom or Teams. Yeah, we should we should create some plan how to yeah how to force like everyone to start using the the Gemini on like every all the projects and all the meetings and absolutely like everywhere

The second question about the processing the granula. So how it works is that that script is taking that from whatever place the you that API key has the access to. so yeah, if the script is like run immediately after the meeting, it's taken from from granula. it also identifies the duplicity. So if if the meeting happened on both granula and gemini, it's prioritizing the Gemini because in Gemini is said like who is saying what, so it's better for for our purposes.

And third question about the access to the private information. So probably the easiest solution would be that we will really like in the create the technical account. The technical account, for example, transcript at the Oakslab.com will be invited to Google Meetings, but also that Google account will have access in granola to the meetings that are worth like sharing let's say publicly, like across across the whole organization. And this stuff will be processed automatically for one center point, and in cases when someone wants to process the meetings that that are not there, that are like more sensitive, those meetings will be processed, let's say manually or like by by those people on their machine, and probably those MD files will not be stored to the will not be stored to the outline and will be working only as a repository for for that like specific member of the digital management team.It's important to realize that probably everyone needs to have his own directory with with like his own clot memory and like and all the configuration and like all the MCP setup and all the tools and like everything, and all that shared context should be in the outline, but yes, there will be some stuff that will be kept just like locally on the machine of of that person.

And the architecture question from ND about the size of the data and like how to process that. So I believe that it's fine and like correct to start like anyhow and generate those MD files. And once we will see that it's some issue with that, then we can like think about moving that to some rack system or like some like storage or database or like something. So we need to start somewhere, we just need to create that content because we don't have like anything for now.

when it comes to outline, yeah, that security stuff is definitely a huge topic that needs to be resolved. please, as I asked earlier, create a new MD file in the outline with the action points or like the tasks, and definitely this should be one of the points. Also, go through the other existing outline documents that you already generated and aggregate from that list of like open tasks and like prioritize them and suggest who should be doing what.

Add Stephing, like who is doing what, and like what is doing Kuba, and what is the doing Johan. That's absolutely great point. please take the document where was proposed by you the like the split who is doing what, and make it like much more like precise, and let's have a conversation like together who is doing what specifically one of the huge topic is that we have the regular reporting system that we called product syncs, and those product syncs are being led by the leading trio on the project, product lead, design lead and tech lead, and through these meetings they are reporting the progress of the projects to us. These meetings are happening on Thursdays every two weeks. what correspond to the to the sprint, so like we have two week sprint, so that's why we have it every two weeks, and we have defined structure for these like product things, how they are reporting the progress. Until now we were using confluence, but I believe that now is the best step to actually move it to the outline. So this should be like one of the action points to move it for for pilot projects to to outline, and what is the most important is to like come up with the solution like how to leverage the AI for the preparation for the product things, but also for solving the follow-ups to the to the meeting. So now we were using Asana for for the action points, but probably it doesn't make like too much sense, and maybe those action points should be potentially directly in outline or potentially in linear, and that's like let's say again like another task to to resolve and like decide.

----

Matej put this comment: @tonda this is amazing. I was planning to implement something like this with LearningSpring as part of the AI pilot. The technical implementation will be the easy part. The harder part will be to get staff fully on board (need to change the way they work and think). There will also be impact on the stakeholder. Once/if we get our regulatory on board with Outline, I would go for intense pilot in a few projects and then scale to whole company. If we watch for the risks (all that come to mind were mentioned in your doc), then this has to be hugely beneficial

