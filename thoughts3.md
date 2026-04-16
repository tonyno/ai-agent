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