Data prep:
Elections result per Kalfi are published by 
ועדת הבחירות המרכזית לכנסת
for knessets numbered 18-22.
created a dictonary of all the different parties ( throught the years
in the last  elections.) symbols to number codes.


yeshuv type for all yeshuvs were found on a different excel table online:?


Kalfis locations were found on a seperate file online:
https://bechirot22.bechirot.gov.il/election/Kneset20/Pages/BallotsList.aspx



headline replaced to english from hebrew

replaced parties code in kneset elections published results with the code.
removed maatafot hitzoniot 875, 999, 9999



Data exploration:
vote percent:
histogram and box plot for general view,
over 100 vote percent 2 outliers:
SN 1198 3719
a lot of low voting percent outliers to look at:
n50smallest:

22 out of the 50 lowest vote percent kalfis are located
in Jerusalem so will look on the smallest kalfi seperatly, jerusalem and non jerusalem

In Jerusalem:



Outside Jerusalem:
mostly arab, badioum yeshivim with low vote %
3 kalfis in Tel Aviv
6 kalfis in Elat



BZB:
small:
most kalfis are in small jewish yeshuvs with a single kalfi
this yeshuvs/kalfis tend to have higher than the avg voting percent and very low error percent
most of the others are small non jewish yeshuvs
as par with the rest of the non jewish ( mostly arab) population, have low vote percent




ibbim is outstaning with very low vote percent
same with kfar silver
shar menahse , aluni yitzhak ayanot


there is a single kalfi with low bzb in a big city:
tiberaius bit sefer daliut.


BZB

there are total of only 36 different unique yeshuvs on the top 50 largest bzb kalfis.
6 of the highest bzb top 50 are in tel aviv
3 in Jerusalem

other than that 19 out of the 50 kalfis are in non jewish yeshuvs
somehow this yeshuvs has two very busy high bzb kalfis while other more
populated cities has either 1 (haifa , beersheva, ranna risho) or none


Arrabe
El'ad
Elat
I'billin
Nazareth
Ramat Gan
Sederot
Tel Sheva


exploring the list of biggest kalfis even further for the top 200 kalfis:
97 unique yeshuvs on that list
76 kalfis are in non jewish yeshuvs in 35 unique non jewish yeshuv.
List of 41 yeshuvs with more than 1 kalfi on top 200 highest bzb list:
|                           | Yeshuv |
|---------------------------|--------|
| Tel Aviv \- Yafo          | 17     |
| Jerusalem                 | 13     |
| Rahat                     | 7      |
| Ashqelon                  | 6      |
| Nazareth                  | 6      |
| Arrabe                    | 5      |
| Mughar                    | 4      |
| Tamra                     | 4      |
| Haifa                     | 4      |
| Afula                     | 4      |
| I'billin                  | 4      |
| Rishon LeZiyyon           | 3      |
| Kuseife                   | 3      |
| Shefar'am                 | 3      |
| Ramat Gan                 | 3      |
| Julis                     | 3      |
| Sederot                   | 3      |
| Modi'in\-Makkabbim\-Re'ut | 3      |
| Netanya                   | 3      |
| Tuba\-Zangariyye          | 3      |
| Hod HaSharon              | 3      |
| Kafar Yasif               | 2      |
| Nahariyya                 | 2      |
| Elat                      | 2      |
| Hadera                    | 2      |
| Ein Mahel                 | 2      |
| Giv'at Shemu'el           | 2      |
| Kafar Qara                | 2      |
| Ma'ale Adummim            | 2      |
| Beit Jann                 | 2      |
| Rehovot                   | 2      |
| Ra'annana                 | 2      |
| Binyamina\-Giv'at Ada     | 2      |
| Yanuh\-Jat                | 2      |
| Be'er Sheva               | 2      |
| Kafar Bara                | 2      |
| Tel Sheva                 | 2      |
| Umm al\-Fahm              | 2      |
| Peqi'in \(Buqei'a\)       | 2      |
| El'ad                     | 2      |
| Ashdod                    | 2      |



   
   
   what about top 1k biggest bzb kalfis?
   
   196 unique yeshuvs
   
   
   | lol123|
   |---------------------------------|
   | Tel Aviv \- Yafo            67  | 
   | Jerusalem                  50   |
   | Shefar'am                  26   |
   | Tamra                      25   |
   | Haifa                      24   |
   | Ramat Gan                  24   |
   | Rishon LeZiyyon            21   |
   | Tire                       21   |
   | Ashqelon                   20   |
   | Netanya                    20   |
   | Nazareth                   20   |
   | Petah Tiqwa                18   |
   | Hod HaSharon               17   |
   | Ashdod                     15   |
   | Bene Beraq                 15   |
   | Modi'in\-Makkabbim\-Re'ut    14 |
   | Rehovot                    13   |
   | Rahat                      13   |
   | Arrabe                     12   |
   | Hadera                     12   |
   | Kafar Qara                 12   |
   | Nahariyya                  12   |
   | Bet Shemesh                11   |
   | Ar'ara                     11   |
   | Kafar Kanna                10   |

    
    357 non jewish kalfis in top 1k biggest bzb
    in 63 unique yeshuvs



























Questions:
    a. Yeshuvim,
        1. when BZB increase but no kalfi num increase - did voters % gone down ?
        2. when kalfi num increase( or yahas kalfi is going up ) over the years did voters % gone up ?
        
        corraltion between ppk to percent voters total data kneset 18-22
        only yeshuvim with number of kalfi > 1.
        
        query_list = []
           num_kalfis_total =9263
            num_unique_yeshuvim =1156
            total_bzb =5278985
            total_voters =3229668
            total_vote_percent =0.6117971541877842
            avg_bzb_per_yeshuv =569.9001403433014
            (-0.09655280875367481, 1.2405445035168334e-20)
            
           query_list = [ Query.Ppk_Above_X=175]    
           num_kalfis_total =9154
            num_unique_yeshuvim =1068
            total_bzb =5264879
            total_voters =3221841
            total_vote_percent =0.6119496763363412
            avg_bzb_per_yeshuv =575.1451824339086
            (-0.12936284711768847, 1.852274665751351e-35)
           
                    
          query_list = [ Query.Ppk_Above_X=200]           
            num_kalfis_total =9120
            num_unique_yeshuvim =1035
            total_bzb =5258488
            total_voters =3217456
            total_vote_percent =0.6118595307244211
            avg_bzb_per_yeshuv =576.588596491228
            (-0.12555778346971486, 2.281133066301454e-33)
                        
         query_list = [ Query.Ppk_Above_X=250]
            num_kalfis_total =9015
            num_unique_yeshuvim =942
            total_bzb =5234609
            total_voters =3201839
            total_vote_percent =0.6116672706595659
            avg_bzb_per_yeshuv =580.6554631170271
            (-0.12193864737851318, 3.279412119513264e-31)
        
        
        query_list = [ Query.Ppk_Above_X=300]    
        num_kalfis_total =8886
        num_unique_yeshuvim =845
        total_bzb =5198919
        total_voters =3178665
        total_vote_percent =0.6114088332593757
        avg_bzb_per_yeshuv =585.0685347738015
        (-0.11955082877687018, 1.190816046692303e-29)
        
        
        
          query_list = [ Query.Ppk_Above_X=350]
            num_kalfis_total =8677
            num_unique_yeshuvim =706
            total_bzb =5130983
            total_voters =3131963
            total_vote_percent =0.610402139317164
            avg_bzb_per_yeshuv =591.3314509623142
            (-0.09347729997915177, 2.654657233332777e-18)
        
        
        query_list=[Query.No_Single_Kalfi]
            num_kalfis_total =8498
            num_unique_yeshuvim =391
            total_bzb =5013590
            total_voters =3042849
            total_vote_percent =0.6069201909210765
            avg_bzb_per_yeshuv =589.9729348081902
            (-0.030663111643890635, 0.004699873321591595)        
        
              
     query_list=[Query.No_Single_Kalfi, Query.Ppk_Above_X=200]             
        num_kalfis_total =8475
        num_unique_yeshuvim =390
        total_bzb =5010510
        total_voters =3041969
        total_vote_percent =0.6071176387234034
        avg_bzb_per_yeshuv =591.2106194690266
        (-0.06186309410041155, 1.20003540958646e-08)     
              
               
        query_list=[Query.No_Single_Kalfi, Query.Ppk_Above_X=250]
            num_kalfis_total =8463
            num_unique_yeshuvim =390
            total_bzb =5007765
            total_voters =3040785
            total_vote_percent =0.6072139966631821
            avg_bzb_per_yeshuv =591.7245657568238
            (-0.06963823233578181, 1.4251615048862298e-10)
            
            
            
        query_list=[Query.No_Single_Kalfi, Query.Ppk_Above_X=350]
            num_kalfis_total =8311
            num_unique_yeshuvim =340
            total_bzb =4960052
            total_voters =3008834
            total_vote_percent =0.60661339840792
            avg_bzb_per_yeshuv =596.8056792203105
            (-0.05238903616820668, 1.7652596354079995e-06)
        
        
        query_list=[Query.Above_Two_Kalfi]   
        num_kalfis_total =8172
        num_unique_yeshuvim =228
        total_bzb =4883566
        total_voters =2953670
        total_vote_percent =0.6048182823780819
        avg_bzb_per_yeshuv =597.5974057758199
        (0.032364285621494335, 0.0034332700675776574)
                
        query_list=[Query.Above_Two_Kalfi,  Query.Ppk_Above_X=250]   
        num_kalfis_total =8140
        num_unique_yeshuvim =228
        total_bzb =4878217
        total_voters =2951943
        total_vote_percent =0.605127447179984
        avg_bzb_per_yeshuv =599.2895577395577
        (-0.010479343916341035, 0.34448145284389237)
        
      query_list=[Query.Non arabs0]          
         num_kalfis_total =8274
        num_unique_yeshuvim =1022
        total_bzb =4665335
        total_voters =2902524
        total_vote_percent =0.6221469626511279
        avg_bzb_per_yeshuv =563.8548465071308
        (-0.09941692718877132, 1.2550844753044386e-19)
        
        
      query_list=[Query.Non_Arabs_Only, Query.No_Single_Kalfi]
      num_kalfis_total =7540
        num_unique_yeshuvim =288
        total_bzb =4409213
        total_voters =2719799
        total_vote_percent =0.6168445479952999
        avg_bzb_per_yeshuv =584.7762599469496
        (-0.019074395025435793, 0.09768814480216696)
        
        
        
          query_list=[Query.Non_Arabs_Only, Query.Kalfi_Above_X175]
        num_kalfis_total =8173
        num_unique_yeshuvim =942
        total_bzb =4652274
        total_voters =2895146
        total_vote_percent =0.6223077144639374
        avg_bzb_per_yeshuv =569.2247644683715
        (-0.13581060559084973, 6.00066348850279e-35)
        
        
        
        
       query_list=[Query.Non_Arabs_Only, Query.Kalfi_Above_X200]
       num_kalfis_total =8141
        num_unique_yeshuvim =911
        total_bzb =4646267
        total_voters =2890937
        total_vote_percent =0.6222063863312203
        avg_bzb_per_yeshuv =570.7243581869549
        (-0.13100401644278634, 1.7041670199889007e-32)
       
         
       query_list=[Query.Non_Arabs_Only, Query.Kalfi_Above_X250]  
               num_kalfis_total =8039
                num_unique_yeshuvim =820
                total_bzb =4623078
                total_voters =2875638
                total_vote_percent =0.6220180580989548
                avg_bzb_per_yeshuv =575.0812290085831
                (-0.12801731045151765, 1.0015559995515341e-30)   
        
        
       query_list=[Query.Non_Arabs_Only, Query.Kalfi_Above_350]          
            num_kalfis_total =7712
            num_unique_yeshuvim =592
            total_bzb =4522597
            total_voters =2806932
            total_vote_percent =0.6206460580060528
            avg_bzb_per_yeshuv =586.4363329875519
            (-0.09273139739407707, 3.3571519493114333e-16)

        
        query_list=[Query.Arabs_Only]
    num_kalfis_total =989
    num_unique_yeshuvim =134
    total_bzb =613650
    total_voters =327144
    total_vote_percent =0.5331117086286972
    avg_bzb_per_yeshuv =620.4752275025278
    (0.14744426480471204, 3.2164559400317513e-06)

        
        
       query_list=[Query.Arabs_Only, Query.Kalfi_Above_250]         
        num_kalfis_total =976
    num_unique_yeshuvim =122
    total_bzb =611531
    total_voters =326201
    total_vote_percent =0.5334169486093101
    avg_bzb_per_yeshuv =626.5686475409836
    (0.13680799802396626, 1.7970482720651136e-05)
        
        
        
        
        
        
        
        
        arabs only:
        non arabs only:
        
        
        
        3. BZB going down - less likeley to like govern parties?
        
        arabs:
        kalfi num / bzb  in arabs compared to non arabs yeshuvim
        
        
        
        
        
        
        FINDINGS:
        BIG:
        NON JEW:
        yeshuv types all of the big non jew ones
        the avg bzb jumped on between 20 to 21,22 elections
        drastic reduction in vote % in the same arab yeshuv types
        between 20 and 21.
                   
        avg bzb lowered between 21 to 22  and we saw increasing vote %
        might be negative corrleation between avg bzb and vote %
        
        
        BIG:
        JEW:
        jews big yeshuvs:
        very slight change to avg bzb between 18 to 19 but high increase in vote%
        
        we saw dramatic increase in vote% between election 19 to 20
        with very slight increasing to avg bzb = 
        so not even weak negative corrleation
        
        BUT
        we saw bigger increase in avg bzb between knesset 19 to 20
        and lower vote % all around big jews yeshuvs
            
        voting percent stay almost the same between 21 to 22 for jews
        
        
        
        HUGE cities:
        very steep increase in avg bzb - Jerusalem between 19 to 20
        leading to a steep decline in vote %
        
       general steady increase in avg bzb and decline in vote % is noted all around
       
       
       OTHERS
       Both in total data and kalfis above 250 ppl
       baduin and arab settelements have much higher avg bzb
       
       besides them  we can see a steep and steady increase over the years
       of avg bzb per kalfi in all small shapes of settlements,
       
       while in most settelemnets types its non an issue, since genereally the 
       avg bzb still very low compared to the bigger cities
       
       the avg bzb per kalfi in baduin and non jew villagers is much higher,
       combining this fact with the low vote %, high error rate in this settlements
       we might want to re think the number of kalfis in this yeshuvs
       
       
       
       as talked about in the media during the last elections there high steep in vote%
       in non jews yeshuvs,
       
       until now the high avg bzb per kalfis in this yeshuvs might not been an issue due to the low vote %
       but if the population with participate more and more the high bzb in the kalfi
       might turn to be a problem
       
       
       
        boxplot:
        
        120:667
        130:2598
        140:1439
        HUGE
        high numbers of ouitlers below min whisker in jeruslaem
        around 44-50 kalfis with very low voting percent %
        might be because of the non jew population
        the numbers of min outilers decarses: 49 -> 44 -> 40
        last 3 elections, fitting the increase in arab voting
        so in cae the outilers kalfis are for arabs pop it might make sense
        NO DATA ABOUT THE KALFIS IN ORDER TO  CHECK THAT OUT!??
        its possible to check, look at those kalfi vote percent
        and the kalfis with low look at arab parties voting
        
        
        BIG JEW
        Dramatic one time increase in kalfis with very low voting 
        in 50-100 during kneset 21, went down back again in 22.
        
        
        12 kalfis in 5-10 in kneseet 22 not good!
        out of 225
        the count:
        50-100:1366
        20-50:1518
        10-20:227
        5-10:255
        2-5:139
        
        
       BIG NON JEW
       high number of kalfis positive outiler 50-100 which is very few cities
       total of 189 kalfis and 15 kalfis in 21 elections were really positive!
       went back down in kneseet 22 but which kalfis where they?
       
       a lot of positive outliers in kneseet 21, suspicous ?
       23 kalfis out of the 359 kalfis in 10-20 arab
       5 kalfis out of 380 in kalfis 20-50
       
       
       
       50-100 arab:189
        20-50 arab:380
        10-20 arab:359
        5-10 arab:170
        2-5 arab :69
        
        
        other
        kalfi num
        319:450
        20-50 arab:45
        10-20 arab:305
        5-10 arab:71
        2-5 arab :107
        2-5 arab :35
        2-5 arab :47
