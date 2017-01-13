
cbcr_root = "Canada Business Corporations Regulations"

cbcr_1_1 = "Part 1 General Electronic Documents 7 (1) For the purpose of paragraph 252_3(2)(a) of the Act, the consent shall be in writing."\
"(2) For the purpose of paragraph 252_3(2)(b) of the Act, a notice, document or other information that is not required under the Act to be sent to a specific place may be sent as an electronic document to a place other than to an information system designated by the addressee under paragraph 252_3(2)(a) of the Act by posting it on or making it available through a generally accessible electronic source, such as a website, and by providing the addressee with notice in writing of the availability and location of that electronic document."

cbcr_1_2 = "Part 1 General Notice of Meetings" \
     "44 For the purpose of subsection 135(1) of the Act, the prescribed period for the directors to provide notice of the time and place of a meeting of shareholders is not less than 21 days and not more than 60 days before the meeting."
cbcr_2_1 = "PART 7 Proxies and Proxy Solicitation Form of Proxy 54 For the purpose of subsection 149(1) of the Act, a form of proxy shall be in the form provided for in section 9.4 (Content 	of Form of Proxy) of NI 51-102."
cbcr_2_2_1 = "PART 7 Proxies and Proxy Solicitation Form of Proxy Management Proxy Circular" \
    "55 (1) Subject to subsection (3), a management proxy circular shall be in the form provided for in Form 51-102F5 (Information Circular) of NI 51-102, which form, in the circumstances described in Item 8 of Part 2 of that Form, includes the statement referred to in that Item."
cbcr_2_2_2 = "PART 7 Proxies and Proxy Solicitation Form of Proxy Management Proxy Circular 55 (2) A management proxy circular shall also set out the following:"\
    "(a) the percentage of votes required for the approval of any matter that is to be submitted to a vote of shareholders at the meeting, other than the election of directors;"\
    "(b) a statement of the right of a shareholder to dissent under section 190 of the Act with respect to any matter to be acted on at the meeting and a brief summary of the procedure to be followed to exercise that right;"\
    "(c) a statement, signed by a director or an officer of the corporation, that the contents and the sending of the circular have been approved by the directors; and"\
    "(d) a statement indicating the final date by which the corporation must receive a proposal for the purpose of paragraph 137(5)(a) of the Act."
cbcr_2_3 = "PART 7 Proxies and Proxy Solicitation Form of Proxy 56 For the purpose of subsection 150(2) of the Act, the prescribed form of statement that shall accompany the copy of the management proxy circular to be sent to the Director under that subsection is a statement signed by a director or an officer of the corporation, to the effect that a copy of the circular has been sent to each director, to each shareholder whose proxy has been solicited and to the auditor of the corporation."

cbcr = {'id': cbcr_root, 'children': [
                    {'id': cbcr_1_1, 'children':[]},
                    {'id': cbcr_1_2, 'children':[]},
                    {'id': cbcr_2_1, 'children':[]},
                    {'id': cbcr_2_2_1, 'children':[]},
                    {'id': cbcr_2_2_2, 'children': []},
                    {'id': cbcr_2_3, 'children': []},
                ]}

################################################################################################

osact_root = "Ontario Securities Act"

osact_1_1 ="Definitions 1. (1)  In this Act, 'form of proxy' means a written or printed form that, upon completion and execution by or on behalf of a security holder, becomes a proxy;"
osact_1_2 ="Definitions 1. (1)  In this Act, 'proxy' means a completed and executed form of proxy by means of which a security holder has appointed a person or company as the security holder's nominee to attend and act for and on the security holder's behalf at a meeting of security holders;"
osact_1_3 ="Definitions 1. (1)  In this Act, 'reporting issuer' means an issuer,"\
	"(a) that has issued voting securities on or after the 1st day of May, 1967 in respect of which a prospectus was filed and a receipt therefor obtained under a predecessor of this Act or in respect of which a securities exchange take-over bid circular was filed under a predecessor of this Act,"\
	"(b)	that has filed a prospectus and for which the Director has issued a receipt under this Act, "\
	"(b.1)	that has filed a securities exchange take-over bid circular under this Act before December 14, 1999,"\
	"(c)	any of whose securities have been at any time since the 15th day of September, 1979 listed and posted for trading on any exchange in Ontario recognized by the Commission, regardless of when such listing and posting for trading commenced,"\
	"(d)	to which the Business Corporations Act applies and which, for the purposes of that Act, is offering its securities to the public,"\
	"(e)	that is the company whose existence continues following the exchange of securities of a company by or for the account of such company with another company or the holders of the securities of that other company in connection with,"\
	"(i)	a statutory amalgamation or arrangement, or"\
	"(ii)	a statutory procedure under which one company takes title to the assets of the other company that in turn loses its existence by operation of law, or under which the existing companies merge into a new company,"\
    "where one of the amalgamating or merged companies or the continuing company has been a reporting issuer for at least twelve months, or"\
	"(f)	that is designated as a reporting issuer in an order made under subsection 1 (11);"

osact_2_1 ="PART XVIII CONTINUOUS DISCLOSURE Filing of information circular 81 (1) Where the management of a reporting issuer is required to send an information circular under clause 86 (1) (a), the reporting issuer shall forthwith file a copy of such information circular certified in accordance with the regulations."
osact_2_2 ="PART XVIII CONTINUOUS DISCLOSURE Filing of information circular Idem (2)  In any case where subsection (1) is not applicable, the reporting issuer shall file annually within 140 days from the end of its last financial year a report prepared and certified in accordance with the regulations."

osact_3_1 = "PART XIX PROXIES AND PROXY SOLICITATION Definitions 84.  In this Part,"\
"'information circular' means an information circular prepared in accordance with the regulations;"

osact_3_2 ="PART XIX PROXIES AND PROXY SOLICITATION Mandatory solicitation of proxies"\
"85. Subject to section 88, if the management of a reporting issuer gives or intends to give to holders of its voting securities notice of a meeting, the management shall, concurrently with or prior to giving the notice to the security holders whose latest address as shown on the books of the reporting issuer is in Ontario, send to each such security holder who is entitled to notice of meeting, at the security holder's latest address as shown on the books of the reporting issuer, a form of proxy for use at the meeting that complies with the regulations."

osact_3_3_1 = "PART XIX PROXIES AND PROXY SOLICITATION Information Circular"\
"86 (1)  Subject to subsection (2) and section 88, no person or company shall solicit proxies from holders of its voting securities whose latest address as shown on the books of the reporting issuer is in Ontario unless,"\
"(a) in the case of a solicitation by or on behalf of the management of a reporting issuer, an information circular, either as an appendix to or as a separate document accompanying the notice of the meeting, is sent to each such security holder of the reporting issuer whose proxy is solicited at the security holder's latest address as shown on the books of the reporting issuer; or"\
"(b) in the case of any other solicitation, the person or company making the solicitation, concurrently with or prior thereto, delivers or sends an information circular to each such security holder whose proxy is solicited."
osact_3_3_2 = "PART XIX PROXIES AND PROXY SOLICITATION Information Circular 86 Application of subs. (1) (2) Subsection (1) does not apply to,"\
"(a) any solicitation, otherwise than by or on behalf of the management of a reporting issuer, where the total number of security holders whose proxies are solicited is not more than fifteen, two or more persons or companies who are the joint registered owners of one or more securities being counted as one security holder;"\
"(a.1) any solicitation, otherwise than by or on behalf of the management of a reporting issuer, in such other circumstances as may be prescribed in the regulations;"\
"(b)any solicitation by a person or company made under section 49; or"\
"(c) any solicitation by a person or company in respect of securities of which he, she or it is the beneficial owner."

osact_3_4 = "PART XIX PROXIES AND PROXY SOLICITATION Voting where proxies 87 The chair at a meeting has the right not to conduct a vote by way of ballot on any matter or group of matters in connection with which the form of proxy has provided a means whereby the person or company whose proxy is solicited may specify how such person or company wishes the securities registered in his, her or its name to be voted unless,"\
"(a) a poll is demanded by any security holder present at the meeting in person or represented thereat by proxy; or"\
"(b) proxies requiring that the securities represented thereby be voted against what would otherwise be the decision of the meeting in relation to such matters or group of matters total more than 5 per cent of all the voting rights attached to all the securities entitled to be voted and be represented at the meeting."

osact = {'id': osact_root, 'children': [
                    {'id': osact_1_1, 'children':[]},
                    {'id': osact_1_2, 'children': []},
                    {'id': osact_1_3, 'children': []},
                    {'id': osact_2_1, 'children':[]},
                    {'id': osact_2_2, 'children': []},
                    {'id': osact_3_1, 'children': []},
                    {'id': osact_3_2, 'children': []},
                    {'id': osact_3_3_1, 'children': []},
                    {'id': osact_3_3_2, 'children': []},
                    {'id': osact_3_4, 'children': []},
        ]}

######################################################################################################

cbcact_root ="Canada Business Corporations Act"

cbcact_1_1 = "PART I Interpretation and Application Definitions"\
"2 (1) In this Act,"\
"distributing corporation means, subject to subsections (6) and (7), a distributing corporation as defined in the regulations;"\
"prescribed means prescribed by the regulations;"\
"send includes deliver;"

cbcact_2_1_1 ="PART XII Shareholders Place of meetings 132 (1) Meetings of shareholders of a corporation shall be held at the place within Canada provided in the by-laws or, in the absence of such provision, at the place within Canada that the directors determine. "
cbcact_2_1_2 ="PART XII Shareholders Meeting outside Canada (2) Despite subsection (1), a meeting of shareholders of a corporation may be held at a place outside Canada if the place is specified in the articles or all the shareholders entitled to vote at the meeting agree that the meeting is to be held at that place. "
cbcact_2_1_3 ="PART XII Shareholders Exception (3) A shareholder who attends a meeting of shareholders held outside Canada is deemed to have agreed to it being held outside Canada except when the shareholder attends the meeting for the express purpose of objecting to the transaction of any business on the grounds that the meeting is not lawfully held."
cbcact_2_1_4 =" PART XII Shareholders Participation in meeting by electronic means (4) Unless the by-laws otherwise provide, any person entitled to attend a meeting of shareholders may participate in the meeting, in accordance with the regulations, if any, by means of a telephonic, electronic or other communication facility that permits all participants to communicate adequately with each other during the meeting, if the corporation makes available such a communication facility. A person participating in a meeting by such means is deemed for the purposes of this Act to be present at the meeting."
cbcact_2_1_5 =" PART XII Shareholders Meeting held by electronic means (5) If the directors or the shareholders of a corporation call a meeting of shareholders pursuant to this Act, those directors or shareholders, as the case may be, may determine that the meeting shall be held, in accordance with the regulations, if any, entirely by means of a telephonic, electronic or other communication facility that permits all participants to communicate adequately with each other during the meeting, if the by-laws so provide."

cbcact_2_2_1 ="PART XII Shareholders Calling annual meetings"\
"133 (1) The directors of a corporation shall call an annual meeting of shareholders"\
"(a) not later than eighteen months after the corporation comes into existence; and"\
"(b) subsequently, not later than fifteen months after holding the last preceding annual meeting but no later than six months after the end of the corporation's preceding financial year."
cbcact_2_2_2 ="PART XII Shareholders Order to delay calling of annual meeting (3) Despite subsection (1), the corporation may apply to the court for an order extending the time for calling an annual meeting."

cbcact_2_3_1 ="PART XII Shareholders Fixing record date"\
"134 (1) The directors may, within the prescribed period, fix in advance a date as the record date for the purpose of determining shareholders"\
"(c) entitled to receive notice of a meeting of shareholders;"\
"(d) entitled to vote at a meeting of shareholders; "
cbcact_2_3_2 = "PART XII Shareholders No record date fixed (2) If no record date is fixed,"\
"(a) the record date for the determination of shareholders entitled to receive notice of a meeting of shareholders shall be"\
"(i) at the close of business on the day immediately preceding the day on which the notice is given, or"\
"(ii) if no notice is given, the day on which the meeting is held; "
cbcact_2_3_3 = "PART XII Shareholders When record date fixed (3) If a record date is fixed, unless notice of the record date is waived in writing by every holder of a share of the class or series affected whose name is set out in the securities register at the close of business on the day the directors fix the record date, notice of the record date must be given within the prescribed period"\
"(a) by advertisement in a newspaper published or distributed in the place where the corporation has its registered office and in each place in Canada where it has a transfer agent or where a transfer of its shares may be recorded; and"\
"(b) by written notice to each stock exchange in Canada on which the shares of the corporation are listed for trading."

cbcact_2_4_1 ="PART XII Shareholders Notice of meeting"\
"135 (1) Notice of the time and place of a meeting of shareholders shall be sent within the prescribed period to"\
"(a) each shareholder entitled to vote at the meeting;"\
"(b) each director; and"\
"(c) the auditor of the corporation."
cbcact_2_4_2 ="PART XII Shareholders Exception shareholders not registered (2) A notice of a meeting is not required to be sent to shareholders who were not registered on the records of the corporation or its transfer agent on the record date determined under paragraph 134(1)(c) or subsection 134(2), but failure to receive a notice does not deprive a shareholder of the right to vote at the meeting."

cbcact_2_5_1 ="PART XII Shareholders Voting"\
" 141 (1) Unless the by-laws otherwise provide, voting at a meeting of shareholders shall be by show of hands except where a ballot is demanded by a shareholder or proxyholder entitled to vote at the meeting."
cbcact_2_5_2 ="PART XII Shareholders Ballot (2) A shareholder or proxyholder may demand a ballot either before or after any vote by show of hands."
cbcact_2_5_3 ="PART XII Shareholders Electronic voting (3) Despite subsection (1), unless the by-laws otherwise provide, any vote referred to in subsection (1) may be held, in accordance with the regulations, if any, entirely by means of a telephonic, electronic or other communication facility, if the corporation makes available such a communication facility."
cbcact_2_5_4 ="PART XII Shareholders Voting while participating electronically (4) Unless the by-laws otherwise provide, any person participating in a meeting of shareholders under subsection 132(4) or (5) and entitled to vote at that meeting may vote, in accordance with the regulations, if any, by means of the telephonic, electronic or other communication facility that the corporation has made available for that purpose."

cbcact_3_1_1 = "PART XIII Proxies Definitions 147 In this Part, form of proxy means a written or printed form that, on completion and execution or, in Quebec, on signing by or on behalf of a shareholder, becomes a proxy;"
cbcact_3_1_2 = "PART XIII Proxies Definitions 147 In this Part, intermediary means a person who holds a security on behalf of another person who is not the registered holder of the security, and includes" \
"(a) a securities broker or dealer required to be registered to trade or deal in securities under the laws of any jurisdiction;"\
"(b) a securities depositary;"\
"(c) a financial institution;"\
"(d) in respect of a clearing agency, a securities dealer, trust company, bank or other person, including another clearing agency, on whose behalf the clearing agency or its nominees hold securities of an issuer;"\
"(e) a trustee or administrator of a self-administered retirement savings plan, retirement income fund, education savings plan or other similar self-administered savings or investment plan registered under the Income Tax Act;"\
"(f) a nominee of a person referred to in any of paragraphs (a) to (e); and"\
"(g) a person who carries out functions similar to those carried out by individuals or entities referred to in any of paragraphs (a) to (e) and that holds a security registered in its name, or in the name of its nominee, on behalf of another person who is not the registered holder of the security."

cbcact_3_2_1 ="PART XIII Proxies solicit or solicitation (a) includes"\
"(i) a request for a proxy whether or not accompanied by or included in a form of proxy,"\
"(ii) a request to execute or not to execute or, in Quebec, to sign or not to sign a form of proxy or to revoke a proxy,"\
"(iii) the sending of a form of proxy or other communication to a shareholder under circumstances reasonably calculated to result in the procurement, withholding or revocation of a proxy, and"\
"(iv) the sending of a form of proxy to a shareholder under section 149; but"
cbcact_3_2_2 ="PART XIII Proxies solicit or solicitation (b) does not include"\
"(i) the sending of a form of proxy in response to an unsolicited request made by or on behalf of a shareholder,"\
"(ii) the performance of administrative acts or professional services on behalf of a person soliciting a proxy,"\
"(iii) the sending by an intermediary of the documents referred to in section 153,"\
"(iv) a solicitation by a person in respect of shares of which the person is the beneficial owner,"\
"(v) a public announcement, as prescribed, by a shareholder of how the shareholder intends to vote and the reasons for that decision,"\
"(vi) a communication for the purposes of obtaining the number of shares required for a shareholder proposal under subsection 137(1.1), or"\
"(vii) a communication, other than a solicitation by or on behalf of the management of the corporation, that is made to shareholders, in any circumstances that may be prescribed; "\
"solicitation by or on behalf of the management of a corporation means a solicitation by any person pursuant to a resolution or instructions of, or with the acquiescence of, the directors or a committee of the directors."

cbcact_3_3 ="PART XIII Proxies Mandatory solicitation 149 (1) Subject to subsection (2), the management of a corporation shall, concurrently with giving notice of a meeting of shareholders, send a form of proxy in prescribed form to each shareholder who is entitled to receive notice of the meeting."

cbcact_3_4_1 ="PART XIII Proxies Soliciting proxies 150 (1) A person shall not solicit proxies unless"\
"(a) in the case of solicitation by or on behalf of the management of a corporation, a management proxy circular in prescribed form, either as an appendix to or as a separate document accompanying the notice of the meeting, or"\
"(b) in the case of any other solicitation, a dissident's proxy circular in prescribed form stating the purposes of the solicitation is sent to the auditor of the corporation, to each shareholder whose proxy is solicited, to each director and, if paragraph (b) applies, to the corporation."
cbcact_3_4_2 ="PART XIII Proxies Soliciting proxies Copy to Director (2) A person required to send a management proxy circular or dissident's proxy circular shall send concurrently a copy of it to the Director together with a statement in prescribed form, the form of proxy, any other documents for use in connection with the meeting and, in the case of a management proxy circular, a copy of the notice of meeting."

cbcact_3_5_1 ="PART XIII Proxies Duty of intermediary 153 (1) Shares of a corporation that are registered in the name of an intermediary or their nominee and not beneficially owned by the intermediary must not be voted unless the intermediary, without delay after receipt of the notice of the meeting, financial statements, management proxy circular, dissident's proxy circular and any other documents other than the form of proxy sent to shareholders by or on behalf of any person for use in connection with the meeting, sends a copy of the document to the beneficial owner and, except when the intermediary has received written voting instructions from the beneficial owner, a written request for such instructions. "
cbcact_3_5_2 ="PART XIII Proxies Restriction on voting (2) An intermediary, or a proxyholder appointed by an intermediary, may not vote shares that the intermediary does not beneficially own and that are registered in the name of the intermediary or in the name of a nominee of the intermediary unless the intermediary or proxyholder, as the case may be, receives written voting instructions from the beneficial owner."
cbcact_3_5_3 ="PART XIII Proxies Copies (3) A person by or on behalf of whom a solicitation is made shall provide, at the request of an intermediary, without delay, to the intermediary at the person's expense the necessary number of copies of the documents referred to in subsection (1), other than copies of the document requesting voting instructions."
cbcact_3_5_4 ="PART XIII Proxies Instructions to intermediary (4) An intermediary shall vote or appoint a proxyholder to vote any shares referred to in subsection (1) in accordance with any written voting instructions received from the beneficial owner."
cbcact_3_5_5 ="PART XIII Proxies Beneficial owner as proxyholder (5) If a beneficial owner so requests and provides an intermediary with appropriate documentation, the intermediary must appoint the beneficial owner or a nominee of the beneficial owner as proxyholder."


cbcact_4_1_1 ="PART XIV Financial Disclosure Annual financial statements 155 (1) Subject to section 156, the directors of a corporation shall place before the shareholders at every annual meeting"\
"(a) comparative financial statements as prescribed relating separately to"\
"(i) the period that began on the date the corporation came into existence and ended not more than six months before the annual meeting or, if the corporation has completed a financial year, the period that began immediately after the end of the last completed financial year and ended not more than six months before the annual meeting, and"\
"(ii) the immediately preceding financial year;"
cbcact_4_1_2 ="PART XIV Financial Disclosure Annual financial statements 155 (1) Subject to section 156, the directors of a corporation shall place before the shareholders at every annual meeting (b) the report of the auditor, if any; and"
cbcact_4_1_3 ="PART XIV Financial Disclosure Annual financial statements 155 (1) Subject to section 156, the directors of a corporation shall place before the shareholders at every annual meeting (c) any further information respecting the financial position of the corporation and the results of its operations required by the articles, the by-laws or any unanimous shareholder agreement."

cbcact_4_2 ="PART XIV Financial Disclosure Copies to shareholders 159(1) A corporation shall, not less than twenty-one days before each annual meeting of shareholders or before the signing of a resolution under paragraph 142(1)(b) in lieu of the annual meeting, send a copy of the documents referred to in section 155 to each shareholder, except to a shareholder who has informed the corporation in writing that he or she does not want a copy of those documents."

cbcact_4_3_1 ="PART XIV Financial Disclosure Copies to Director 160 (1) A distributing corporation, any of the issued securities of which remain outstanding and are held by more than one person, shall send a copy of the documents referred to in section 155 to the Director"\
"(a) not less than twenty-one days before each annual meeting of shareholders, or without delay after a resolution referred to in paragraph 142(1)(b) is signed; and"
cbcact_4_3_2 ="PART XIV Financial Disclosure Copies to Director 160 (1) A distributing corporation, any of the issued securities of which remain outstanding and are held by more than one person, shall send a copy of the documents referred to in section 155 to the Director (b) in any event within fifteen months after the last preceding annual meeting should have been held or a resolution in lieu of the meeting should have been signed, but no later than six months after the end of the corporation's preceding financial year."

cbcact_5_1_1 ="PART XX.1 Documents in Electronic or Other Form Use not mandatory 252.3 (1) Nothing in this Act or the regulations requires a person to create or provide an electronic document."\
"Consent and other requirements (2) Despite anything in this Part, a requirement under this Act or the regulations to provide a person with a notice, document or other information is not satisfied by the provision of an electronic document unless"\
"(a) the addressee has consented, in the manner prescribed, and has designated an information system for the receipt of the electronic document; and"\
"(b) the electronic document is provided to the designated information system, unless otherwise prescribed."

cbcact_5_2 ="PART XX.1 Documents in Electronic or Other Form Creation and provision of information 252.4 A requirement under this Act or the regulations that a notice, document or other information be created or provided, is satisfied by the creation or provision of an electronic document if"\
"(a) the by-laws or the articles of the corporation do not provide otherwise; and"\
"(b) the regulations, if any, have been complied with."

cbcact_6_1 ="PART XXI General Notice to directors and shareholders 253 (1) A notice or document required by this Act, the regulations, the articles or the by-laws to be sent to a shareholder or director of a corporation may be sent by prepaid mail addressed to, or may be delivered personally to,"\
"(a) the shareholder at the shareholder's latest address as shown in the records of the corporation or its transfer agent"

cbcact = {'id': cbcact_root, 'children': [
                    {'id': cbcact_1_1, 'children':[]},
                    {'id': cbcact_2_1_1, 'children':[]},
                    {'id': cbcact_2_1_2, 'children': []},
                    {'id': cbcact_2_1_3, 'children': []},
                    {'id': cbcact_2_1_4, 'children': []},
                    {'id': cbcact_2_1_5, 'children': []},
                    {'id': cbcact_2_2_1, 'children': []},
                    {'id': cbcact_2_2_2, 'children': []},
                    {'id': cbcact_2_3_1, 'children': []},
                    {'id': cbcact_2_3_2, 'children': []},
                    {'id': cbcact_2_3_3, 'children': []},
                    {'id': cbcact_2_4_1, 'children': []},
                    {'id': cbcact_2_4_2, 'children': []},
                    {'id': cbcact_2_5_1, 'children': []},
                    {'id': cbcact_2_5_2, 'children': []},
                    {'id': cbcact_2_5_3, 'children': []},
                    {'id': cbcact_2_5_4, 'children': []},
                    {'id': cbcact_3_1_1, 'children': []},
                    {'id': cbcact_3_1_2, 'children': []},
                    {'id': cbcact_3_2_1, 'children': []},
                    {'id': cbcact_3_2_2, 'children': []},
                        {'id': cbcact_3_3, 'children': []},
                        {'id': cbcact_3_4_1, 'children': []},
                        {'id': cbcact_3_4_2, 'children': []},
                    {'id': cbcact_3_5_1, 'children': []},
                    {'id': cbcact_3_5_2, 'children': []},
                    {'id': cbcact_3_5_3, 'children': []},
                    {'id': cbcact_3_5_4, 'children': []},
                    {'id': cbcact_3_5_5, 'children': []},
                    {'id': cbcact_4_1_1, 'children': []},
                    {'id': cbcact_4_1_2, 'children': []},
                    {'id': cbcact_4_1_3, 'children': []},
                    {'id': cbcact_4_2, 'children': []},
                    {'id': cbcact_4_3_1, 'children': []},
                    {'id': cbcact_4_3_2, 'children': []},
                    {'id': cbcact_5_1_1, 'children': []},
                    {'id': cbcact_5_2, 'children': []},
                    {'id': cbcact_6_1, 'children': []},
                ]}


















