Shallow Neural Networks for Mushrooms

- Name
Junghwan Kim

- Description
I converted the original dataset which is agaricus-lepiota.data into three files: training.txt for network training, val.txt for validation, and testing.txt for network testing.
	training: 75.0%
	val: 12.5%
	testing: 12.5%
	training + val + testing = 100%
I implemented formulas.py to offer math formulas such as Sigmoid function, Derivative of neural activation function, Squared error function, and Derivative of squared error function.
I wrote models.py to implement two functions which are evaluation function and backpropagation function. The evaluation function will get input and compute the output of layer nodes. The backpropagation function will update weights using derivative of neural activation function with learning rate.
I also wrote proj_test.py to initialize layers and evaluate it. And it will run error function.

- How to run
This project requires Python 2 and numpy.
To run my project, input the below command:
	python proj_test.py
Do not use Python 3. It will occur error.

- Result
Error percentage on training set: 0.01396
Error percentage on validation set: 0.00006
Error percentage on testing set: 0.02

- Output -------------------------------------
Last login: Sat Dec 12 13:58:36 on ttys000
jkim@jKim-MacBook source % python proj_test.py
Parsing the training dataset...
Begining training the neural network:
Current iteration: 0
Current error: 0.440266217756

Current iteration: 1
Current error: 0.426714862041

Current iteration: 2
Current error: 0.41072294061

Current iteration: 3
Current error: 0.39220664621

Current iteration: 4
Current error: 0.37105230011

Current iteration: 5
Current error: 0.347474477253

Current iteration: 6
Current error: 0.32182827161

Current iteration: 7
Current error: 0.294566644477

Current iteration: 8
Current error: 0.266584496084

Current iteration: 9
Current error: 0.238516216366

Current iteration: 10
Current error: 0.0612661622484

Current iteration: 11
Current error: 0.225211084856

Current iteration: 12
Current error: 0.198622035009

Current iteration: 13
Current error: 0.173768010077

Current iteration: 14
Current error: 0.151133051374

Current iteration: 15
Current error: 0.119256657689

Current iteration: 16
Current error: 0.148976067072

Current iteration: 17
Current error: 0.129031920907

Current iteration: 18
Current error: 0.111511509413

Current iteration: 19
Current error: 0.096375403901

Current iteration: 20
Current error: 0.0833945808149

Current iteration: 21
Current error: 0.0723377498794

Current iteration: 22
Current error: 0.0629433982002

Current iteration: 23
Current error: 0.0549631430789

Current iteration: 24
Current error: 0.0481952804812

Current iteration: 25
Current error: 0.0424407514641

Current iteration: 26
Current error: 0.0375423293233

Current iteration: 27
Current error: 0.0333456968515

Current iteration: 28
Current error: 0.0297464162713

Current iteration: 29
Current error: 0.0266619811567

Current iteration: 30
Current error: 0.0239847356995

Current iteration: 31
Current error: 0.021653005414

Current iteration: 32
Current error: 0.0196204810895

Current iteration: 33
Current error: 0.0178479260436

Current iteration: 34
Current error: 0.0162845569722

Current iteration: 35
Current error: 0.0149077629185

Current iteration: 36
Current error: 0.0136855675346

Current iteration: 37
Current error: 0.0126002110999

Current iteration: 38
Current error: 0.0116356716756

Current iteration: 39
Current error: 0.0107691953001

Current iteration: 40
Current error: 0.00998903452753

Current iteration: 41
Current error: 0.00929331916669

Current iteration: 42
Current error: 0.00865963702233

Current iteration: 43
Current error: 0.00808441653522

Current iteration: 44
Current error: 0.00756717666676

Current iteration: 45
Current error: 0.00709108442976

Current iteration: 46
Current error: 0.00665997854731

Current iteration: 47
Current error: 0.00626634096032

Current iteration: 48
Current error: 0.397235688125

Current iteration: 49
Current error: 0.00942243894767

Current iteration: 50
Current error: 0.00877903403774

Current iteration: 51
Current error: 0.00819381132008

Current iteration: 52
Current error: 0.00766799913808

Current iteration: 53
Current error: 0.00718224788046

Current iteration: 54
Current error: 0.00674452679357

Current iteration: 55
Current error: 0.00634016280621

Current iteration: 56
Current error: 0.00597271346414

Current iteration: 57
Current error: 0.00563484789577

Current iteration: 58
Current error: 0.00532655319721

Current iteration: 59
Current error: 0.00503495748228

Current iteration: 60
Current error: 0.00477145889798

Current iteration: 61
Current error: 0.00452517321674

Current iteration: 62
Current error: 0.00429817887063

Current iteration: 63
Current error: 0.00408604140912

Current iteration: 64
Current error: 0.00389020578778

Current iteration: 65
Current error: 0.00370807327584

Current iteration: 66
Current error: 0.00353582996306

Current iteration: 67
Current error: 0.00337673097186

Current iteration: 68
Current error: 0.00322735280657

Current iteration: 69
Current error: 0.00308700135205

Current iteration: 70
Current error: 0.00295741474157

Current iteration: 71
Current error: 0.00283264223524

Current iteration: 72
Current error: 0.00271793650713

Current iteration: 73
Current error: 0.00260756484997

Current iteration: 74
Current error: 0.00250526049038

Current iteration: 75
Current error: 0.00241004929514

Current iteration: 76
Current error: 0.00231821506097

Current iteration: 77
Current error: 0.00223072154178

Current iteration: 78
Current error: 0.0021499004838

Current iteration: 79
Current error: 0.00207108658699

Current iteration: 80
Current error: 0.00199801707465

Current iteration: 81
Current error: 0.00192814354218

Current iteration: 82
Current error: 0.00186214171194

Current iteration: 83
Current error: 0.00179922945401

Current iteration: 84
Current error: 0.00174015306787

Current iteration: 85
Current error: 0.00168248320009

Current iteration: 86
Current error: 0.00162834392467

Current iteration: 87
Current error: 0.00157692968554

Current iteration: 88
Current error: 0.00152723659498

Current iteration: 89
Current error: 0.00148079999953

Current iteration: 90
Current error: 0.00143563400963

Current iteration: 91
Current error: 0.00139175083047

Current iteration: 92
Current error: 0.00135106612004

Current iteration: 93
Current error: 0.00131186822098

Current iteration: 94
Current error: 0.00127384577419

Current iteration: 95
Current error: 0.00123793753609

Current iteration: 96
Current error: 0.00120441053538

Current iteration: 97
Current error: 0.00117055338916

Current iteration: 98
Current error: 0.4534036363

Current iteration: 99
Current error: 0.00195258426957

Current iteration: 100
Current error: 0.00188467020759

Current iteration: 101
Current error: 0.441460731457

Current iteration: 102
Current error: 0.00307735374102

Current iteration: 103
Current error: 0.00294510140528

Current iteration: 104
Current error: 0.00282309565535

Current iteration: 105
Current error: 0.00270775634672

Current iteration: 106
Current error: 0.00259889324093

Current iteration: 107
Current error: 0.00249718438065

Current iteration: 108
Current error: 0.00240036054502

Current iteration: 109
Current error: 0.00230889855831

Current iteration: 110
Current error: 0.00222315543695

Current iteration: 111
Current error: 0.0021420961809

Current iteration: 112
Current error: 0.00206511462563

Current iteration: 113
Current error: 0.00199227627495

Current iteration: 114
Current error: 0.439915668734

Current iteration: 115
Current error: 0.00324000338586

Current iteration: 116
Current error: 0.424343213625

Current iteration: 117
Current error: 0.00512317039213

Current iteration: 118
Current error: 0.00484990934857

Current iteration: 119
Current error: 0.00459884796419

Current iteration: 120
Current error: 0.00436783236212

Current iteration: 121
Current error: 0.00414955204756

Current iteration: 122
Current error: 0.0039498734633

Current iteration: 123
Current error: 0.00376155895849

Current iteration: 124
Current error: 0.00358733576135

Current iteration: 125
Current error: 0.00342532020528

Current iteration: 126
Current error: 0.00327286155446

Current iteration: 127
Current error: 0.00313115668805

Current iteration: 128
Current error: 0.00299573306924

Current iteration: 129
Current error: 0.427091843914

Current iteration: 130
Current error: 0.00476017458475

Current iteration: 131
Current error: 0.00451514872944

Current iteration: 132
Current error: 0.00428843732907

Current iteration: 133
Current error: 0.413752136892

Current iteration: 134
Current error: 0.00664729325027

Current iteration: 135
Current error: 0.00625461832265

Current iteration: 136
Current error: 0.00589320208493

Current iteration: 137
Current error: 0.00555977116394

Current iteration: 138
Current error: 0.00525466769756

Current iteration: 139
Current error: 0.00497323037251

Current iteration: 140
Current error: 0.0047127564427

Current iteration: 141
Current error: 0.00447063697727

Current iteration: 142
Current error: 0.004248252447

Current iteration: 143
Current error: 0.00404000861859

Current iteration: 144
Current error: 0.00384789932914

Current iteration: 145
Current error: 0.00366703471655

Current iteration: 146
Current error: 0.00349845019899

Current iteration: 147
Current error: 0.0033416353377

Current iteration: 148
Current error: 0.00319438830983

Current iteration: 149
Current error: 0.00305646449083

Current iteration: 150
Current error: 0.00292756105576

Current iteration: 151
Current error: 0.00280826251946

Current iteration: 152
Current error: 0.00269228758276

Current iteration: 153
Current error: 0.00258443355385

Current iteration: 154
Current error: 0.00248292576771

Current iteration: 155
Current error: 0.0023890035492

Current iteration: 156
Current error: 0.434505566485

Current iteration: 157
Current error: 0.00384554715523

Current iteration: 158
Current error: 0.00366572917692

Current iteration: 159
Current error: 0.00349652893409

Current iteration: 160
Current error: 0.00334000492168

Current iteration: 161
Current error: 0.00319284973252

Current iteration: 162
Current error: 0.00305531029948

Current iteration: 163
Current error: 0.00292742654391

Current iteration: 164
Current error: 0.00280593669389

Current iteration: 165
Current error: 0.429325593454

Current iteration: 166
Current error: 0.00447749736357

Current iteration: 167
Current error: 0.00425348909687

Current iteration: 168
Current error: 0.00404335378717

Current iteration: 169
Current error: 0.00385055240743

Current iteration: 170
Current error: 0.00366988679139

Current iteration: 171
Current error: 0.00350079104481

Current iteration: 172
Current error: 0.00334348499063

Current iteration: 173
Current error: 0.00319699488518

Current iteration: 174
Current error: 0.00305924511719

Current iteration: 175
Current error: 0.00292940581485

Current iteration: 176
Current error: 0.00280790336095

Current iteration: 177
Current error: 0.00269350751755

Current iteration: 178
Current error: 0.00258741603039

Current iteration: 179
Current error: 0.00248439733867

Current iteration: 180
Current error: 0.00238850400973

Current iteration: 181
Current error: 0.00229875237425

Current iteration: 182
Current error: 0.00221345696833

Current iteration: 183
Current error: 0.00213187599917

Current iteration: 184
Current error: 0.00205521154799

Current iteration: 185
Current error: 0.0019834817734

Current iteration: 186
Current error: 0.00191379293485

Current iteration: 187
Current error: 0.00184901799714

Current iteration: 188
Current error: 0.00178642372308

Current iteration: 189
Current error: 0.00172677938958

Current iteration: 190
Current error: 0.00167080807067

Current iteration: 191
Current error: 0.444729837961

Current iteration: 192
Current error: 0.00274232381035

Current iteration: 193
Current error: 0.00263307605037

Current iteration: 194
Current error: 0.43140157087

Current iteration: 195
Current error: 0.00421742372164

Current iteration: 196
Current error: 0.00400997744398

Current iteration: 197
Current error: 0.00381871063297

Current iteration: 198
Current error: 0.00364037644489

Current iteration: 199
Current error: 0.420116787677

Current iteration: 200
Current error: 0.00570942880252

Current iteration: 201
Current error: 0.00539202931171

Current iteration: 202
Current error: 0.00510050265705

Current iteration: 203
Current error: 0.00483095063674

Current iteration: 204
Current error: 0.00458002713985

Current iteration: 205
Current error: 0.00434876272477

Current iteration: 206
Current error: 0.00413322896015

Current iteration: 207
Current error: 0.00393405328694

Current iteration: 208
Current error: 0.00374848396572

Current iteration: 209
Current error: 0.00357366018993

Current iteration: 210
Current error: 0.00341197878232

Current iteration: 211
Current error: 0.00326113892718

Current iteration: 212
Current error: 0.00311928586842

Current iteration: 213
Current error: 0.00298621225438

Current iteration: 214
Current error: 0.0028609285865

Current iteration: 215
Current error: 0.00274494564441

Current iteration: 216
Current error: 0.00263383499298

Current iteration: 217
Current error: 0.00253016703307

Current iteration: 218
Current error: 0.00243097422003

Current iteration: 219
Current error: 0.0023381116962

Current iteration: 220
Current error: 0.00225028456964

Current iteration: 221
Current error: 0.00216760088677

Current iteration: 222
Current error: 0.0020896285295

Current iteration: 223
Current error: 0.00201419091409

Current iteration: 224
Current error: 0.00194400761831

Current iteration: 225
Current error: 0.00187687113282

Current iteration: 226
Current error: 0.441570398194

Current iteration: 227
Current error: 0.00306305471764

Current iteration: 228
Current error: 0.00293352100599

Current iteration: 229
Current error: 0.00281167137367

Current iteration: 230
Current error: 0.00269709207131

Current iteration: 231
Current error: 0.00258924861252

Current iteration: 232
Current error: 0.00248780426996

Current iteration: 233
Current error: 0.00239240843932

Current iteration: 234
Current error: 0.00230120504862

Current iteration: 235
Current error: 0.00221652847374

Current iteration: 236
Current error: 0.0021355936067

Current iteration: 237
Current error: 0.00205794816248

Current iteration: 238
Current error: 0.00198585779113

Current iteration: 239
Current error: 0.00191640443502

Current iteration: 240
Current error: 0.00185051664383

Current iteration: 241
Current error: 0.00178815967791

Current iteration: 242
Current error: 0.00172923463629

Current iteration: 243
Current error: 0.00167281284914

Current iteration: 244
Current error: 0.00161891029796

Current iteration: 245
Current error: 0.00156820352787

Current iteration: 246
Current error: 0.00151885077479

Current iteration: 247
Current error: 0.447206760161

Current iteration: 248
Current error: 0.00250438311482

Current iteration: 249
Current error: 0.00240767604603

Current iteration: 250
Current error: 0.00231755072399

Current iteration: 251
Current error: 0.00222990559901

Current iteration: 252
Current error: 0.00215021399988

Current iteration: 253
Current error: 0.00207087848369

Current iteration: 254
Current error: 0.00199688185073

Current iteration: 255
Current error: 0.00192763404391

Current iteration: 256
Current error: 0.00186217239289

Current iteration: 257
Current error: 0.00179866201075

Current iteration: 258
Current error: 0.00173921648137

Current iteration: 259
Current error: 0.00168206169031

Current iteration: 260
Current error: 0.00162760153012

Current iteration: 261
Current error: 0.0015759487749

Current iteration: 262
Current error: 0.00152639584491

Current iteration: 263
Current error: 0.00148057426178

Current iteration: 264
Current error: 0.00143496390604

Current iteration: 265
Current error: 0.0013923610613

Current iteration: 266
Current error: 0.00135160781817

Current iteration: 267
Current error: 0.00131151519079

Current iteration: 268
Current error: 0.00127407508071

Current iteration: 269
Current error: 0.00123733700878

Current iteration: 270
Current error: 0.00120277796799

Current iteration: 271
Current error: 0.00117035313756

Current iteration: 272
Current error: 0.00113825054961

Current iteration: 273
Current error: 0.0011071495328

Current iteration: 274
Current error: 0.0010780421219

Current iteration: 275
Current error: 0.001049553188

Current iteration: 276
Current error: 0.00102275361514

Current iteration: 277
Current error: 0.000996994449012

Current iteration: 278
Current error: 0.000971256532834

Current iteration: 279
Current error: 0.000946972657455

Current iteration: 280
Current error: 0.000923552680923

Current iteration: 281
Current error: 0.000901174441277

Current iteration: 282
Current error: 0.000879580533301

Current iteration: 283
Current error: 0.000858922456779

Current iteration: 284
Current error: 0.000838679534849

Current iteration: 285
Current error: 0.000818697806798

Current iteration: 286
Current error: 0.000800129748994

Current iteration: 287
Current error: 0.000781791138842

Current iteration: 288
Current error: 0.000764224074354

Current iteration: 289
Current error: 0.000746981891259

Current iteration: 290
Current error: 0.000730651152539

Current iteration: 291
Current error: 0.000714675235525

Current iteration: 292
Current error: 0.000699219415203

Current iteration: 293
Current error: 0.463683199641

Current iteration: 294
Current error: 0.00118950059099

Current iteration: 295
Current error: 0.0011568838677

Current iteration: 296
Current error: 0.00112569231126

Current iteration: 297
Current error: 0.00109578679514

Current iteration: 298
Current error: 0.0010666090283

Current iteration: 299
Current error: 0.00103933099445

Current iteration: 300
Current error: 0.00101196569606

Current iteration: 301
Current error: 0.00098625634991

Current iteration: 302
Current error: 0.000961356457939

Current iteration: 303
Current error: 0.000937814847591

Current iteration: 304
Current error: 0.000914409105372

Current iteration: 305
Current error: 0.000892490618304

Current iteration: 306
Current error: 0.000871161955397

Current iteration: 307
Current error: 0.000850846184176

Current iteration: 308
Current error: 0.000830504550285

Current iteration: 309
Current error: 0.460521915814

Current iteration: 310
Current error: 0.00140432532117

Current iteration: 311
Current error: 0.00136195577759

Current iteration: 312
Current error: 0.00132275685992

Current iteration: 313
Current error: 0.00128431231332

Current iteration: 314
Current error: 0.00124812979319

Current iteration: 315
Current error: 0.00121256368524

Current iteration: 316
Current error: 0.00118003656446

Current iteration: 317
Current error: 0.00114707130119

Current iteration: 318
Current error: 0.00111604150959

Current iteration: 319
Current error: 0.00108673787657

Current iteration: 320
Current error: 0.455049089547

Current iteration: 321
Current error: 0.00181907803754

Current iteration: 322
Current error: 0.00175746502439

Current iteration: 323
Current error: 0.00170021629429

Current iteration: 324
Current error: 0.00164489326994

Current iteration: 325
Current error: 0.00159237905569

Current iteration: 326
Current error: 0.00154246756955

Current iteration: 327
Current error: 0.00149475773349

Current iteration: 328
Current error: 0.00144900070113

Current iteration: 329
Current error: 0.00140560833599

Current iteration: 330
Current error: 0.0013635696781

Current iteration: 331
Current error: 0.0013248111386

Current iteration: 332
Current error: 0.00128545599812

Current iteration: 333
Current error: 0.00124881885124

Current iteration: 334
Current error: 0.00121400742398

Current iteration: 335
Current error: 0.00118013775679

Current iteration: 336
Current error: 0.00114805841034

Current iteration: 337
Current error: 0.00111702691455

Current iteration: 338
Current error: 0.00108724499805

Current iteration: 339
Current error: 0.00105866352112

Current iteration: 340
Current error: 0.00103122914971

Current iteration: 341
Current error: 0.00100492165481

Current iteration: 342
Current error: 0.000979489294271

Current iteration: 343
Current error: 0.000954876608529

Current iteration: 344
Current error: 0.000931376494062

Current iteration: 345
Current error: 0.458272136673

Current iteration: 346
Current error: 0.0015679223739

Current iteration: 347
Current error: 0.00151891158277

Current iteration: 348
Current error: 0.00147176843761

Current iteration: 349
Current error: 0.00142753353207

Current iteration: 350
Current error: 0.00138506849343

Current iteration: 351
Current error: 0.00134371395572

Current iteration: 352
Current error: 0.00130522126523

Current iteration: 353
Current error: 0.450900924653

Current iteration: 354
Current error: 0.00216676276035

Current iteration: 355
Current error: 0.00208890625991

Current iteration: 356
Current error: 0.00201477967317

Current iteration: 357
Current error: 0.00194356582976

Current iteration: 358
Current error: 0.00187691901882

Current iteration: 359
Current error: 0.00181301287059

Current iteration: 360
Current error: 0.00175275231005

Current iteration: 361
Current error: 0.0016951524815

Current iteration: 362
Current error: 0.00164061677949

Current iteration: 363
Current error: 0.00158767019881

Current iteration: 364
Current error: 0.00153902924055

Current iteration: 365
Current error: 0.00149081159123

Current iteration: 366
Current error: 0.00144497131412

Current iteration: 367
Current error: 0.00140174546667

Current iteration: 368
Current error: 0.00136045714425

Current iteration: 369
Current error: 0.00132059125598

Current iteration: 370
Current error: 0.00128249363849

Current iteration: 371
Current error: 0.00124633317035

Current iteration: 372
Current error: 0.00121131334607

Current iteration: 373
Current error: 0.0011780455418

Current iteration: 374
Current error: 0.00114562418873

Current iteration: 375
Current error: 0.00111474591521

Current iteration: 376
Current error: 0.00108512444742

Current iteration: 377
Current error: 0.00105662422995

Current iteration: 378
Current error: 0.00102917845468

Current iteration: 379
Current error: 0.00100244579741

Current iteration: 380
Current error: 0.000977042684458

Current iteration: 381
Current error: 0.000952989571242

Current iteration: 382
Current error: 0.000929322622719

Current iteration: 383
Current error: 0.000906591249045

Current iteration: 384
Current error: 0.000884785658898

Current iteration: 385
Current error: 0.000863899347923

Current iteration: 386
Current error: 0.000842925942308

Current iteration: 387
Current error: 0.000823545466518

Current iteration: 388
Current error: 0.00080441315139

Current iteration: 389
Current error: 0.00078628714782

Current iteration: 390
Current error: 0.000768657257353

Current iteration: 391
Current error: 0.000751022109243

Current iteration: 392
Current error: 0.000734407498127

Current iteration: 393
Current error: 0.000718659103582

Current iteration: 394
Current error: 0.000703082157504

Current iteration: 395
Current error: 0.000687926986916

Current iteration: 396
Current error: 0.000673070985698

Current iteration: 397
Current error: 0.000659362101025

Current iteration: 398
Current error: 0.000645479801194

Current iteration: 399
Current error: 0.000632212453209

Current iteration: 400
Current error: 0.000619351801462

Current iteration: 401
Current error: 0.000606907760219

Current iteration: 402
Current error: 0.000595005835997

Current iteration: 403
Current error: 0.466422497419

Current iteration: 404
Current error: 0.00101691269748

Current iteration: 405
Current error: 0.000990928825721

Current iteration: 406
Current error: 0.000965871698752

Current iteration: 407
Current error: 0.000941923406455

Current iteration: 408
Current error: 0.000918650932698

Current iteration: 409
Current error: 0.000896540305606

Current iteration: 410
Current error: 0.000874790161392

Current iteration: 411
Current error: 0.000854155513687

Current iteration: 412
Current error: 0.000833871972805

Current iteration: 413
Current error: 0.000814750555752

Current iteration: 414
Current error: 0.000795766892623

Current iteration: 415
Current error: 0.000777914503554

Current iteration: 416
Current error: 0.000760357671678

Current iteration: 417
Current error: 0.000743305664629

Current iteration: 418
Current error: 0.000727158959058

Current iteration: 419
Current error: 0.000711696038233

Current iteration: 420
Current error: 0.00069592610293

Current iteration: 421
Current error: 0.000681125947165

Current iteration: 422
Current error: 0.00066675444553

Current iteration: 423
Current error: 0.00065279946495

Current iteration: 424
Current error: 0.00063991411906

Current iteration: 425
Current error: 0.000626249955009

Current iteration: 426
Current error: 0.000613565942546

Current iteration: 427
Current error: 0.000601484622221

Current iteration: 428
Current error: 0.00058922121187

Current iteration: 429
Current error: 0.000578084535961

Current iteration: 430
Current error: 0.000566392369282

Current iteration: 431
Current error: 0.000555475684817

Current iteration: 432
Current error: 0.000544983554135

Current iteration: 433
Current error: 0.000534904961575

Current iteration: 434
Current error: 0.000524484358755

Current iteration: 435
Current error: 0.000515109627363

Current iteration: 436
Current error: 0.000505514899247

Current iteration: 437
Current error: 0.000495984495759

Current iteration: 438
Current error: 0.000486987329415

Current iteration: 439
Current error: 0.000478470331085

Current iteration: 440
Current error: 0.000469639900271

Current iteration: 441
Current error: 0.000461517459303

Current iteration: 442
Current error: 0.000453378563232

Current iteration: 443
Current error: 0.000445548844132

Current iteration: 444
Current error: 0.000437737610479

Current iteration: 445
Current error: 0.000430628773721

Current iteration: 446
Current error: 0.000423151579573

Current iteration: 447
Current error: 0.000416043897828

Current iteration: 448
Current error: 0.000408957713362

Current iteration: 449
Current error: 0.000402316191806

Current iteration: 450
Current error: 0.00039568564421

Current iteration: 451
Current error: 0.00038929348232

Current iteration: 452
Current error: 0.000382753355521

Current iteration: 453
Current error: 0.000376807916576

Current iteration: 454
Current error: 0.000370864936211

Current iteration: 455
Current error: 0.000365332552488

Current iteration: 456
Current error: 0.000359266097351

Current iteration: 457
Current error: 0.000353754074678

Current iteration: 458
Current error: 0.000348329066423

Current iteration: 459
Current error: 0.000342973935556

Current iteration: 460
Current error: 0.000338007610743

Current iteration: 461
Current error: 0.000332550974436

Current iteration: 462
Current error: 0.000327626904027

Current iteration: 463
Current error: 0.00032291807856

Current iteration: 464
Current error: 0.000317909701689

Current iteration: 465
Current error: 0.000313404645968

Current iteration: 466
Current error: 0.000308716403674

Current iteration: 467
Current error: 0.000304359553606

Current iteration: 468
Current error: 0.000300042361115

Current iteration: 469
Current error: 0.000295778390133

Current iteration: 470
Current error: 0.000291464613148

Current iteration: 471
Current error: 0.000287430426262

Current iteration: 472
Current error: 0.000283458437353

Current iteration: 473
Current error: 0.000279614699563

Current iteration: 474
Current error: 0.000275597586542

Current iteration: 475
Current error: 0.476943412893

Current iteration: 476
Current error: 0.000480740967737

Current iteration: 477
Current error: 0.000472238550939

Current iteration: 478
Current error: 0.00046381613147

Current iteration: 479
Current error: 0.000455680944138

Current iteration: 480
Current error: 0.000447657897137

Current iteration: 481
Current error: 0.000439983101744

Current iteration: 482
Current error: 0.000432540898835

Current iteration: 483
Current error: 0.000425070732305

Current iteration: 484
Current error: 0.000418012339742

Current iteration: 485
Current error: 0.000411238254941

Current iteration: 486
Current error: 0.000404163657293

Current iteration: 487
Current error: 0.000397590885746

Current iteration: 488
Current error: 0.00039099118228

Current iteration: 489
Current error: 0.000384850179884

Current iteration: 490
Current error: 0.000378489329492

Current iteration: 491
Current error: 0.00037253260024

Current iteration: 492
Current error: 0.000366755414489

Current iteration: 493
Current error: 0.000360980453886

Current iteration: 494
Current error: 0.000355344484325

Current iteration: 495
Current error: 0.000349864177554

Current iteration: 496
Current error: 0.000344524212799

Current iteration: 497
Current error: 0.00033910938937

Current iteration: 498
Current error: 0.000334108894983

Current iteration: 499
Current error: 0.000329034927539

Current iteration: 500
Current error: 0.000324167442783

Current iteration: 501
Current error: 0.00031972037912

Current iteration: 502
Current error: 0.000314650728443

Current iteration: 503
Current error: 0.000310115341432

Current iteration: 504
Current error: 0.000305549050656

Current iteration: 505
Current error: 0.000301327162297

Current iteration: 506
Current error: 0.475922235769

Current iteration: 507
Current error: 0.000524276598739

Current iteration: 508
Current error: 0.000514449218959

Current iteration: 509
Current error: 0.000505166878702

Current iteration: 510
Current error: 0.000495809433918

Current iteration: 511
Current error: 0.000486928247372

Current iteration: 512
Current error: 0.000478092026902

Current iteration: 513
Current error: 0.000469559677795

Current iteration: 514
Current error: 0.000461278834383

Current iteration: 515
Current error: 0.000453275901808

Current iteration: 516
Current error: 0.000445352665487

Current iteration: 517
Current error: 0.470833959203

Current iteration: 518
Current error: 0.000767741890287

Current iteration: 519
Current error: 0.000750616901951

Current iteration: 520
Current error: 0.000733943108231

Current iteration: 521
Current error: 0.000718140160321

Current iteration: 522
Current error: 0.000702354821247

Current iteration: 523
Current error: 0.00068740794116

Current iteration: 524
Current error: 0.000672812949424

Current iteration: 525
Current error: 0.000658673727769

Current iteration: 526
Current error: 0.000645007485333

Current iteration: 527
Current error: 0.000631659467583

Current iteration: 528
Current error: 0.00061895615373

Current iteration: 529
Current error: 0.000606577067376

Current iteration: 530
Current error: 0.000594397274073

Current iteration: 531
Current error: 0.000582726140073

Current iteration: 532
Current error: 0.000571389833358

Current iteration: 533
Current error: 0.000560115112547

Current iteration: 534
Current error: 0.000549818099669

Current iteration: 535
Current error: 0.000538928607426

Current iteration: 536
Current error: 0.000528641040384

Current iteration: 537
Current error: 0.000518930214016

Current iteration: 538
Current error: 0.000509227482923

Current iteration: 539
Current error: 0.000500032104914

Current iteration: 540
Current error: 0.00049083420828

Current iteration: 541
Current error: 0.000481926638213

Current iteration: 542
Current error: 0.000473195468453

Current iteration: 543
Current error: 0.000464905537331

Current iteration: 544
Current error: 0.000456629568948

Current iteration: 545
Current error: 0.47047377521

Current iteration: 546
Current error: 0.000786895014731

Current iteration: 547
Current error: 0.000768940061671

Current iteration: 548
Current error: 0.000751927590572

Current iteration: 549
Current error: 0.000735200757466

Current iteration: 550
Current error: 0.462762240352

Current iteration: 551
Current error: 0.00124848336122

Current iteration: 552
Current error: 0.00121349592027

Current iteration: 553
Current error: 0.00118010038737

Current iteration: 554
Current error: 0.00114799013849

Current iteration: 555
Current error: 0.00111660691792

Current iteration: 556
Current error: 0.00108661088412

Current iteration: 557
Current error: 0.00105826454674

Current iteration: 558
Current error: 0.455616083823

Current iteration: 559
Current error: 0.00177370931237

Current iteration: 560
Current error: 0.00171453435547

Current iteration: 561
Current error: 0.0016585851688

Current iteration: 562
Current error: 0.00160595052844

Current iteration: 563
Current error: 0.00155491642899

Current iteration: 564
Current error: 0.0015071850372

Current iteration: 565
Current error: 0.00146097567035

Current iteration: 566
Current error: 0.00141627409676

Current iteration: 567
Current error: 0.00137391399078

Current iteration: 568
Current error: 0.00133338208667

Current iteration: 569
Current error: 0.00129533215923

Current iteration: 570
Current error: 0.00125873304

Current iteration: 571
Current error: 0.00122261113379

Current iteration: 572
Current error: 0.00118943892625

Current iteration: 573
Current error: 0.0011559954254

Current iteration: 574
Current error: 0.00112507249762

Current iteration: 575
Current error: 0.0010950264503

Current iteration: 576
Current error: 0.00106609048899

Current iteration: 577
Current error: 0.00103838054141

Current iteration: 578
Current error: 0.00101115816762

Current iteration: 579
Current error: 0.000985668263347

Current iteration: 580
Current error: 0.000961056348569

Current iteration: 581
Current error: 0.000937407515727

Current iteration: 582
Current error: 0.000914163854836

Current iteration: 583
Current error: 0.000891739480462

Current iteration: 584
Current error: 0.00087073567202

Current iteration: 585
Current error: 0.000849934826924

Current iteration: 586
Current error: 0.000829940759262

Current iteration: 587
Current error: 0.000810984459013

Current iteration: 588
Current error: 0.000792159865547

Current iteration: 589
Current error: 0.461405666433

Current iteration: 590
Current error: 0.449529390051

Current iteration: 591
Current error: 0.00229002975792

Current iteration: 592
Current error: 0.00220503696907

Current iteration: 593
Current error: 0.00212457329445

Current iteration: 594
Current error: 0.00204861307256

Current iteration: 595
Current error: 0.00197560038632

Current iteration: 596
Current error: 0.00190684860453

Current iteration: 597
Current error: 0.00184260459686

Current iteration: 598
Current error: 0.00178045483673

Current iteration: 599
Current error: 0.0017216175606

Current iteration: 600
Current error: 0.443919481576

Current iteration: 601
Current error: 0.00282099282207

Current iteration: 602
Current error: 0.429108167638

Current iteration: 603
Current error: 0.00449885106301

Current iteration: 604
Current error: 0.00427397511392

Current iteration: 605
Current error: 0.00406381503792

Current iteration: 606
Current error: 0.415855674616

Current iteration: 607
Current error: 0.00632344335242

Current iteration: 608
Current error: 0.00595966393615

Current iteration: 609
Current error: 0.00562030618603

Current iteration: 610
Current error: 0.00530892623647

Current iteration: 611
Current error: 0.00502262909586

Current iteration: 612
Current error: 0.00475964376037

Current iteration: 613
Current error: 0.00451419028721

Current iteration: 614
Current error: 0.00428844010365

Current iteration: 615
Current error: 0.00407762010045

Current iteration: 616
Current error: 0.00388122903994

Current iteration: 617
Current error: 0.00369976661412

Current iteration: 618
Current error: 0.00352882289733

Current iteration: 619
Current error: 0.00337051965005

Current iteration: 620
Current error: 0.00322060638385

Current iteration: 621
Current error: 0.00308304210321

Current iteration: 622
Current error: 0.0029500914412

Current iteration: 623
Current error: 0.0028286594421

Current iteration: 624
Current error: 0.00271204865801

Current iteration: 625
Current error: 0.00260335756241

Current iteration: 626
Current error: 0.00250157803044

Current iteration: 627
Current error: 0.00240439908081

Current iteration: 628
Current error: 0.00231369092337

Current iteration: 629
Current error: 0.00222667101269

Current iteration: 630
Current error: 0.00214530436908

Current iteration: 631
Current error: 0.00206803927974

Current iteration: 632
Current error: 0.00199507960688

Current iteration: 633
Current error: 0.00192502379083

Current iteration: 634
Current error: 0.00185961304931

Current iteration: 635
Current error: 0.441817010256

Current iteration: 636
Current error: 0.00303513333329

Current iteration: 637
Current error: 0.00290797594223

Current iteration: 638
Current error: 0.00278724820656

Current iteration: 639
Current error: 0.00267401811443

Current iteration: 640
Current error: 0.00256764959257

Current iteration: 641
Current error: 0.00246761714207

Current iteration: 642
Current error: 0.0023725232387

Current iteration: 643
Current error: 0.00228312923682

Current iteration: 644
Current error: 0.00219813422015

Current iteration: 645
Current error: 0.00211850671065

Current iteration: 646
Current error: 0.438115922976

Current iteration: 647
Current error: 0.00343618508554

Current iteration: 648
Current error: 0.00328298073041

Current iteration: 649
Current error: 0.00313935068605

Current iteration: 650
Current error: 0.00300457171742

Current iteration: 651
Current error: 0.426981608992

Current iteration: 652
Current error: 0.00477233257217

Current iteration: 653
Current error: 0.00452614388884

Current iteration: 654
Current error: 0.411539870042

Current iteration: 655
Current error: 0.00698693344761

Current iteration: 656
Current error: 0.00656536296675

Current iteration: 657
Current error: 0.00617816546395

Current iteration: 658
Current error: 0.00582415876805

Current iteration: 659
Current error: 0.00549568915354

Current iteration: 660
Current error: 0.00519755599802

Current iteration: 661
Current error: 0.00491838457691

Current iteration: 662
Current error: 0.00466279852121

Current iteration: 663
Current error: 0.00442392500803

Current iteration: 664
Current error: 0.00420409824744

Current iteration: 665
Current error: 0.00399966127527

Current iteration: 666
Current error: 0.00380976473232

Current iteration: 667
Current error: 0.0036324759779

Current iteration: 668
Current error: 0.00346596704489

Current iteration: 669
Current error: 0.00331119192014

Current iteration: 670
Current error: 0.00316613959455

Current iteration: 671
Current error: 0.00302978954072

Current iteration: 672
Current error: 0.00290286392694

Current iteration: 673
Current error: 0.00278173175935

Current iteration: 674
Current error: 0.00266966608313

Current iteration: 675
Current error: 0.00256295933012

Current iteration: 676
Current error: 0.00246280478709

Current iteration: 677
Current error: 0.00236828484497

Current iteration: 678
Current error: 0.00227987573781

Current iteration: 679
Current error: 0.00219502718421

Current iteration: 680
Current error: 0.00211471821716

Current iteration: 681
Current error: 0.00203932326365

Current iteration: 682
Current error: 0.00196797941818

Current iteration: 683
Current error: 0.00189924014369

Current iteration: 684
Current error: 0.00183493560805

Current iteration: 685
Current error: 0.442206834061

Current iteration: 686
Current error: 0.00299741639834

Current iteration: 687
Current error: 0.00287226814285

Current iteration: 688
Current error: 0.00275359440115

Current iteration: 689
Current error: 0.00264298996672

Current iteration: 690
Current error: 0.00253842775477

Current iteration: 691
Current error: 0.00243909150877

Current iteration: 692
Current error: 0.00234597559386

Current iteration: 693
Current error: 0.435026763552

Current iteration: 694
Current error: 0.0037821684209

Current iteration: 695
Current error: 0.00360745140172

Current iteration: 696
Current error: 0.00344265444857

Current iteration: 697
Current error: 0.00328874431249

Current iteration: 698
Current error: 0.00314480880369

Current iteration: 699
Current error: 0.425392944955

Current iteration: 700
Current error: 0.00498119908631

Current iteration: 701
Current error: 0.00472030984168

Current iteration: 702
Current error: 0.00447870989199

Current iteration: 703
Current error: 0.00425437872129

Current iteration: 704
Current error: 0.00404642108509

Current iteration: 705
Current error: 0.00385253609132

Current iteration: 706
Current error: 0.00367248434687

Current iteration: 707
Current error: 0.00350364086727

Current iteration: 708
Current error: 0.00334618718827

Current iteration: 709
Current error: 0.0031987917396

Current iteration: 710
Current error: 0.0030609420216

Current iteration: 711
Current error: 0.00293218415763

Current iteration: 712
Current error: 0.00280956427935

Current iteration: 713
Current error: 0.00269478699263

Current iteration: 714
Current error: 0.00258744221272

Current iteration: 715
Current error: 0.00248573916839

Current iteration: 716
Current error: 0.00239049475136

Current iteration: 717
Current error: 0.0022997337414

Current iteration: 718
Current error: 0.00221468283577

Current iteration: 719
Current error: 0.00213302696922

Current iteration: 720
Current error: 0.00205629139372

Current iteration: 721
Current error: 0.00198365290585

Current iteration: 722
Current error: 0.00191563899636

Current iteration: 723
Current error: 0.00184923250466

Current iteration: 724
Current error: 0.00178747821869

Current iteration: 725
Current error: 0.00172789720495

Current iteration: 726
Current error: 0.00167157201269

Current iteration: 727
Current error: 0.00161878987329

Current iteration: 728
Current error: 0.00156621395036

Current iteration: 729
Current error: 0.00151842313761

Current iteration: 730
Current error: 0.00147171509076

Current iteration: 731
Current error: 0.00142694105099

Current iteration: 732
Current error: 0.00138412814971

Current iteration: 733
Current error: 0.00134379443792

Current iteration: 734
Current error: 0.00130398011505

Current iteration: 735
Current error: 0.00126678024165

Current iteration: 736
Current error: 0.00123073019948

Current iteration: 737
Current error: 0.00119695488974

Current iteration: 738
Current error: 0.00116414448003

Current iteration: 739
Current error: 0.00113204832683

Current iteration: 740
Current error: 0.00110198208747

Current iteration: 741
Current error: 0.00107264603637

Current iteration: 742
Current error: 0.00104437898622

Current iteration: 743
Current error: 0.0010177030522

Current iteration: 744
Current error: 0.000992270990163

Current iteration: 745
Current error: 0.000966478224655

Current iteration: 746
Current error: 0.000942582527216

Current iteration: 747
Current error: 0.000919258497413

Current iteration: 748
Current error: 0.000897065336065

Current iteration: 749
Current error: 0.459017635644

Current iteration: 750
Current error: 0.00151229500938

Current iteration: 751
Current error: 0.00146630496576

Current iteration: 752
Current error: 0.00142191822694

Current iteration: 753
Current error: 0.00137958656103

Current iteration: 754
Current error: 0.00133878954693

Current iteration: 755
Current error: 0.00129961137227

Current iteration: 756
Current error: 0.00126282720413

Current iteration: 757
Current error: 0.00122771492069

Current iteration: 758
Current error: 0.00119322566727

Current iteration: 759
Current error: 0.00116064125034

Current iteration: 760
Current error: 0.00112892935046

Current iteration: 761
Current error: 0.00109872282555

Current iteration: 762
Current error: 0.00106983896324

Current iteration: 763
Current error: 0.00104164582829

Current iteration: 764
Current error: 0.00101485620906

Current iteration: 765
Current error: 0.000988970705279

Current iteration: 766
Current error: 0.000964166999507

Current iteration: 767
Current error: 0.000939889477263

Current iteration: 768
Current error: 0.000916744292155

Current iteration: 769
Current error: 0.000894646539025

Current iteration: 770
Current error: 0.000873249743308

Current iteration: 771
Current error: 0.000852478578002

Current iteration: 772
Current error: 0.000832554616656

Current iteration: 773
Current error: 0.00081323302936

Current iteration: 774
Current error: 0.000794605505479

Current iteration: 775
Current error: 0.00077648716708

Current iteration: 776
Current error: 0.000758976012043

Current iteration: 777
Current error: 0.000742084152761

Current iteration: 778
Current error: 0.000725844629665

Current iteration: 779
Current error: 0.0007099762407

Current iteration: 780
Current error: 0.000694795502802

Current iteration: 781
Current error: 0.000680032830542

Current iteration: 782
Current error: 0.000665910505525

Current iteration: 783
Current error: 0.00065180653838

Current iteration: 784
Current error: 0.000638474542297

Current iteration: 785
Current error: 0.000625116495225

Current iteration: 786
Current error: 0.000612582330641

Current iteration: 787
Current error: 0.000600397870161

Current iteration: 788
Current error: 0.00058840007478

Current iteration: 789
Current error: 0.000576621984376

Current iteration: 790
Current error: 0.000565508661993

Current iteration: 791
Current error: 0.000554745141351

Current iteration: 792
Current error: 0.000543942018594

Current iteration: 793
Current error: 0.000533758117185

Current iteration: 794
Current error: 0.000523593462104

Current iteration: 795
Current error: 0.000513921416207

Current iteration: 796
Current error: 0.000504456827303

Current iteration: 797
Current error: 0.000495341378563

Current iteration: 798
Current error: 0.000486188703796

Current iteration: 799
Current error: 0.000477690217872

Current iteration: 800
Current error: 0.000468956854009

Current iteration: 801
Current error: 0.000460794147607

Current iteration: 802
Current error: 0.470340475616

Current iteration: 803
Current error: 0.000793369135196

Current iteration: 804
Current error: 0.000775735677775

Current iteration: 805
Current error: 0.000758299112433

Current iteration: 806
Current error: 0.000741761127971

Current iteration: 807
Current error: 0.000724966135234

Current iteration: 808
Current error: 0.000709637696404

Current iteration: 809
Current error: 0.000694125548648

Current iteration: 810
Current error: 0.000679288554136

Current iteration: 811
Current error: 0.000664880869914

Current iteration: 812
Current error: 0.000651191460144

Current iteration: 813
Current error: 0.464910902146

Current iteration: 814
Current error: 0.00110985937492

Current iteration: 815
Current error: 0.00108031390858

Current iteration: 816
Current error: 0.00105201153284

Current iteration: 817
Current error: 0.00102490689119

Current iteration: 818
Current error: 0.000998885962823

Current iteration: 819
Current error: 0.000973320683755

Current iteration: 820
Current error: 0.000949187330897

Current iteration: 821
Current error: 0.000925842115532

Current iteration: 822
Current error: 0.000903143210903

Current iteration: 823
Current error: 0.000881217445567

Current iteration: 824
Current error: 0.000860556785905

Current iteration: 825
Current error: 0.000840026971989

Current iteration: 826
Current error: 0.000820592408501

Current iteration: 827
Current error: 0.000801482005493

Current iteration: 828
Current error: 0.000783768164362

Current iteration: 829
Current error: 0.000765734006051

Current iteration: 830
Current error: 0.000748587563102

Current iteration: 831
Current error: 0.000732007871789

Current iteration: 832
Current error: 0.000716242864949

Current iteration: 833
Current error: 0.000700648134184

Current iteration: 834
Current error: 0.000685684574033

Current iteration: 835
Current error: 0.000670932961611

Current iteration: 836
Current error: 0.000657547987361

Current iteration: 837
Current error: 0.000643502538139

Current iteration: 838
Current error: 0.0006300878152

Current iteration: 839
Current error: 0.000617361361924

Current iteration: 840
Current error: 0.00060494669306

Current iteration: 841
Current error: 0.000592872305877

Current iteration: 842
Current error: 0.000581276613313

Current iteration: 843
Current error: 0.000569802696195

Current iteration: 844
Current error: 0.000558942402346

Current iteration: 845
Current error: 0.000548082131529

Current iteration: 846
Current error: 0.000537590953424

Current iteration: 847
Current error: 0.000527564564271

Current iteration: 848
Current error: 0.000517739493379

Current iteration: 849
Current error: 0.468621790154

Current iteration: 850
Current error: 0.458700245912

Current iteration: 851
Current error: 0.00153494492949

Current iteration: 852
Current error: 0.00148792301358

Current iteration: 853
Current error: 0.00144196272891

Current iteration: 854
Current error: 0.00139857183074

Current iteration: 855
Current error: 0.00135721228745

Current iteration: 856
Current error: 0.00131781702412

Current iteration: 857
Current error: 0.00128002576917

Current iteration: 858
Current error: 0.00124345183915

Current iteration: 859
Current error: 0.00120852476071

Current iteration: 860
Current error: 0.00117521853788

Current iteration: 861
Current error: 0.0011434294443

Current iteration: 862
Current error: 0.00111254566695

Current iteration: 863
Current error: 0.0010826633296

Current iteration: 864
Current error: 0.455108607477

Current iteration: 865
Current error: 0.00181244291546

Current iteration: 866
Current error: 0.44253661455

Current iteration: 867
Current error: 0.0029624840703

Current iteration: 868
Current error: 0.00284003752099

Current iteration: 869
Current error: 0.00272268855682

Current iteration: 870
Current error: 0.00261331996529

Current iteration: 871
Current error: 0.00251051044069

Current iteration: 872
Current error: 0.00241397677375

Current iteration: 873
Current error: 0.00232229444916

Current iteration: 874
Current error: 0.00223541422641

Current iteration: 875
Current error: 0.00215296464636

Current iteration: 876
Current error: 0.0020752642182

Current iteration: 877
Current error: 0.00200192708871

Current iteration: 878
Current error: 0.00193182870021

Current iteration: 879
Current error: 0.00186516851134

Current iteration: 880
Current error: 0.00180245106218

Current iteration: 881
Current error: 0.00174254331258

Current iteration: 882
Current error: 0.00168504394506

Current iteration: 883
Current error: 0.00163082144435

Current iteration: 884
Current error: 0.445337845532

Current iteration: 885
Current error: 0.00268022879754

Current iteration: 886
Current error: 0.00257374436766

Current iteration: 887
Current error: 0.00247371289464

Current iteration: 888
Current error: 0.00237763225465

Current iteration: 889
Current error: 0.00228861752882

Current iteration: 890
Current error: 0.00220334364361

Current iteration: 891
Current error: 0.00212250180096

Current iteration: 892
Current error: 0.438023551118

Current iteration: 893
Current error: 0.00344095874009

Current iteration: 894
Current error: 0.00328773080814

Current iteration: 895
Current error: 0.00314435668217

Current iteration: 896
Current error: 0.00301056811178

Current iteration: 897
Current error: 0.00288282336205

Current iteration: 898
Current error: 0.00276398554035

Current iteration: 899
Current error: 0.00265283819051

Current iteration: 900
Current error: 0.00254734303275

Current iteration: 901
Current error: 0.00244826448884

Current iteration: 902
Current error: 0.00235400950152

Current iteration: 903
Current error: 0.00226612980459

Current iteration: 904
Current error: 0.00218210591141

Current iteration: 905
Current error: 0.00210326341595

Current iteration: 906
Current error: 0.00202889899171

Current iteration: 907
Current error: 0.00195628102499

Current iteration: 908
Current error: 0.00188917617078

Current iteration: 909
Current error: 0.00182501441281

Current iteration: 910
Current error: 0.00176358337115

Current iteration: 911
Current error: 0.00170619516677

Current iteration: 912
Current error: 0.00164997494656

Current iteration: 913
Current error: 0.00159750909116

Current iteration: 914
Current error: 0.00154722179262

Current iteration: 915
Current error: 0.00149946215482

Current iteration: 916
Current error: 0.00145349797995

Current iteration: 917
Current error: 0.0014098235826

Current iteration: 918
Current error: 0.00136760073207

Current iteration: 919
Current error: 0.00132776449009

Current iteration: 920
Current error: 0.00128920430223

Current iteration: 921
Current error: 0.00125251493167

Current iteration: 922
Current error: 0.451839877171

Current iteration: 923
Current error: 0.00208394401075

Current iteration: 924
Current error: 0.00200976060096

Current iteration: 925
Current error: 0.00194082651537

Current iteration: 926
Current error: 0.00187321089394

Current iteration: 927
Current error: 0.00180929894961

Current iteration: 928
Current error: 0.00174859214505

Current iteration: 929
Current error: 0.00169166275396

Current iteration: 930
Current error: 0.00163726117366

Current iteration: 931
Current error: 0.00158481874015

Current iteration: 932
Current error: 0.00153539348741

Current iteration: 933
Current error: 0.0014879674901

Current iteration: 934
Current error: 0.00144228642575

Current iteration: 935
Current error: 0.00139898008409

Current iteration: 936
Current error: 0.00135772518533

Current iteration: 937
Current error: 0.00131811788895

Current iteration: 938
Current error: 0.00128019368353

Current iteration: 939
Current error: 0.00124460565507

Current iteration: 940
Current error: 0.00120860356932

Current iteration: 941
Current error: 0.00117593789085

Current iteration: 942
Current error: 0.453306467317

Current iteration: 943
Current error: 0.00196124513728

Current iteration: 944
Current error: 0.00189301063171

Current iteration: 945
Current error: 0.00182946937902

Current iteration: 946
Current error: 0.00176739403665

Current iteration: 947
Current error: 0.001709137684

Current iteration: 948
Current error: 0.00165318963532

Current iteration: 949
Current error: 0.00160058069692

Current iteration: 950
Current error: 0.0015502598622

Current iteration: 951
Current error: 0.00150209796945

Current iteration: 952
Current error: 0.00145628080002

Current iteration: 953
Current error: 0.00141217093925

Current iteration: 954
Current error: 0.001370311019

Current iteration: 955
Current error: 0.00133027069616

Current iteration: 956
Current error: 0.00129166933515

Current iteration: 957
Current error: 0.00125474851123

Current iteration: 958
Current error: 0.00121950859603

Current iteration: 959
Current error: 0.00118633161769

Current iteration: 960
Current error: 0.00115355678141

Current iteration: 961
Current error: 0.00112189356274

Current iteration: 962
Current error: 0.00109171739197

Current iteration: 963
Current error: 0.0010631579215

Current iteration: 964
Current error: 0.00103633999284

Current iteration: 965
Current error: 0.00100889273195

Current iteration: 966
Current error: 0.000983192760556

Current iteration: 967
Current error: 0.000958750540669

Current iteration: 968
Current error: 0.000934666764063

Current iteration: 969
Current error: 0.000911858187088

Current iteration: 970
Current error: 0.000890004128447

Current iteration: 971
Current error: 0.000869488485589

Current iteration: 972
Current error: 0.000848236681998

Current iteration: 973
Current error: 0.000828213333185

Current iteration: 974
Current error: 0.000809004278088

Current iteration: 975
Current error: 0.000790434347028

Current iteration: 976
Current error: 0.461449294299

Current iteration: 977
Current error: 0.0013395326016

Current iteration: 978
Current error: 0.00130025453247

Current iteration: 979
Current error: 0.00126298179221

Current iteration: 980
Current error: 0.0012276227113

Current iteration: 981
Current error: 0.0011934226118

Current iteration: 982
Current error: 0.00116068718262

Current iteration: 983
Current error: 0.00112875281059

Current iteration: 984
Current error: 0.00109878775952

Current iteration: 985
Current error: 0.00106967074876

Current iteration: 986
Current error: 0.00104177373446

Current iteration: 987
Current error: 0.00101473781292

Current iteration: 988
Current error: 0.000989106563833

Current iteration: 989
Current error: 0.000964253185616

Current iteration: 990
Current error: 0.000940056640715

Current iteration: 991
Current error: 0.000916723553391

Current iteration: 992
Current error: 0.000895003422736

Current iteration: 993
Current error: 0.000873312124393

Current iteration: 994
Current error: 0.459540318322

Current iteration: 995
Current error: 0.00147364644894

Current iteration: 996
Current error: 0.0014290926492

Current iteration: 997
Current error: 0.00138645301415

Current iteration: 998
Current error: 0.00134555853271

Current iteration: 999
Current error: 0.00130645759932

Current iteration: 1000
Current error: 0.00126924785235

Current iteration: 1001
Current error: 0.451554911234

Current iteration: 1002
Current error: 0.00210981425101

Current iteration: 1003
Current error: 0.00203429590513

Current iteration: 1004
Current error: 0.00196281174599

Current iteration: 1005
Current error: 0.0018945904453

Current iteration: 1006
Current error: 0.00183110973584

Current iteration: 1007
Current error: 0.00176919249444

Current iteration: 1008
Current error: 0.00171052156231

Current iteration: 1009
Current error: 0.00165541112777

Current iteration: 1010
Current error: 0.00160244817382

Current iteration: 1011
Current error: 0.00155166203609

Current iteration: 1012
Current error: 0.00150416383882

Current iteration: 1013
Current error: 0.00145764691513

Current iteration: 1014
Current error: 0.00141358974534

Current iteration: 1015
Current error: 0.00137180773083

Current iteration: 1016
Current error: 0.00133126497459

Current iteration: 1017
Current error: 0.0012933433781

Current iteration: 1018
Current error: 0.00125591630305

Current iteration: 1019
Current error: 0.00122031413361

Current iteration: 1020
Current error: 0.00118668915631

Current iteration: 1021
Current error: 0.00115384002243

Current iteration: 1022
Current error: 0.00112311883413

Current iteration: 1023
Current error: 0.00109307003195

Current iteration: 1024
Current error: 0.00106430301272

Current iteration: 1025
Current error: 0.00103644836307

Current iteration: 1026
Current error: 0.00101030762557

Current iteration: 1027
Current error: 0.000984580561741

Current iteration: 1028
Current error: 0.000959310409523

Current iteration: 1029
Current error: 0.000935540330778

Current iteration: 1030
Current error: 0.000912451038695

Current iteration: 1031
Current error: 0.000890517315518

Current iteration: 1032
Current error: 0.000869088755375

Current iteration: 1033
Current error: 0.000848597513856

Current iteration: 1034
Current error: 0.000828521140761

Current iteration: 1035
Current error: 0.000809606740143

Current iteration: 1036
Current error: 0.000791125530811

Current iteration: 1037
Current error: 0.000773201676667

Current iteration: 1038
Current error: 0.000756229571332

Current iteration: 1039
Current error: 0.000738836702645

Current iteration: 1040
Current error: 0.000722879524717

Current iteration: 1041
Current error: 0.000707158631073

Current iteration: 1042
Current error: 0.000692081810672

Current iteration: 1043
Current error: 0.00067731145466

Current iteration: 1044
Current error: 0.000663000155499

Current iteration: 1045
Current error: 0.000649239184838

Current iteration: 1046
Current error: 0.000635820140919

Current iteration: 1047
Current error: 0.000623070375414

Current iteration: 1048
Current error: 0.000610287954106

Current iteration: 1049
Current error: 0.000598128852757

Current iteration: 1050
Current error: 0.000586257139794

Current iteration: 1051
Current error: 0.000574713884037

Current iteration: 1052
Current error: 0.000563654481219

Current iteration: 1053
Current error: 0.000552562900341

Current iteration: 1054
Current error: 0.000541926948109

Current iteration: 1055
Current error: 0.000531759865208

Current iteration: 1056
Current error: 0.000521882821526

Current iteration: 1057
Current error: 0.000512136173101

Current iteration: 1058
Current error: 0.000502594358231

Current iteration: 1059
Current error: 0.000493596053046

Current iteration: 1060
Current error: 0.000484584763821

Current iteration: 1061
Current error: 0.000476421614668

Current iteration: 1062
Current error: 0.000467683278347

Current iteration: 1063
Current error: 0.000459177226401

Current iteration: 1064
Current error: 0.00045136863125

Current iteration: 1065
Current error: 0.000443337869165

Current iteration: 1066
Current error: 0.000436001496693

Current iteration: 1067
Current error: 0.000428289878817

Current iteration: 1068
Current error: 0.000421092208573

Current iteration: 1069
Current error: 0.000414233526757

Current iteration: 1070
Current error: 0.000407338599058

Current iteration: 1071
Current error: 0.000400535902888

Current iteration: 1072
Current error: 0.00039417105677

Current iteration: 1073
Current error: 0.000387433756595

Current iteration: 1074
Current error: 0.000381403997092

Current iteration: 1075
Current error: 0.000375133770544

Current iteration: 1076
Current error: 0.000369156036871

Current iteration: 1077
Current error: 0.000363459495314

Current iteration: 1078
Current error: 0.000357861804339

Current iteration: 1079
Current error: 0.000352149913317

Current iteration: 1080
Current error: 0.000346689762329

Current iteration: 1081
Current error: 0.000341510391937

Current iteration: 1082
Current error: 0.474385141784

Current iteration: 1083
Current error: 0.000592691130436

Current iteration: 1084
Current error: 0.466481015019

Current iteration: 1085
Current error: 0.00101367345298

Current iteration: 1086
Current error: 0.000987376050006

Current iteration: 1087
Current error: 0.000962712624639

Current iteration: 1088
Current error: 0.000938997382515

Current iteration: 1089
Current error: 0.000915950551807

Current iteration: 1090
Current error: 0.000893534007326

Current iteration: 1091
Current error: 0.000871986370995

Current iteration: 1092
Current error: 0.000851421773707

Current iteration: 1093
Current error: 0.00083125400086

Current iteration: 1094
Current error: 0.460476431962

Current iteration: 1095
Current error: 0.00140611863755

Current iteration: 1096
Current error: 0.00136460607918

Current iteration: 1097
Current error: 0.00132391698745

Current iteration: 1098
Current error: 0.00128593496034

Current iteration: 1099
Current error: 0.00124905321694

Current iteration: 1100
Current error: 0.00121410930411

Current iteration: 1101
Current error: 0.00118059570236

Current iteration: 1102
Current error: 0.00114822158262

Current iteration: 1103
Current error: 0.00111724519948

Current iteration: 1104
Current error: 0.0010875091023

Current iteration: 1105
Current error: 0.00105897981053

Current iteration: 1106
Current error: 0.001031478971

Current iteration: 1107
Current error: 0.00100492221664

Current iteration: 1108
Current error: 0.000979624386522

Current iteration: 1109
Current error: 0.000954990485204

Current iteration: 1110
Current error: 0.000931466323237

Current iteration: 1111
Current error: 0.000908834044218

Current iteration: 1112
Current error: 0.000886356692466

Current iteration: 1113
Current error: 0.459234558221

Current iteration: 1114
Current error: 0.00149556782854

Current iteration: 1115
Current error: 0.447583989976

Current iteration: 1116
Current error: 0.0024680609274

Current iteration: 1117
Current error: 0.00237298793959

Current iteration: 1118
Current error: 0.00228399157103

Current iteration: 1119
Current error: 0.00219868282015

Current iteration: 1120
Current error: 0.00211889131534

Current iteration: 1121
Current error: 0.00204261137385

Current iteration: 1122
Current error: 0.00197136681827

Current iteration: 1123
Current error: 0.0019024149136

Current iteration: 1124
Current error: 0.00183779189715

Current iteration: 1125
Current error: 0.00177639490728

Current iteration: 1126
Current error: 0.00171756545062

Current iteration: 1127
Current error: 0.0016613371758

Current iteration: 1128
Current error: 0.00160782961707

Current iteration: 1129
Current error: 0.0015571295701

Current iteration: 1130
Current error: 0.00150871959256

Current iteration: 1131
Current error: 0.00146297678896

Current iteration: 1132
Current error: 0.00141849820505

Current iteration: 1133
Current error: 0.00137603587641

Current iteration: 1134
Current error: 0.00133599184963

Current iteration: 1135
Current error: 0.00129683872033

Current iteration: 1136
Current error: 0.0012598098143

Current iteration: 1137
Current error: 0.00122440761109

Current iteration: 1138
Current error: 0.00119026533217

Current iteration: 1139
Current error: 0.00115837877494

Current iteration: 1140
Current error: 0.00112651323858

Current iteration: 1141
Current error: 0.00109622972846

Current iteration: 1142
Current error: 0.00106738688929

Current iteration: 1143
Current error: 0.00103945353832

Current iteration: 1144
Current error: 0.00101265542669

Current iteration: 1145
Current error: 0.456525993826

Current iteration: 1146
Current error: 0.00169938852594

Current iteration: 1147
Current error: 0.00164449990039

Current iteration: 1148
Current error: 0.00159226185367

Current iteration: 1149
Current error: 0.00154154783421

Current iteration: 1150
Current error: 0.00149413523001

Current iteration: 1151
Current error: 0.00144865519369

Current iteration: 1152
Current error: 0.00140512077148

Current iteration: 1153
Current error: 0.00136357300417

Current iteration: 1154
Current error: 0.00132463915054

Current iteration: 1155
Current error: 0.00128508578704

Current iteration: 1156
Current error: 0.00124914852098

Current iteration: 1157
Current error: 0.00121364043873

Current iteration: 1158
Current error: 0.00118027213075

Current iteration: 1159
Current error: 0.0011476334641

Current iteration: 1160
Current error: 0.00111707967155

Current iteration: 1161
Current error: 0.00108712073498

Current iteration: 1162
Current error: 0.00105852975809

Current iteration: 1163
Current error: 0.00103079723449

Current iteration: 1164
Current error: 0.00100427098857

Current iteration: 1165
Current error: 0.000979081726729

Current iteration: 1166
Current error: 0.000954348675772

Current iteration: 1167
Current error: 0.000930867680266

Current iteration: 1168
Current error: 0.000908200699866

Current iteration: 1169
Current error: 0.000885935025165

Current iteration: 1170
Current error: 0.000865086861158

Current iteration: 1171
Current error: 0.000844839190004

Current iteration: 1172
Current error: 0.000825725812645

Current iteration: 1173
Current error: 0.000806087867551

Current iteration: 1174
Current error: 0.000787502913314

Current iteration: 1175
Current error: 0.000769757719801

Current iteration: 1176
Current error: 0.000752528786385

Current iteration: 1177
Current error: 0.000735532098384

Current iteration: 1178
Current error: 0.0007194460975

Current iteration: 1179
Current error: 0.000704066351049

Current iteration: 1180
Current error: 0.000688870638661

Current iteration: 1181
Current error: 0.4639240285

Current iteration: 1182
Current error: 0.00117254811322

Current iteration: 1183
Current error: 0.0011404109762

Current iteration: 1184
Current error: 0.00110980268423

Current iteration: 1185
Current error: 0.00108012692156

Current iteration: 1186
Current error: 0.00105200145385

Current iteration: 1187
Current error: 0.00102457613019

Current iteration: 1188
Current error: 0.000998220725223

Current iteration: 1189
Current error: 0.000973195339569

Current iteration: 1190
Current error: 0.000949611396702

Current iteration: 1191
Current error: 0.00092541513331

Current iteration: 1192
Current error: 0.000903356278803

Current iteration: 1193
Current error: 0.000881522210015

Current iteration: 1194
Current error: 0.000860188699388

Current iteration: 1195
Current error: 0.000839767680722

Current iteration: 1196
Current error: 0.000820395055432

Current iteration: 1197
Current error: 0.460737985649

Current iteration: 1198
Current error: 0.00138759552374

Current iteration: 1199
Current error: 0.00134669932125

Current iteration: 1200
Current error: 0.0013085909683

Current iteration: 1201
Current error: 0.00126968269759

Current iteration: 1202
Current error: 0.00123398937235

Current iteration: 1203
Current error: 0.0011994365169

Current iteration: 1204
Current error: 0.00116625296641

Current iteration: 1205
Current error: 0.00113464576245

Current iteration: 1206
Current error: 0.00110430475849

Current iteration: 1207
Current error: 0.00107492728453

Current iteration: 1208
Current error: 0.00104674927579

Current iteration: 1209
Current error: 0.00101967967119

Current iteration: 1210
Current error: 0.000993953452255

Current iteration: 1211
Current error: 0.000969044233866

Current iteration: 1212
Current error: 0.45744937316

Current iteration: 1213
Current error: 0.0016288832466

Current iteration: 1214
Current error: 0.00157673172489

Current iteration: 1215
Current error: 0.00152764185213

Current iteration: 1216
Current error: 0.00148047398916

Current iteration: 1217
Current error: 0.00143523622116

Current iteration: 1218
Current error: 0.00139239934589

Current iteration: 1219
Current error: 0.00135116238279

Current iteration: 1220
Current error: 0.00131177455544

Current iteration: 1221
Current error: 0.00127401626515

Current iteration: 1222
Current error: 0.451443415578

Current iteration: 1223
Current error: 0.00211944659581

Current iteration: 1224
Current error: 0.00204226481358

Current iteration: 1225
Current error: 0.00197032738922

Current iteration: 1226
Current error: 0.0019022677698

Current iteration: 1227
Current error: 0.00183769856514

Current iteration: 1228
Current error: 0.0017754955776

Current iteration: 1229
Current error: 0.00171734798958

Current iteration: 1230
Current error: 0.00166115047527

Current iteration: 1231
Current error: 0.00160746478894

Current iteration: 1232
Current error: 0.445716486223

Current iteration: 1233
Current error: 0.00264420763839

Current iteration: 1234
Current error: 0.00253883889121

Current iteration: 1235
Current error: 0.00244031780155

Current iteration: 1236
Current error: 0.00234694494242

Current iteration: 1237
Current error: 0.435005154704

Current iteration: 1238
Current error: 0.00378397966856

Current iteration: 1239
Current error: 0.00360963793695

Current iteration: 1240
Current error: 0.00344581485798

Current iteration: 1241
Current error: 0.00329025617771

Current iteration: 1242
Current error: 0.00314643813687

Current iteration: 1243
Current error: 0.00301118416247

Current iteration: 1244
Current error: 0.00288560223199

Current iteration: 1245
Current error: 0.0027660863861

Current iteration: 1246
Current error: 0.00265462731221

Current iteration: 1247
Current error: 0.0025484631346

Current iteration: 1248
Current error: 0.00244999873037

Current iteration: 1249
Current error: 0.00235649613138

Current iteration: 1250
Current error: 0.0022672513036

Current iteration: 1251
Current error: 0.00218340759157

Current iteration: 1252
Current error: 0.00210387982003

Current iteration: 1253
Current error: 0.00202884606668

Current iteration: 1254
Current error: 0.439333909803

Current iteration: 1255
Current error: 0.00329755216423

Current iteration: 1256
Current error: 0.00315343390083

Current iteration: 1257
Current error: 0.00301799745369

Current iteration: 1258
Current error: 0.00289113644712

Current iteration: 1259
Current error: 0.00277263143587

Current iteration: 1260
Current error: 0.00265956712277

Current iteration: 1261
Current error: 0.00255356890851

Current iteration: 1262
Current error: 0.0024539873372

Current iteration: 1263
Current error: 0.00236143563424

Current iteration: 1264
Current error: 0.00227185292183

Current iteration: 1265
Current error: 0.00218711529226

Current iteration: 1266
Current error: 0.00210770594778

Current iteration: 1267
Current error: 0.00203263538322

Current iteration: 1268
Current error: 0.0019625420601

Current iteration: 1269
Current error: 0.00189347107978

Current iteration: 1270
Current error: 0.00182884750967

Current iteration: 1271
Current error: 0.00176759319117

Current iteration: 1272
Current error: 0.00170888162288

Current iteration: 1273
Current error: 0.00165381289426

Current iteration: 1274
Current error: 0.00160050872384

Current iteration: 1275
Current error: 0.00155128000865

Current iteration: 1276
Current error: 0.00150251889808

Current iteration: 1277
Current error: 0.447467582817

Current iteration: 1278
Current error: 0.00247934033301

Current iteration: 1279
Current error: 0.00238343566081

Current iteration: 1280
Current error: 0.434517596914

Current iteration: 1281
Current error: 0.00383888151449

Current iteration: 1282
Current error: 0.0036588957733

Current iteration: 1283
Current error: 0.00349172522968

Current iteration: 1284
Current error: 0.00333517612213

Current iteration: 1285
Current error: 0.00318830044951

Current iteration: 1286
Current error: 0.00305070421186

Current iteration: 1287
Current error: 0.00292349928107

Current iteration: 1288
Current error: 0.00280104875758

Current iteration: 1289
Current error: 0.00268709465052

Current iteration: 1290
Current error: 0.0025797081015

Current iteration: 1291
Current error: 0.00247840947357

Current iteration: 1292
Current error: 0.00238355735336

Current iteration: 1293
Current error: 0.434513197101

Current iteration: 1294
Current error: 0.00384023007839

Current iteration: 1295
Current error: 0.00365852746337

Current iteration: 1296
Current error: 0.00349295872013

Current iteration: 1297
Current error: 0.00333490112602

Current iteration: 1298
Current error: 0.00318757093426

Current iteration: 1299
Current error: 0.00305074047368

Current iteration: 1300
Current error: 0.00292200462485

Current iteration: 1301
Current error: 0.00280065998547

Current iteration: 1302
Current error: 0.00268711996618

Current iteration: 1303
Current error: 0.00258027075198

Current iteration: 1304
Current error: 0.00247878056948

Current iteration: 1305
Current error: 0.00238279469368

Current iteration: 1306
Current error: 0.00229283401854

Current iteration: 1307
Current error: 0.00220785968232

Current iteration: 1308
Current error: 0.00212725324035

Current iteration: 1309
Current error: 0.00205073494034

Current iteration: 1310
Current error: 0.00197861108158

Current iteration: 1311
Current error: 0.00190971792555

Current iteration: 1312
Current error: 0.00184456436384

Current iteration: 1313
Current error: 0.00178212007669

Current iteration: 1314
Current error: 0.00172378928041

Current iteration: 1315
Current error: 0.0016671568592

Current iteration: 1316
Current error: 0.00161453231657

Current iteration: 1317
Current error: 0.00156287958451

Current iteration: 1318
Current error: 0.00151384383769

Current iteration: 1319
Current error: 0.00146767156553

Current iteration: 1320
Current error: 0.00142412414087

Current iteration: 1321
Current error: 0.00138095415582

Current iteration: 1322
Current error: 0.00134040942157

Current iteration: 1323
Current error: 0.00130105022407

Current iteration: 1324
Current error: 0.00126371386393

Current iteration: 1325
Current error: 0.00122922514277

Current iteration: 1326
Current error: 0.00119397927545

Current iteration: 1327
Current error: 0.00116118289022

Current iteration: 1328
Current error: 0.00112965018987

Current iteration: 1329
Current error: 0.00109940466263

Current iteration: 1330
Current error: 0.00107076174316

Current iteration: 1331
Current error: 0.00104259689556

Current iteration: 1332
Current error: 0.00101578460661

Current iteration: 1333
Current error: 0.000989719817074

Current iteration: 1334
Current error: 0.000964925326839

Current iteration: 1335
Current error: 0.000940863025424

Current iteration: 1336
Current error: 0.458035358562

Current iteration: 1337
Current error: 0.00158355515435

Current iteration: 1338
Current error: 0.00153344559128

Current iteration: 1339
Current error: 0.00148619510229

Current iteration: 1340
Current error: 0.00144110063729

Current iteration: 1341
Current error: 0.00139757109473

Current iteration: 1342
Current error: 0.00135634012222

Current iteration: 1343
Current error: 0.00131712817128

Current iteration: 1344
Current error: 0.0012786084003

Current iteration: 1345
Current error: 0.00124251601819

Current iteration: 1346
Current error: 0.00120771514484

Current iteration: 1347
Current error: 0.00117445347821

Current iteration: 1348
Current error: 0.00114218440059

Current iteration: 1349
Current error: 0.00111145514263

Current iteration: 1350
Current error: 0.0010820277404

Current iteration: 1351
Current error: 0.00105362044612

Current iteration: 1352
Current error: 0.00102709047811

Current iteration: 1353
Current error: 0.000999968638067

Current iteration: 1354
Current error: 0.456761072284

Current iteration: 1355
Current error: 0.00167856266554

Current iteration: 1356
Current error: 0.00162492888461

Current iteration: 1357
Current error: 0.00157321419998

Current iteration: 1358
Current error: 0.00152440898341

Current iteration: 1359
Current error: 0.00147737725828

Current iteration: 1360
Current error: 0.00143313012022

Current iteration: 1361
Current error: 0.448631593697

Current iteration: 1362
Current error: 0.00236894718445

Current iteration: 1363
Current error: 0.00227997662696

Current iteration: 1364
Current error: 0.435917120482

Current iteration: 1365
Current error: 0.00368116445597

Current iteration: 1366
Current error: 0.00351229397813

Current iteration: 1367
Current error: 0.00335279578334

Current iteration: 1368
Current error: 0.423097000304

Current iteration: 1369
Current error: 0.00528823641829

Current iteration: 1370
Current error: 0.00500345466585

Current iteration: 1371
Current error: 0.00474208649296

Current iteration: 1372
Current error: 0.00449855169249

Current iteration: 1373
Current error: 0.00427240957596

Current iteration: 1374
Current error: 0.00406322831806

Current iteration: 1375
Current error: 0.00386942056195

Current iteration: 1376
Current error: 0.00368636363992

Current iteration: 1377
Current error: 0.00351732240243

Current iteration: 1378
Current error: 0.00335943435086

Current iteration: 1379
Current error: 0.00321020059991

Current iteration: 1380
Current error: 0.00307160946859

Current iteration: 1381
Current error: 0.00294206033885

Current iteration: 1382
Current error: 0.00282028848049

Current iteration: 1383
Current error: 0.00270475878021

Current iteration: 1384
Current error: 0.0025958936599

Current iteration: 1385
Current error: 0.00249443151051

Current iteration: 1386
Current error: 0.433089167536

Current iteration: 1387
Current error: 0.00400653580746

Current iteration: 1388
Current error: 0.00381519425543

Current iteration: 1389
Current error: 0.00363678171017

Current iteration: 1390
Current error: 0.420096134066

Current iteration: 1391
Current error: 0.00570521411288

Current iteration: 1392
Current error: 0.00538914860773

Current iteration: 1393
Current error: 0.00509619173694

Current iteration: 1394
Current error: 0.00482600929681

Current iteration: 1395
Current error: 0.00457585045122

Current iteration: 1396
Current error: 0.00434469978622

Current iteration: 1397
Current error: 0.00413013412381

Current iteration: 1398
Current error: 0.00393244182744

Current iteration: 1399
Current error: 0.00374627460609

Current iteration: 1400
Current error: 0.0035714297587

Current iteration: 1401
Current error: 0.00341122928402

Current iteration: 1402
Current error: 0.0032584330549

Current iteration: 1403
Current error: 0.00311728716922

Current iteration: 1404
Current error: 0.425692158131

Current iteration: 1405
Current error: 0.00493769754952

Current iteration: 1406
Current error: 0.00468207127216

Current iteration: 1407
Current error: 0.00444139781442

Current iteration: 1408
Current error: 0.00421947160407

Current iteration: 1409
Current error: 0.00401374248592

Current iteration: 1410
Current error: 0.00382300305304

Current iteration: 1411
Current error: 0.00364410364696

Current iteration: 1412
Current error: 0.00347752161211

Current iteration: 1413
Current error: 0.00332298189355

Current iteration: 1414
Current error: 0.00317611766788

Current iteration: 1415
Current error: 0.00303927728683

Current iteration: 1416
Current error: 0.00291135696414

Current iteration: 1417
Current error: 0.00279070217637

Current iteration: 1418
Current error: 0.00267746286477

Current iteration: 1419
Current error: 0.00257179317545

Current iteration: 1420
Current error: 0.00246988465689

Current iteration: 1421
Current error: 0.433413437075

Current iteration: 1422
Current error: 0.414774394223

Current iteration: 1423
Current error: 0.00647999548689

Current iteration: 1424
Current error: 0.00610106812763

Current iteration: 1425
Current error: 0.00575086524392

Current iteration: 1426
Current error: 0.00543353201576

Current iteration: 1427
Current error: 0.00513519979052

Current iteration: 1428
Current error: 0.406157953394

Current iteration: 1429
Current error: 0.00785159971779

Current iteration: 1430
Current error: 0.00735216566734

Current iteration: 1431
Current error: 0.00689720851857

Current iteration: 1432
Current error: 0.00648121199074

Current iteration: 1433
Current error: 0.395555346524

Current iteration: 1434
Current error: 0.00971798695281

Current iteration: 1435
Current error: 0.00904358458476

Current iteration: 1436
Current error: 0.00843688879265

Current iteration: 1437
Current error: 0.0078832230645

Current iteration: 1438
Current error: 0.00738079790545

Current iteration: 1439
Current error: 0.00692391803695

Current iteration: 1440
Current error: 0.00650630373462

Current iteration: 1441
Current error: 0.00612709490847

Current iteration: 1442
Current error: 0.00577434283514

Current iteration: 1443
Current error: 0.00545174066004

Current iteration: 1444
Current error: 0.00515465574758

Current iteration: 1445
Current error: 0.00488257371672

Current iteration: 1446
Current error: 0.00462735802203

Current iteration: 1447
Current error: 0.00439273034643

Current iteration: 1448
Current error: 0.412762904388

Current iteration: 1449
Current error: 0.00679596874572

Current iteration: 1450
Current error: 0.0063886357853

Current iteration: 1451
Current error: 0.00601654834924

Current iteration: 1452
Current error: 0.00567524921281

Current iteration: 1453
Current error: 0.00535983802699

Current iteration: 1454
Current error: 0.00507136387779

Current iteration: 1455
Current error: 0.00480216333385

Current iteration: 1456
Current error: 0.00455609531398

Current iteration: 1457
Current error: 0.0043258749449

Current iteration: 1458
Current error: 0.00411069491568

Current iteration: 1459
Current error: 0.00391447857554

Current iteration: 1460
Current error: 0.00372853270726

Current iteration: 1461
Current error: 0.00355659168565

Current iteration: 1462
Current error: 0.00339524613244

Current iteration: 1463
Current error: 0.00324464439643

Current iteration: 1464
Current error: 0.00310425913934

Current iteration: 1465
Current error: 0.00297222307976

Current iteration: 1466
Current error: 0.00284782801649

Current iteration: 1467
Current error: 0.00273245670869

Current iteration: 1468
Current error: 0.00262161197735

Current iteration: 1469
Current error: 0.00251733241656

Current iteration: 1470
Current error: 0.00242051919215

Current iteration: 1471
Current error: 0.00232826998344

Current iteration: 1472
Current error: 0.435247600018

Current iteration: 1473
Current error: 0.00375461841368

Current iteration: 1474
Current error: 0.00358169534254

Current iteration: 1475
Current error: 0.00341886386315

Current iteration: 1476
Current error: 0.0032667449903

Current iteration: 1477
Current error: 0.00312839444877

Current iteration: 1478
Current error: 0.00299032623655

Current iteration: 1479
Current error: 0.00286566182354

Current iteration: 1480
Current error: 0.00274835893241

Current iteration: 1481
Current error: 0.00263675249922

Current iteration: 1482
Current error: 0.00253294300175

Current iteration: 1483
Current error: 0.00243453094974

Current iteration: 1484
Current error: 0.00234148624982

Current iteration: 1485
Current error: 0.0022535385546

Current iteration: 1486
Current error: 0.00217039536681

Current iteration: 1487
Current error: 0.00209190184079

Current iteration: 1488
Current error: 0.00201708735596

Current iteration: 1489
Current error: 0.00194811049482

Current iteration: 1490
Current error: 0.00187975492715

Current iteration: 1491
Current error: 0.00181585271226

Current iteration: 1492
Current error: 0.00175522082497

Current iteration: 1493
Current error: 0.00169757195898

Current iteration: 1494
Current error: 0.00164295341393

Current iteration: 1495
Current error: 0.00159035995209

Current iteration: 1496
Current error: 0.0015400888113

Current iteration: 1497
Current error: 0.00149292199935

Current iteration: 1498
Current error: 0.00144719824231

Current iteration: 1499
Current error: 0.00140357301224

Current iteration: 1500
Current error: 0.00136276893975

Current iteration: 1501
Current error: 0.00132227427236

Current iteration: 1502
Current error: 0.00128408566699

Current iteration: 1503
Current error: 0.00124721050801

Current iteration: 1504
Current error: 0.00121261785099

Current iteration: 1505
Current error: 0.00117969353002

Current iteration: 1506
Current error: 0.00114693825703

Current iteration: 1507
Current error: 0.00111577551318

Current iteration: 1508
Current error: 0.00108606945677

Current iteration: 1509
Current error: 0.00105760138322

Current iteration: 1510
Current error: 0.00102992207649

Current iteration: 1511
Current error: 0.00100412586857

Current iteration: 1512
Current error: 0.000978252063164

Current iteration: 1513
Current error: 0.000953581781982

Current iteration: 1514
Current error: 0.000930125591312

Current iteration: 1515
Current error: 0.00090725017218

Current iteration: 1516
Current error: 0.000885386761142

Current iteration: 1517
Current error: 0.000864146466687

Current iteration: 1518
Current error: 0.000843713093958

Current iteration: 1519
Current error: 0.000824285491287

Current iteration: 1520
Current error: 0.000805025158652

Current iteration: 1521
Current error: 0.000786711231934

Current iteration: 1522
Current error: 0.000769063009452

Current iteration: 1523
Current error: 0.000751847648931

Current iteration: 1524
Current error: 0.000735280464772

Current iteration: 1525
Current error: 0.000718992367176

Current iteration: 1526
Current error: 0.000703605056362

Current iteration: 1527
Current error: 0.000688366934541

Current iteration: 1528
Current error: 0.000673792889028

Current iteration: 1529
Current error: 0.000659835933674

Current iteration: 1530
Current error: 0.000646026156577

Current iteration: 1531
Current error: 0.000632726583552

Current iteration: 1532
Current error: 0.00061987325981

Current iteration: 1533
Current error: 0.000607255723684

Current iteration: 1534
Current error: 0.000595180810802

Current iteration: 1535
Current error: 0.000583298288653

Current iteration: 1536
Current error: 0.00057189999889

Current iteration: 1537
Current error: 0.0005608666004

Current iteration: 1538
Current error: 0.000550374853665

Current iteration: 1539
Current error: 0.000539960724836

Current iteration: 1540
Current error: 0.000529823703539

Current iteration: 1541
Current error: 0.000519490669924

Current iteration: 1542
Current error: 0.000509936253607

Current iteration: 1543
Current error: 0.000500456895783

Current iteration: 1544
Current error: 0.469106222938

Current iteration: 1545
Current error: 0.000860053075972

Current iteration: 1546
Current error: 0.00083988924822

Current iteration: 1547
Current error: 0.000820269685867

Current iteration: 1548
Current error: 0.0008018609662

Current iteration: 1549
Current error: 0.000783193947526

Current iteration: 1550
Current error: 0.000765924723626

Current iteration: 1551
Current error: 0.000748113285389

Current iteration: 1552
Current error: 0.000731941727078

Current iteration: 1553
Current error: 0.000716248954933

Current iteration: 1554
Current error: 0.000700266149015

Current iteration: 1555
Current error: 0.000685764118564

Current iteration: 1556
Current error: 0.000670978299436

Current iteration: 1557
Current error: 0.000657029355835

Current iteration: 1558
Current error: 0.000643317704205

Current iteration: 1559
Current error: 0.000629964997693

Current iteration: 1560
Current error: 0.000617195738337

Current iteration: 1561
Current error: 0.000605598873285

Current iteration: 1562
Current error: 0.000592677273054

Current iteration: 1563
Current error: 0.466454713058

Current iteration: 1564
Current error: 0.00101416690655

Current iteration: 1565
Current error: 0.00098745478499

Current iteration: 1566
Current error: 0.000962798669586

Current iteration: 1567
Current error: 0.000938914629762

Current iteration: 1568
Current error: 0.000916010490144

Current iteration: 1569
Current error: 0.458589600986

Current iteration: 1570
Current error: 0.00154294903607

Current iteration: 1571
Current error: 0.00149542484829

Current iteration: 1572
Current error: 0.00144973254305

Current iteration: 1573
Current error: 0.00140619156673

Current iteration: 1574
Current error: 0.00136422576727

Current iteration: 1575
Current error: 0.44981362816

Current iteration: 1576
Current error: 0.00226012832716

Current iteration: 1577
Current error: 0.00217662964631

Current iteration: 1578
Current error: 0.00209800963895

Current iteration: 1579
Current error: 0.00202288781823

Current iteration: 1580
Current error: 0.00195182371674

Current iteration: 1581
Current error: 0.0018850943582

Current iteration: 1582
Current error: 0.00182035494887

Current iteration: 1583
Current error: 0.00175955871998

Current iteration: 1584
Current error: 0.00170291277308

Current iteration: 1585
Current error: 0.00164670696132

Current iteration: 1586
Current error: 0.00159417242607

Current iteration: 1587
Current error: 0.445886597669

Current iteration: 1588
Current error: 0.00262294601151

Current iteration: 1589
Current error: 0.00252011388735

Current iteration: 1590
Current error: 0.00242148723275

Current iteration: 1591
Current error: 0.00232959125554

Current iteration: 1592
Current error: 0.00224148337125

Current iteration: 1593
Current error: 0.00215931662157

Current iteration: 1594
Current error: 0.00208100528013

Current iteration: 1595
Current error: 0.00200732187743

Current iteration: 1596
Current error: 0.00193815595407

Current iteration: 1597
Current error: 0.00187022859951

Current iteration: 1598
Current error: 0.00180776730654

Current iteration: 1599
Current error: 0.00174781954448

Current iteration: 1600
Current error: 0.00168964804417

Current iteration: 1601
Current error: 0.00163523716618

Current iteration: 1602
Current error: 0.00158280812215

Current iteration: 1603
Current error: 0.00153333234541

Current iteration: 1604
Current error: 0.00148696883973

Current iteration: 1605
Current error: 0.0014406907997

Current iteration: 1606
Current error: 0.00139757743698

Current iteration: 1607
Current error: 0.00135652671882

Current iteration: 1608
Current error: 0.00131700938104

Current iteration: 1609
Current error: 0.00127905808486

Current iteration: 1610
Current error: 0.00124265417052

Current iteration: 1611
Current error: 0.001207866171

Current iteration: 1612
Current error: 0.00117513070729

Current iteration: 1613
Current error: 0.00114264562165

Current iteration: 1614
Current error: 0.00111160711093

Current iteration: 1615
Current error: 0.0010827943672

Current iteration: 1616
Current error: 0.455114421608

Current iteration: 1617
Current error: 0.00181094474079

Current iteration: 1618
Current error: 0.00175157269594

Current iteration: 1619
Current error: 0.00169294207895

Current iteration: 1620
Current error: 0.00163845575618

Current iteration: 1621
Current error: 0.00158667641419

Current iteration: 1622
Current error: 0.00153630014028

Current iteration: 1623
Current error: 0.00148910390232

Current iteration: 1624
Current error: 0.00144387160774

Current iteration: 1625
Current error: 0.00140061247234

Current iteration: 1626
Current error: 0.0013585560966

Current iteration: 1627
Current error: 0.00131906698107

Current iteration: 1628
Current error: 0.00128187025866

Current iteration: 1629
Current error: 0.00124478828973

Current iteration: 1630
Current error: 0.00121010266026

Current iteration: 1631
Current error: 0.0011764347642

Current iteration: 1632
Current error: 0.00114442927622

Current iteration: 1633
Current error: 0.00111339972331

Current iteration: 1634
Current error: 0.00108391703931

Current iteration: 1635
Current error: 0.00105593310703

Current iteration: 1636
Current error: 0.00102789371307

Current iteration: 1637
Current error: 0.00100155897308

Current iteration: 1638
Current error: 0.000977028497926

Current iteration: 1639
Current error: 0.00095189061404

Current iteration: 1640
Current error: 0.000928309738582

Current iteration: 1641
Current error: 0.00090571370166

Current iteration: 1642
Current error: 0.000883951564401

Current iteration: 1643
Current error: 0.000862552399837

Current iteration: 1644
Current error: 0.000842356368773

Current iteration: 1645
Current error: 0.000822676346048

Current iteration: 1646
Current error: 0.460666544188

Current iteration: 1647
Current error: 0.00139139537547

Current iteration: 1648
Current error: 0.00135021601414

Current iteration: 1649
Current error: 0.450078213207

Current iteration: 1650
Current error: 0.00223870382535

Current iteration: 1651
Current error: 0.436424510845

Current iteration: 1652
Current error: 0.00361820867234

Current iteration: 1653
Current error: 0.00345354144688

Current iteration: 1654
Current error: 0.00329913222039

Current iteration: 1655
Current error: 0.00315496039908

Current iteration: 1656
Current error: 0.425257340888

Current iteration: 1657
Current error: 0.00499469668064

Current iteration: 1658
Current error: 0.00473331198319

Current iteration: 1659
Current error: 0.00449108223049

Current iteration: 1660
Current error: 0.00426623423119

Current iteration: 1661
Current error: 0.00405605941196

Current iteration: 1662
Current error: 0.00386148451726

Current iteration: 1663
Current error: 0.00368088725496

Current iteration: 1664
Current error: 0.00351160622322

Current iteration: 1665
Current error: 0.00335369907334

Current iteration: 1666
Current error: 0.00320625444816

Current iteration: 1667
Current error: 0.00306753916161

Current iteration: 1668
Current error: 0.00293737872104

Current iteration: 1669
Current error: 0.427745170454

Current iteration: 1670
Current error: 0.00467197190058

Current iteration: 1671
Current error: 0.00443412898077

Current iteration: 1672
Current error: 0.0042131789543

Current iteration: 1673
Current error: 0.00400777100312

Current iteration: 1674
Current error: 0.00381674059014

Current iteration: 1675
Current error: 0.00364155554392

Current iteration: 1676
Current error: 0.00347252272681

Current iteration: 1677
Current error: 0.003316663803

Current iteration: 1678
Current error: 0.00317167524879

Current iteration: 1679
Current error: 0.00303517782919

Current iteration: 1680
Current error: 0.00290713954317

Current iteration: 1681
Current error: 0.00278764732109

Current iteration: 1682
Current error: 0.00267352423078

Current iteration: 1683
Current error: 0.00256741017975

Current iteration: 1684
Current error: 0.00246678919516

Current iteration: 1685
Current error: 0.00237213087313

Current iteration: 1686
Current error: 0.00228389383211

Current iteration: 1687
Current error: 0.00219886860606

Current iteration: 1688
Current error: 0.00211826411065

Current iteration: 1689
Current error: 0.0020424564671

Current iteration: 1690
Current error: 0.00197027582619

Current iteration: 1691
Current error: 0.0019017295974

Current iteration: 1692
Current error: 0.00183690954252

Current iteration: 1693
Current error: 0.00177543734217

Current iteration: 1694
Current error: 0.00171826880379

Current iteration: 1695
Current error: 0.443939001562

Current iteration: 1696
Current error: 0.00281404016625

Current iteration: 1697
Current error: 0.00269937053108

Current iteration: 1698
Current error: 0.00259274786486

Current iteration: 1699
Current error: 0.00249019036706

Current iteration: 1700
Current error: 0.00239325467068

Current iteration: 1701
Current error: 0.00230272886171

Current iteration: 1702
Current error: 0.00221728047973

Current iteration: 1703
Current error: 0.00213639105395

Current iteration: 1704
Current error: 0.00205897903427

Current iteration: 1705
Current error: 0.00198632699775

Current iteration: 1706
Current error: 0.00191705478273

Current iteration: 1707
Current error: 0.00185133355119

Current iteration: 1708
Current error: 0.00178939056865

Current iteration: 1709
Current error: 0.00173086499281

Current iteration: 1710
Current error: 0.00167374417506

Current iteration: 1711
Current error: 0.00161956746284

Current iteration: 1712
Current error: 0.00156848911145

Current iteration: 1713
Current error: 0.00151934575296

Current iteration: 1714
Current error: 0.0014724239891

Current iteration: 1715
Current error: 0.00142785238994

Current iteration: 1716
Current error: 0.00138526828163

Current iteration: 1717
Current error: 0.0013446069341

Current iteration: 1718
Current error: 0.00130525653957

Current iteration: 1719
Current error: 0.00126797101527

Current iteration: 1720
Current error: 0.00123192564295

Current iteration: 1721
Current error: 0.00119794816704

Current iteration: 1722
Current error: 0.00116499470366

Current iteration: 1723
Current error: 0.00113319240786

Current iteration: 1724
Current error: 0.0011029072371

Current iteration: 1725
Current error: 0.00107334820262

Current iteration: 1726
Current error: 0.00104558776064

Current iteration: 1727
Current error: 0.0010182612464

Current iteration: 1728
Current error: 0.000993133359879

Current iteration: 1729
Current error: 0.000967529276711

Current iteration: 1730
Current error: 0.000944052704111

Current iteration: 1731
Current error: 0.000920126475581

Current iteration: 1732
Current error: 0.00089828813233

Current iteration: 1733
Current error: 0.000876195607914

Current iteration: 1734
Current error: 0.000855350618873

Current iteration: 1735
Current error: 0.000835306073537

Current iteration: 1736
Current error: 0.000815953837973

Current iteration: 1737
Current error: 0.000796919928125

Current iteration: 1738
Current error: 0.000779180197371

Current iteration: 1739
Current error: 0.000761444351154

Current iteration: 1740
Current error: 0.000744854006331

Current iteration: 1741
Current error: 0.462478323857

Current iteration: 1742
Current error: 0.00126319113768

Current iteration: 1743
Current error: 0.00122784287704

Current iteration: 1744
Current error: 0.00119340280216

Current iteration: 1745
Current error: 0.00116107294505

Current iteration: 1746
Current error: 0.00112926801014

Current iteration: 1747
Current error: 0.454168336499

Current iteration: 1748
Current error: 0.44036005253

Current iteration: 1749
Current error: 0.00318165681552

Current iteration: 1750
Current error: 0.00304412319554

Current iteration: 1751
Current error: 0.00291578561745

Current iteration: 1752
Current error: 0.00279418553947

Current iteration: 1753
Current error: 0.00268173006373

Current iteration: 1754
Current error: 0.002574390917

Current iteration: 1755
Current error: 0.00247446614963

Current iteration: 1756
Current error: 0.0023785131787

Current iteration: 1757
Current error: 0.00228825535136

Current iteration: 1758
Current error: 0.00220422639643

Current iteration: 1759
Current error: 0.00212351585399

Current iteration: 1760
Current error: 0.00204692080235

Current iteration: 1761
Current error: 0.00197532483952

Current iteration: 1762
Current error: 0.00190612687996

Current iteration: 1763
Current error: 0.0018409872124

Current iteration: 1764
Current error: 0.00177939195923

Current iteration: 1765
Current error: 0.00172015742963

Current iteration: 1766
Current error: 0.00166651155772

Current iteration: 1767
Current error: 0.00161076515012

Current iteration: 1768
Current error: 0.00156010214209

Current iteration: 1769
Current error: 0.446485054443

Current iteration: 1770
Current error: 0.00256979448743

Current iteration: 1771
Current error: 0.00246979774345

Current iteration: 1772
Current error: 0.00237540974314

Current iteration: 1773
Current error: 0.00228470096948

Current iteration: 1774
Current error: 0.00220126588825

Current iteration: 1775
Current error: 0.00211945134099

Current iteration: 1776
Current error: 0.00204326027626

Current iteration: 1777
Current error: 0.00197163428891

Current iteration: 1778
Current error: 0.00190369856329

Current iteration: 1779
Current error: 0.00183835510393

Current iteration: 1780
Current error: 0.00177640473679

Current iteration: 1781
Current error: 0.00171807801702

Current iteration: 1782
Current error: 0.00166248096619

Current iteration: 1783
Current error: 0.00160917469939

Current iteration: 1784
Current error: 0.00155782666474

Current iteration: 1785
Current error: 0.0015094205738

Current iteration: 1786
Current error: 0.00146291783014

Current iteration: 1787
Current error: 0.00141900020464

Current iteration: 1788
Current error: 0.00137645352411

Current iteration: 1789
Current error: 0.00133643136298

Current iteration: 1790
Current error: 0.00129787372176

Current iteration: 1791
Current error: 0.0012602241938

Current iteration: 1792
Current error: 0.00122573089874

Current iteration: 1793
Current error: 0.00119064244095

Current iteration: 1794
Current error: 0.00115844076194

Current iteration: 1795
Current error: 0.00112663865463

Current iteration: 1796
Current error: 0.00109645010011

Current iteration: 1797
Current error: 0.00106765121088

Current iteration: 1798
Current error: 0.00103990853346

Current iteration: 1799
Current error: 0.00101440382415

Current iteration: 1800
Current error: 0.000986955540307

Current iteration: 1801
Current error: 0.000962888629796

Current iteration: 1802
Current error: 0.000938858228694

Current iteration: 1803
Current error: 0.000915580236946

Current iteration: 1804
Current error: 0.000893532157656

Current iteration: 1805
Current error: 0.000871890765463

Current iteration: 1806
Current error: 0.000851139525909

Current iteration: 1807
Current error: 0.000831264838942

Current iteration: 1808
Current error: 0.000811725935483

Current iteration: 1809
Current error: 0.000793195791934

Current iteration: 1810
Current error: 0.000775312121271

Current iteration: 1811
Current error: 0.000757961740969

Current iteration: 1812
Current error: 0.000741172984443

Current iteration: 1813
Current error: 0.462574004321

Current iteration: 1814
Current error: 0.00125752388395

Current iteration: 1815
Current error: 0.00122210340073

Current iteration: 1816
Current error: 0.00118835030065

Current iteration: 1817
Current error: 0.0011559088618

Current iteration: 1818
Current error: 0.00112439989725

Current iteration: 1819
Current error: 0.00109485361652

Current iteration: 1820
Current error: 0.00106514795298

Current iteration: 1821
Current error: 0.0010375893265

Current iteration: 1822
Current error: 0.00101075433742

Current iteration: 1823
Current error: 0.000985514593287

Current iteration: 1824
Current error: 0.0009606039796

Current iteration: 1825
Current error: 0.000936564081413

Current iteration: 1826
Current error: 0.000913901674917

Current iteration: 1827
Current error: 0.000892301046323

Current iteration: 1828
Current error: 0.000870215534415

Current iteration: 1829
Current error: 0.000849460929611

Current iteration: 1830
Current error: 0.000830230004702

Current iteration: 1831
Current error: 0.000811360721744

Current iteration: 1832
Current error: 0.000792301844456

Current iteration: 1833
Current error: 0.000773879078842

Current iteration: 1834
Current error: 0.000756442139559

Current iteration: 1835
Current error: 0.0007400042735

Current iteration: 1836
Current error: 0.000724446267405

Current iteration: 1837
Current error: 0.000707794776689

Current iteration: 1838
Current error: 0.000692946606428

Current iteration: 1839
Current error: 0.000678211969501

Current iteration: 1840
Current error: 0.000663793484119

Current iteration: 1841
Current error: 0.000649758955576

Current iteration: 1842
Current error: 0.000636666359217

Current iteration: 1843
Current error: 0.000623347296829

Current iteration: 1844
Current error: 0.000610771710944

Current iteration: 1845
Current error: 0.000598652950962

Current iteration: 1846
Current error: 0.000586631249925

Current iteration: 1847
Current error: 0.000575152555047

Current iteration: 1848
Current error: 0.000564023325039

Current iteration: 1849
Current error: 0.000552979619708

Current iteration: 1850
Current error: 0.000542605694118

Current iteration: 1851
Current error: 0.000532714086797

Current iteration: 1852
Current error: 0.000522295921791

Current iteration: 1853
Current error: 0.000512501268436

Current iteration: 1854
Current error: 0.468752154844

Current iteration: 1855
Current error: 0.458838342382

Current iteration: 1856
Current error: 0.00151971905197

Current iteration: 1857
Current error: 0.00147336357953

Current iteration: 1858
Current error: 0.00142891716175

Current iteration: 1859
Current error: 0.00138564061941

Current iteration: 1860
Current error: 0.00134477095627

Current iteration: 1861
Current error: 0.00130553717129

Current iteration: 1862
Current error: 0.00126896894933

Current iteration: 1863
Current error: 0.451506764953

Current iteration: 1864
Current error: 0.00210796268322

Current iteration: 1865
Current error: 0.00203254497574

Current iteration: 1866
Current error: 0.00196199051439

Current iteration: 1867
Current error: 0.00189337485046

Current iteration: 1868
Current error: 0.00182900880033

Current iteration: 1869
Current error: 0.0017677036681

Current iteration: 1870
Current error: 0.00170999807043

Current iteration: 1871
Current error: 0.00165397667485

Current iteration: 1872
Current error: 0.00160121149457

Current iteration: 1873
Current error: 0.00155136358701

Current iteration: 1874
Current error: 0.00150405715174

Current iteration: 1875
Current error: 0.00145697933613

Current iteration: 1876
Current error: 0.00141245155453

Current iteration: 1877
Current error: 0.00137079180425

Current iteration: 1878
Current error: 0.449694931197

Current iteration: 1879
Current error: 0.00227089556965

Current iteration: 1880
Current error: 0.00218706056095

Current iteration: 1881
Current error: 0.00210732337474

Current iteration: 1882
Current error: 0.00203196855769

Current iteration: 1883
Current error: 0.00196068151268

Current iteration: 1884
Current error: 0.00189232315447

Current iteration: 1885
Current error: 0.00182825597017

Current iteration: 1886
Current error: 0.00176705504596

Current iteration: 1887
Current error: 0.00170898123415

Current iteration: 1888
Current error: 0.444105029405

Current iteration: 1889
Current error: 0.00280180273675

Current iteration: 1890
Current error: 0.00268852596059

Current iteration: 1891
Current error: 0.00258007884673

Current iteration: 1892
Current error: 0.00248072160352

Current iteration: 1893
Current error: 0.433283394758

Current iteration: 1894
Current error: 0.00398393508392

Current iteration: 1895
Current error: 0.00379501526508

Current iteration: 1896
Current error: 0.00361831080516

Current iteration: 1897
Current error: 0.00345278836866

Current iteration: 1898
Current error: 0.00329934802365

Current iteration: 1899
Current error: 0.00315482672065

Current iteration: 1900
Current error: 0.00302010822522

Current iteration: 1901
Current error: 0.00289745268593

Current iteration: 1902
Current error: 0.00277315993231

Current iteration: 1903
Current error: 0.429650843179

Current iteration: 1904
Current error: 0.00442580267867

Current iteration: 1905
Current error: 0.00420557780736

Current iteration: 1906
Current error: 0.00400082691166

Current iteration: 1907
Current error: 0.00381029615351

Current iteration: 1908
Current error: 0.00363306207862

Current iteration: 1909
Current error: 0.420118730692

Current iteration: 1910
Current error: 0.00570648383265

Current iteration: 1911
Current error: 0.00538090705874

Current iteration: 1912
Current error: 0.00509111566922

Current iteration: 1913
Current error: 0.00482229933151

Current iteration: 1914
Current error: 0.00457139108711

Current iteration: 1915
Current error: 0.00434126324328

Current iteration: 1916
Current error: 0.00412520048733

Current iteration: 1917
Current error: 0.0039262670184

Current iteration: 1918
Current error: 0.00374126739565

Current iteration: 1919
Current error: 0.0035682310701

Current iteration: 1920
Current error: 0.00340642089075

Current iteration: 1921
Current error: 0.00325542225995

Current iteration: 1922
Current error: 0.00311363147703

Current iteration: 1923
Current error: 0.00298031742688

Current iteration: 1924
Current error: 0.00285928197978

Current iteration: 1925
Current error: 0.00274035184431

Current iteration: 1926
Current error: 0.00262829303043

Current iteration: 1927
Current error: 0.00252477922366

Current iteration: 1928
Current error: 0.00242745667797

Current iteration: 1929
Current error: 0.00233392397753

Current iteration: 1930
Current error: 0.00224699140747

Current iteration: 1931
Current error: 0.00216555296088

Current iteration: 1932
Current error: 0.00208655470464

Current iteration: 1933
Current error: 0.00201136336746

Current iteration: 1934
Current error: 0.43957553025

Current iteration: 1935
Current error: 0.422310159462

Current iteration: 1936
Current error: 0.00538962936456

Current iteration: 1937
Current error: 0.00509682131185

Current iteration: 1938
Current error: 0.406527965267

Current iteration: 1939
Current error: 0.00779680372598

Current iteration: 1940
Current error: 0.00730303064863

Current iteration: 1941
Current error: 0.00685263706868

Current iteration: 1942
Current error: 0.0064417915189

Current iteration: 1943
Current error: 0.00606499812713

Current iteration: 1944
Current error: 0.00571931689613

Current iteration: 1945
Current error: 0.00540048386858

Current iteration: 1946
Current error: 0.00510721278932

Current iteration: 1947
Current error: 0.00483745721296

Current iteration: 1948
Current error: 0.00458686133565

Current iteration: 1949
Current error: 0.00435467987504

Current iteration: 1950
Current error: 0.00414200883896

Current iteration: 1951
Current error: 0.00394041485874

Current iteration: 1952
Current error: 0.00375337469346

Current iteration: 1953
Current error: 0.0035803812289

Current iteration: 1954
Current error: 0.00341668242611

Current iteration: 1955
Current error: 0.00326522712248

Current iteration: 1956
Current error: 0.00312386185441

Current iteration: 1957
Current error: 0.00298912613597

Current iteration: 1958
Current error: 0.00286384337817

Current iteration: 1959
Current error: 0.00274659589925

Current iteration: 1960
Current error: 0.00263634201172

Current iteration: 1961
Current error: 0.00253146462575

Current iteration: 1962
Current error: 0.00243270380936

Current iteration: 1963
Current error: 0.00234001131845

Current iteration: 1964
Current error: 0.0022530649458

Current iteration: 1965
Current error: 0.00217064301657

Current iteration: 1966
Current error: 0.00209113115751

Current iteration: 1967
Current error: 0.00201631928984

Current iteration: 1968
Current error: 0.00194573635553

Current iteration: 1969
Current error: 0.00187861437596

Current iteration: 1970
Current error: 0.00181562505707

Current iteration: 1971
Current error: 0.00175443418587

Current iteration: 1972
Current error: 0.443400976881

Current iteration: 1973
Current error: 0.0028733696284

Current iteration: 1974
Current error: 0.00275426609098

Current iteration: 1975
Current error: 0.00264474262921

Current iteration: 1976
Current error: 0.00253878867638

Current iteration: 1977
Current error: 0.00243991008618

Current iteration: 1978
Current error: 0.0023470078106

Current iteration: 1979
Current error: 0.00225903841669

Current iteration: 1980
Current error: 0.00217525174331

Current iteration: 1981
Current error: 0.002096487103

Current iteration: 1982
Current error: 0.00202188768901

Current iteration: 1983
Current error: 0.0019504179056

Current iteration: 1984
Current error: 0.00188330381118

Current iteration: 1985
Current error: 0.441400101677

Current iteration: 1986
Current error: 0.00307216140984

Current iteration: 1987
Current error: 0.00294202409331

Current iteration: 1988
Current error: 0.00281938164331

Current iteration: 1989
Current error: 0.002704892414

Current iteration: 1990
Current error: 0.00259710433941

Current iteration: 1991
Current error: 0.00249582017791

Current iteration: 1992
Current error: 0.00239802685235

Current iteration: 1993
Current error: 0.00230725975604

Current iteration: 1994
Current error: 0.00222104274103

Current iteration: 1995
Current error: 0.00213999787647

Current iteration: 1996
Current error: 0.00206279949213

Current iteration: 1997
Current error: 0.00198983357413

Current iteration: 1998
Current error: 0.00192048120338

Current iteration: 1999
Current error: 0.00185456825446

Current iteration: 2000
Current error: 0.00179257125676

Current iteration: 2001
Current error: 0.00173244845417

Current iteration: 2002
Current error: 0.00167640275502

Current iteration: 2003
Current error: 0.444657383747

Current iteration: 2004
Current error: 0.00275162772435

Current iteration: 2005
Current error: 0.00264078218456

Current iteration: 2006
Current error: 0.00253624954077

Current iteration: 2007
Current error: 0.00243757867961

Current iteration: 2008
Current error: 0.00234401837104

Current iteration: 2009
Current error: 0.00225705566968

Current iteration: 2010
Current error: 0.00217338637114

Current iteration: 2011
Current error: 0.00209427860714

Current iteration: 2012
Current error: 0.00202004811661

Current iteration: 2013
Current error: 0.0019486489328

Current iteration: 2014
Current error: 0.0018816609454

Current iteration: 2015
Current error: 0.00181775893282

Current iteration: 2016
Current error: 0.00175683860453

Current iteration: 2017
Current error: 0.00169929124049

Current iteration: 2018
Current error: 0.00164555792017

Current iteration: 2019
Current error: 0.00159174980694

Current iteration: 2020
Current error: 0.00154172592772

Current iteration: 2021
Current error: 0.00149392827977

Current iteration: 2022
Current error: 0.00144836663098

Current iteration: 2023
Current error: 0.00140478777546

Current iteration: 2024
Current error: 0.00136581288035

Current iteration: 2025
Current error: 0.0013234123965

Current iteration: 2026
Current error: 0.00128508680049

Current iteration: 2027
Current error: 0.00124840420431

Current iteration: 2028
Current error: 0.00121354721991

Current iteration: 2029
Current error: 0.00117992250214

Current iteration: 2030
Current error: 0.00114753239675

Current iteration: 2031
Current error: 0.00111669973407

Current iteration: 2032
Current error: 0.00108673609503

Current iteration: 2033
Current error: 0.00105907347791

Current iteration: 2034
Current error: 0.00103123732978

Current iteration: 2035
Current error: 0.00100496772193

Current iteration: 2036
Current error: 0.000979243802759

Current iteration: 2037
Current error: 0.000954213859329

Current iteration: 2038
Current error: 0.000931340752726

Current iteration: 2039
Current error: 0.000908054657631

Current iteration: 2040
Current error: 0.000886114127717

Current iteration: 2041
Current error: 0.000865371908004

Current iteration: 2042
Current error: 0.000844935759204

Current iteration: 2043
Current error: 0.000824781370554

Current iteration: 2044
Current error: 0.000805656143925

Current iteration: 2045
Current error: 0.000787397019941

Current iteration: 2046
Current error: 0.000770588650653

Current iteration: 2047
Current error: 0.000752110664799

Current iteration: 2048
Current error: 0.000735538543155

Current iteration: 2049
Current error: 0.000719385869092

Current iteration: 2050
Current error: 0.000703807222982

Current iteration: 2051
Current error: 0.000688917644234

Current iteration: 2052
Current error: 0.000674409401104

Current iteration: 2053
Current error: 0.46428054139

Current iteration: 2054
Current error: 0.00114937457489

Current iteration: 2055
Current error: 0.00111714906417

Current iteration: 2056
Current error: 0.00108712466661

Current iteration: 2057
Current error: 0.00105846222385

Current iteration: 2058
Current error: 0.00103350734422

Current iteration: 2059
Current error: 0.0010048623597

Current iteration: 2060
Current error: 0.000979161991268

Current iteration: 2061
Current error: 0.000954721626148

Current iteration: 2062
Current error: 0.000931408789966

Current iteration: 2063
Current error: 0.000910376722562

Current iteration: 2064
Current error: 0.000886384136172

Current iteration: 2065
Current error: 0.000865199623148

Current iteration: 2066
Current error: 0.000844793038577

Current iteration: 2067
Current error: 0.00082510831056

Current iteration: 2068
Current error: 0.460627206782

Current iteration: 2069
Current error: 0.0013950469529

Current iteration: 2070
Current error: 0.00135522054055

Current iteration: 2071
Current error: 0.00131481452694

Current iteration: 2072
Current error: 0.00127680737048

Current iteration: 2073
Current error: 0.00124046225521

Current iteration: 2074
Current error: 0.452011691758

Current iteration: 2075
Current error: 0.00206362584363

Current iteration: 2076
Current error: 0.00199060728641

Current iteration: 2077
Current error: 0.00192123264006

Current iteration: 2078
Current error: 0.440892368355

Current iteration: 2079
Current error: 0.00313157117871

Current iteration: 2080
Current error: 0.00299701472899

Current iteration: 2081
Current error: 0.00287205809357

Current iteration: 2082
Current error: 0.00275381026381

Current iteration: 2083
Current error: 0.0026427936817

Current iteration: 2084
Current error: 0.00253776909234

Current iteration: 2085
Current error: 0.00243922102558

Current iteration: 2086
Current error: 0.00234654878465

Current iteration: 2087
Current error: 0.00225871273246

Current iteration: 2088
Current error: 0.002174324193

Current iteration: 2089
Current error: 0.00209550242041

Current iteration: 2090
Current error: 0.00202144440196

Current iteration: 2091
Current error: 0.0019526411258

Current iteration: 2092
Current error: 0.00188290956807

Current iteration: 2093
Current error: 0.00181885849393

Current iteration: 2094
Current error: 0.00175834647315

Current iteration: 2095
Current error: 0.00170041920907

Current iteration: 2096
Current error: 0.00164502638297

Current iteration: 2097
Current error: 0.00159288305955

Current iteration: 2098
Current error: 0.00154273555518

Current iteration: 2099
Current error: 0.00149479726975

Current iteration: 2100
Current error: 0.0014504035852

Current iteration: 2101
Current error: 0.00140611146718

Current iteration: 2102
Current error: 0.00136384317636

Current iteration: 2103
Current error: 0.00132383555192

Current iteration: 2104
Current error: 0.00128578944158

Current iteration: 2105
Current error: 0.00124919520753

Current iteration: 2106
Current error: 0.451861161657

Current iteration: 2107
Current error: 0.00207822919169

Current iteration: 2108
Current error: 0.00200439553056

Current iteration: 2109
Current error: 0.00193440224105

Current iteration: 2110
Current error: 0.00186745977471

Current iteration: 2111
Current error: 0.00180466170927

Current iteration: 2112
Current error: 0.00174445904044

Current iteration: 2113
Current error: 0.00168728033342

Current iteration: 2114
Current error: 0.00163278879825

Current iteration: 2115
Current error: 0.445251522116

Current iteration: 2116
Current error: 0.00268279560217

Current iteration: 2117
Current error: 0.00257553150634

Current iteration: 2118
Current error: 0.00247442651609

Current iteration: 2119
Current error: 0.00237966182546

Current iteration: 2120
Current error: 0.43453341035

Current iteration: 2121
Current error: 0.00383216191444

Current iteration: 2122
Current error: 0.00365325637799

Current iteration: 2123
Current error: 0.00348724399871

Current iteration: 2124
Current error: 0.0033313611387

Current iteration: 2125
Current error: 0.00318406954281

Current iteration: 2126
Current error: 0.0030459356725

Current iteration: 2127
Current error: 0.00291767599808

Current iteration: 2128
Current error: 0.00279676561201

Current iteration: 2129
Current error: 0.00268305513224

Current iteration: 2130
Current error: 0.00257720559085

Current iteration: 2131
Current error: 0.00247495801469

Current iteration: 2132
Current error: 0.433304949281

Current iteration: 2133
Current error: 0.00397806291599

Current iteration: 2134
Current error: 0.416667774549

Current iteration: 2135
Current error: 0.00620323360667

Current iteration: 2136
Current error: 0.00584551787912

Current iteration: 2137
Current error: 0.00551448932712

Current iteration: 2138
Current error: 0.00521178009258

Current iteration: 2139
Current error: 0.405552945872

Current iteration: 2140
Current error: 0.00795861806743

Current iteration: 2141
Current error: 0.00745023110442

Current iteration: 2142
Current error: 0.00698818889032

Current iteration: 2143
Current error: 0.00656459858905

Current iteration: 2144
Current error: 0.00617676982712

Current iteration: 2145
Current error: 0.00582253389832

Current iteration: 2146
Current error: 0.00549561270483

Current iteration: 2147
Current error: 0.00519607103471

Current iteration: 2148
Current error: 0.00491918481304

Current iteration: 2149
Current error: 0.40799936443

Current iteration: 2150
Current error: 0.00754321415236

Current iteration: 2151
Current error: 0.00707435489667

Current iteration: 2152
Current error: 0.00664212151184

Current iteration: 2153
Current error: 0.00624762140104

Current iteration: 2154
Current error: 0.00589259308831

Current iteration: 2155
Current error: 0.00555579577893

Current iteration: 2156
Current error: 0.0052522444736

Current iteration: 2157
Current error: 0.00496787239749

Current iteration: 2158
Current error: 0.407579479241

Current iteration: 2159
Current error: 0.00761440747061

Current iteration: 2160
Current error: 0.00713635503705

Current iteration: 2161
Current error: 0.390841131763

Current iteration: 2162
Current error: 0.0106084230296

Current iteration: 2163
Current error: 0.00984663647088

Current iteration: 2164
Current error: 0.00916102791124

Current iteration: 2165
Current error: 0.00854040193002

Current iteration: 2166
Current error: 0.00797933055574

Current iteration: 2167
Current error: 0.00746895417287

Current iteration: 2168
Current error: 0.00700359723884

Current iteration: 2169
Current error: 0.00657941073151

Current iteration: 2170
Current error: 0.00619175820257

Current iteration: 2171
Current error: 0.397719329824

Current iteration: 2172
Current error: 0.00932168180446

Current iteration: 2173
Current error: 0.0086853085274

Current iteration: 2174
Current error: 0.00810901446548

Current iteration: 2175
Current error: 0.00758667799838

Current iteration: 2176
Current error: 0.00711417336236

Current iteration: 2177
Current error: 0.00667761189895

Current iteration: 2178
Current error: 0.00628154577682

Current iteration: 2179
Current error: 0.0059184764004

Current iteration: 2180
Current error: 0.00559292243726

Current iteration: 2181
Current error: 0.00527746251217

Current iteration: 2182
Current error: 0.00499247073831

Current iteration: 2183
Current error: 0.00473109396704

Current iteration: 2184
Current error: 0.00448808100645

Current iteration: 2185
Current error: 0.00426376965046

Current iteration: 2186
Current error: 0.00405490364141

Current iteration: 2187
Current error: 0.00386069164396

Current iteration: 2188
Current error: 0.00367907466963

Current iteration: 2189
Current error: 0.00350972614413

Current iteration: 2190
Current error: 0.00335519411876

Current iteration: 2191
Current error: 0.0032062827325

Current iteration: 2192
Current error: 0.00306623337667

Current iteration: 2193
Current error: 0.0029386023861

Current iteration: 2194
Current error: 0.00281418734753

Current iteration: 2195
Current error: 0.00269937635926

Current iteration: 2196
Current error: 0.0025917489249

Current iteration: 2197
Current error: 0.00248997561708

Current iteration: 2198
Current error: 0.00239755873568

Current iteration: 2199
Current error: 0.00230740580696

Current iteration: 2200
Current error: 0.00221748917385

Current iteration: 2201
Current error: 0.00213628129038

Current iteration: 2202
Current error: 0.00205980347762

Current iteration: 2203
Current error: 0.00198650198069

Current iteration: 2204
Current error: 0.0019174406358

Current iteration: 2205
Current error: 0.00185228598688

Current iteration: 2206
Current error: 0.00178946586668

Current iteration: 2207
Current error: 0.00173021332202

Current iteration: 2208
Current error: 0.443746171603

Current iteration: 2209
Current error: 0.00283460248751

Current iteration: 2210
Current error: 0.0027185341036

Current iteration: 2211
Current error: 0.00260972147469

Current iteration: 2212
Current error: 0.00250736381711

Current iteration: 2213
Current error: 0.00241003708322

Current iteration: 2214
Current error: 0.00231827036078

Current iteration: 2215
Current error: 0.00223179149297

Current iteration: 2216
Current error: 0.00215012073888

Current iteration: 2217
Current error: 0.00207211852699

Current iteration: 2218
Current error: 0.00199879466857

Current iteration: 2219
Current error: 0.00192941263218

Current iteration: 2220
Current error: 0.0018635985553

Current iteration: 2221
Current error: 0.0018005021711

Current iteration: 2222
Current error: 0.00174012022967

Current iteration: 2223
Current error: 0.00168296150081

Current iteration: 2224
Current error: 0.00162927758254

Current iteration: 2225
Current error: 0.00157812253517

Current iteration: 2226
Current error: 0.00152766395599

Current iteration: 2227
Current error: 0.446975210215

Current iteration: 2228
Current error: 0.00251827888867

Current iteration: 2229
Current error: 0.00242144906004

Current iteration: 2230
Current error: 0.00232815794926

Current iteration: 2231
Current error: 0.00224109992944

Current iteration: 2232
Current error: 0.00216236028132

Current iteration: 2233
Current error: 0.00208105586599

Current iteration: 2234
Current error: 0.00200715206787

Current iteration: 2235
Current error: 0.00193658282928

Current iteration: 2236
Current error: 0.00187022154507

Current iteration: 2237
Current error: 0.00180701584545

Current iteration: 2238
Current error: 0.00174661567572

Current iteration: 2239
Current error: 0.00168963909947

Current iteration: 2240
Current error: 0.00163464194619

Current iteration: 2241
Current error: 0.00158276113137

Current iteration: 2242
Current error: 0.00153331707468

Current iteration: 2243
Current error: 0.00148612803881

Current iteration: 2244
Current error: 0.00144071747131

Current iteration: 2245
Current error: 0.00139752864467

Current iteration: 2246
Current error: 0.00135606677364

Current iteration: 2247
Current error: 0.00131622411159

Current iteration: 2248
Current error: 0.00127852656496

Current iteration: 2249
Current error: 0.00124225473331

Current iteration: 2250
Current error: 0.00120783276447

Current iteration: 2251
Current error: 0.00117412728385

Current iteration: 2252
Current error: 0.00114216291785

Current iteration: 2253
Current error: 0.00111131755136

Current iteration: 2254
Current error: 0.00108195061549

Current iteration: 2255
Current error: 0.00105345313269

Current iteration: 2256
Current error: 0.00102612671921

Current iteration: 2257
Current error: 0.000999869471801

Current iteration: 2258
Current error: 0.456739465617

Current iteration: 2259
Current error: 0.00167799386374

Current iteration: 2260
Current error: 0.444532365155

Current iteration: 2261
Current error: 0.00275387054343

Current iteration: 2262
Current error: 0.00264314574054

Current iteration: 2263
Current error: 0.431152934535

Current iteration: 2264
Current error: 0.00422856802927

Current iteration: 2265
Current error: 0.00402535565574

Current iteration: 2266
Current error: 0.0038321461824

Current iteration: 2267
Current error: 0.00365101518073

Current iteration: 2268
Current error: 0.00348398532735

Current iteration: 2269
Current error: 0.00332822338159

Current iteration: 2270
Current error: 0.00318222046599

Current iteration: 2271
Current error: 0.0030446456648

Current iteration: 2272
Current error: 0.00291597853938

Current iteration: 2273
Current error: 0.00279575555167

Current iteration: 2274
Current error: 0.00268179183797

Current iteration: 2275
Current error: 0.00257508518115

Current iteration: 2276
Current error: 0.00247588364483

Current iteration: 2277
Current error: 0.00237977915722

Current iteration: 2278
Current error: 0.00228882071658

Current iteration: 2279
Current error: 0.00220471425616

Current iteration: 2280
Current error: 0.00212421969261

Current iteration: 2281
Current error: 0.00204774371275

Current iteration: 2282
Current error: 0.00197523710746

Current iteration: 2283
Current error: 0.00190673881205

Current iteration: 2284
Current error: 0.00184148491143

Current iteration: 2285
Current error: 0.00178175306158

Current iteration: 2286
Current error: 0.00172073498597

Current iteration: 2287
Current error: 0.0016647466229

Current iteration: 2288
Current error: 0.00161249450386

Current iteration: 2289
Current error: 0.445619907862

Current iteration: 2290
Current error: 0.00265076207497

Current iteration: 2291
Current error: 0.00254408798321

Current iteration: 2292
Current error: 0.00244653905199

Current iteration: 2293
Current error: 0.00235185877484

Current iteration: 2294
Current error: 0.00226366696105

Current iteration: 2295
Current error: 0.00218104614678

Current iteration: 2296
Current error: 0.00210083268143

Current iteration: 2297
Current error: 0.00202692085812

Current iteration: 2298
Current error: 0.00195433974397

Current iteration: 2299
Current error: 0.00188701047258

Current iteration: 2300
Current error: 0.00182386128395

Current iteration: 2301
Current error: 0.00176376222059

Current iteration: 2302
Current error: 0.00170428162712

Current iteration: 2303
Current error: 0.00164855109862

Current iteration: 2304
Current error: 0.00159584153849

Current iteration: 2305
Current error: 0.00154570464419

Current iteration: 2306
Current error: 0.00149795694157

Current iteration: 2307
Current error: 0.00145226949932

Current iteration: 2308
Current error: 0.00140813381551

Current iteration: 2309
Current error: 0.00136802222536

Current iteration: 2310
Current error: 0.0013264275225

Current iteration: 2311
Current error: 0.00128841741632

Current iteration: 2312
Current error: 0.00125143244079

Current iteration: 2313
Current error: 0.00121664342473

Current iteration: 2314
Current error: 0.00118252302065

Current iteration: 2315
Current error: 0.0011503061664

Current iteration: 2316
Current error: 0.00111907747144

Current iteration: 2317
Current error: 0.00108969878041

Current iteration: 2318
Current error: 0.00106081931253

Current iteration: 2319
Current error: 0.455449614823

Current iteration: 2320
Current error: 0.0017757784067

Current iteration: 2321
Current error: 0.00171723571183

Current iteration: 2322
Current error: 0.00166097571625

Current iteration: 2323
Current error: 0.444823109331

Current iteration: 2324
Current error: 0.00273069507899

Current iteration: 2325
Current error: 0.00261767357273

Current iteration: 2326
Current error: 0.00251417485427

Current iteration: 2327
Current error: 0.00241740955979

Current iteration: 2328
Current error: 0.00232606115934

Current iteration: 2329
Current error: 0.00223829513732

Current iteration: 2330
Current error: 0.00215601088931

Current iteration: 2331
Current error: 0.00207810705648

Current iteration: 2332
Current error: 0.00200409500468

Current iteration: 2333
Current error: 0.00193609280443

Current iteration: 2334
Current error: 0.00186879713071

Current iteration: 2335
Current error: 0.441681838707

Current iteration: 2336
Current error: 0.00304804269183

Current iteration: 2337
Current error: 0.00291968700171

Current iteration: 2338
Current error: 0.0027989777519

Current iteration: 2339
Current error: 0.00268757781569

Current iteration: 2340
Current error: 0.0025781039063

Current iteration: 2341
Current error: 0.00247791918275

Current iteration: 2342
Current error: 0.00238141697733

Current iteration: 2343
Current error: 0.00229238292179

Current iteration: 2344
Current error: 0.00220953558607

Current iteration: 2345
Current error: 0.00212597678645

Current iteration: 2346
Current error: 0.0020495116228

Current iteration: 2347
Current error: 0.00197799557135

Current iteration: 2348
Current error: 0.0019103080544

Current iteration: 2349
Current error: 0.00184410082022

Current iteration: 2350
Current error: 0.00178228132954

Current iteration: 2351
Current error: 0.00172262921103

Current iteration: 2352
Current error: 0.00166659555827

Current iteration: 2353
Current error: 0.00161280704046

Current iteration: 2354
Current error: 0.0015619888819

Current iteration: 2355
Current error: 0.00151309848603

Current iteration: 2356
Current error: 0.00146658453621

Current iteration: 2357
Current error: 0.00142247845942

Current iteration: 2358
Current error: 0.00137999071332

Current iteration: 2359
Current error: 0.00133928502653

Current iteration: 2360
Current error: 0.00130054410521

Current iteration: 2361
Current error: 0.00126361329215

Current iteration: 2362
Current error: 0.00122797786995

Current iteration: 2363
Current error: 0.00119337968676

Current iteration: 2364
Current error: 0.00116046340414

Current iteration: 2365
Current error: 0.00112921299496

Current iteration: 2366
Current error: 0.0010990229518

Current iteration: 2367
Current error: 0.00106975648152

Current iteration: 2368
Current error: 0.0010438084654

Current iteration: 2369
Current error: 0.00101531411733

Current iteration: 2370
Current error: 0.000989635151503

Current iteration: 2371
Current error: 0.000964158956787

Current iteration: 2372
Current error: 0.000940419819651

Current iteration: 2373
Current error: 0.000917262774124

Current iteration: 2374
Current error: 0.000894791570277

Current iteration: 2375
Current error: 0.000874324208405

Current iteration: 2376
Current error: 0.000853654947154

Current iteration: 2377
Current error: 0.000832699981465

Current iteration: 2378
Current error: 0.00081336023224

Current iteration: 2379
Current error: 0.000794745989311

Current iteration: 2380
Current error: 0.000776530412569

Current iteration: 2381
Current error: 0.000759126208808

Current iteration: 2382
Current error: 0.00074233202404

Current iteration: 2383
Current error: 0.000726000968197

Current iteration: 2384
Current error: 0.463020306063

Current iteration: 2385
Current error: 0.451417747416

Current iteration: 2386
Current error: 0.00210925771056

Current iteration: 2387
Current error: 0.00203716967145

Current iteration: 2388
Current error: 0.00196227848653

Current iteration: 2389
Current error: 0.00189453322534

Current iteration: 2390
Current error: 0.00182984874383

Current iteration: 2391
Current error: 0.0017687225498

Current iteration: 2392
Current error: 0.00171030283865

Current iteration: 2393
Current error: 0.00165456787264

Current iteration: 2394
Current error: 0.00160254726334

Current iteration: 2395
Current error: 0.00155105319733

Current iteration: 2396
Current error: 0.00150336919992

Current iteration: 2397
Current error: 0.00145741660156

Current iteration: 2398
Current error: 0.00141331067745

Current iteration: 2399
Current error: 0.00137142112604

Current iteration: 2400
Current error: 0.00133131601049

Current iteration: 2401
Current error: 0.00129264245062

Current iteration: 2402
Current error: 0.00125557155425

Current iteration: 2403
Current error: 0.451750400411

Current iteration: 2404
Current error: 0.437357667357

Current iteration: 2405
Current error: 0.00350740435607

Current iteration: 2406
Current error: 0.00335002109795

Current iteration: 2407
Current error: 0.00320505995066

Current iteration: 2408
Current error: 0.00306455836179

Current iteration: 2409
Current error: 0.00293766391108

Current iteration: 2410
Current error: 0.00281250833694

Current iteration: 2411
Current error: 0.00269764302746

Current iteration: 2412
Current error: 0.0025900493568

Current iteration: 2413
Current error: 0.00248818744537

Current iteration: 2414
Current error: 0.00239418276554

Current iteration: 2415
Current error: 0.00230173548257

Current iteration: 2416
Current error: 0.00221603851463

Current iteration: 2417
Current error: 0.00213640648538

Current iteration: 2418
Current error: 0.00205839951164

Current iteration: 2419
Current error: 0.00198630258341

Current iteration: 2420
Current error: 0.00191657306496

Current iteration: 2421
Current error: 0.0018515566296

Current iteration: 2422
Current error: 0.00179298648829

Current iteration: 2423
Current error: 0.00173088575652

Current iteration: 2424
Current error: 0.00167249158026

Current iteration: 2425
Current error: 0.00162037300232

Current iteration: 2426
Current error: 0.00156745111839

Current iteration: 2427
Current error: 0.00152248477647

Current iteration: 2428
Current error: 0.00147333532355

Current iteration: 2429
Current error: 0.44792186131

Current iteration: 2430
Current error: 0.00243093139265

Current iteration: 2431
Current error: 0.00233762943496

Current iteration: 2432
Current error: 0.00225005888602

Current iteration: 2433
Current error: 0.436242515359

Current iteration: 2434
Current error: 0.00363575755886

Current iteration: 2435
Current error: 0.00346994919834

Current iteration: 2436
Current error: 0.00331539789692

Current iteration: 2437
Current error: 0.00317109076325

Current iteration: 2438
Current error: 0.00303247362018

Current iteration: 2439
Current error: 0.00290490334714

Current iteration: 2440
Current error: 0.00278485645404

Current iteration: 2441
Current error: 0.00267251633686

Current iteration: 2442
Current error: 0.00256972891168

Current iteration: 2443
Current error: 0.00246574330324

Current iteration: 2444
Current error: 0.00237058188287

Current iteration: 2445
Current error: 0.00228122701372

Current iteration: 2446
Current error: 0.00219668340266

Current iteration: 2447
Current error: 0.00211871634588

Current iteration: 2448
Current error: 0.00204085475378

Current iteration: 2449
Current error: 0.00196914491462

Current iteration: 2450
Current error: 0.00190076292677

Current iteration: 2451
Current error: 0.00183610968924

Current iteration: 2452
Current error: 0.0017742125301

Current iteration: 2453
Current error: 0.00171647070908

Current iteration: 2454
Current error: 0.00166212937597

Current iteration: 2455
Current error: 0.00160655154543

Current iteration: 2456
Current error: 0.00155684828605

Current iteration: 2457
Current error: 0.00150866590739

Current iteration: 2458
Current error: 0.00146149520283

Current iteration: 2459
Current error: 0.00141866337297

Current iteration: 2460
Current error: 0.00137514644919

Current iteration: 2461
Current error: 0.00133489895246

Current iteration: 2462
Current error: 0.00129607104124

Current iteration: 2463
Current error: 0.00126081209315

Current iteration: 2464
Current error: 0.00122383672146

Current iteration: 2465
Current error: 0.00118950096828

Current iteration: 2466
Current error: 0.00115686419536

Current iteration: 2467
Current error: 0.00112539666975

Current iteration: 2468
Current error: 0.45416790752

Current iteration: 2469
Current error: 0.440450443562

Current iteration: 2470
Current error: 0.00317442590522

Current iteration: 2471
Current error: 0.00303817973813

Current iteration: 2472
Current error: 0.00290612652438

Current iteration: 2473
Current error: 0.00278944366588

Current iteration: 2474
Current error: 0.00267386509603

Current iteration: 2475
Current error: 0.00256604617156

Current iteration: 2476
Current error: 0.00246659193312

Current iteration: 2477
Current error: 0.00237141683055

Current iteration: 2478
Current error: 0.00228274662254

Current iteration: 2479
Current error: 0.00219923355926

Current iteration: 2480
Current error: 0.00211845937018

Current iteration: 2481
Current error: 0.00204154465946

Current iteration: 2482
Current error: 0.00196954204398

Current iteration: 2483
Current error: 0.00190267749846

Current iteration: 2484
Current error: 0.00183702185374

Current iteration: 2485
Current error: 0.00177466955482

Current iteration: 2486
Current error: 0.00171630564046

Current iteration: 2487
Current error: 0.00166058006796

Current iteration: 2488
Current error: 0.00160730145676

Current iteration: 2489
Current error: 0.00155741681631

Current iteration: 2490
Current error: 0.00150805197319

Current iteration: 2491
Current error: 0.00146156575854

Current iteration: 2492
Current error: 0.00141761979242

Current iteration: 2493
Current error: 0.00137540292488

Current iteration: 2494
Current error: 0.00133492542713

Current iteration: 2495
Current error: 0.00129696211476

Current iteration: 2496
Current error: 0.00125928452116

Current iteration: 2497
Current error: 0.00122370967051

Current iteration: 2498
Current error: 0.00118983954628

Current iteration: 2499
Current error: 0.0011572377811

Current iteration: 2500
Current error: 0.00112587724895

Current iteration: 2501
Current error: 0.0010960162141

Current iteration: 2502
Current error: 0.00106663578023

Current iteration: 2503
Current error: 0.00103885840203

Current iteration: 2504
Current error: 0.00101251714394

Current iteration: 2505
Current error: 0.000986425479473

Current iteration: 2506
Current error: 0.000961452800833

Current iteration: 2507
Current error: 0.000938118570841

Current iteration: 2508
Current error: 0.000914734686743

Current iteration: 2509
Current error: 0.000892481677568

Current iteration: 2510
Current error: 0.00087283193863

Current iteration: 2511
Current error: 0.000850473638712

Current iteration: 2512
Current error: 0.000830382265498

Current iteration: 2513
Current error: 0.00081117941755

Current iteration: 2514
Current error: 0.00079258998045

Current iteration: 2515
Current error: 0.461294521422

Current iteration: 2516
Current error: 0.00134258683401

Current iteration: 2517
Current error: 0.00130289614517

Current iteration: 2518
Current error: 0.00126549970917

Current iteration: 2519
Current error: 0.00122968426648

Current iteration: 2520
Current error: 0.00119551859248

Current iteration: 2521
Current error: 0.00116274426134

Current iteration: 2522
Current error: 0.00113106537503

Current iteration: 2523
Current error: 0.00110107884776

Current iteration: 2524
Current error: 0.00107152994909

Current iteration: 2525
Current error: 0.0010439721983

Current iteration: 2526
Current error: 0.00101661630308

Current iteration: 2527
Current error: 0.00099093632775

Current iteration: 2528
Current error: 0.000966077346377

Current iteration: 2529
Current error: 0.000943568172353

Current iteration: 2530
Current error: 0.000919157299674

Current iteration: 2531
Current error: 0.00089621634466

Current iteration: 2532
Current error: 0.458983916746

Current iteration: 2533
Current error: 0.00151182533047

Current iteration: 2534
Current error: 0.00146433565822

Current iteration: 2535
Current error: 0.00142030608175

Current iteration: 2536
Current error: 0.00137794917148

Current iteration: 2537
Current error: 0.00133818647924

Current iteration: 2538
Current error: 0.00129884063597

Current iteration: 2539
Current error: 0.00126151635688

Current iteration: 2540
Current error: 0.00122603568056

Current iteration: 2541
Current error: 0.00119173167828

Current iteration: 2542
Current error: 0.00115968939817

Current iteration: 2543
Current error: 0.00112746451615

Current iteration: 2544
Current error: 0.00109743935168

Current iteration: 2545
Current error: 0.0010701498483

Current iteration: 2546
Current error: 0.00104113003432

Current iteration: 2547
Current error: 0.00101423028335

Current iteration: 2548
Current error: 0.000987825053515

Current iteration: 2549
Current error: 0.000963081592814

Current iteration: 2550
Current error: 0.45751859177

Current iteration: 2551
Current error: 0.00161945319556

Current iteration: 2552
Current error: 0.00156773976417

Current iteration: 2553
Current error: 0.0015186781616

Current iteration: 2554
Current error: 0.00147209991785

Current iteration: 2555
Current error: 0.00142750266897

Current iteration: 2556
Current error: 0.00138513060497

Current iteration: 2557
Current error: 0.00134381612956

Current iteration: 2558
Current error: 0.00130507682565

Current iteration: 2559
Current error: 0.00126757287125

Current iteration: 2560
Current error: 0.00123157584886

Current iteration: 2561
Current error: 0.00119774095395

Current iteration: 2562
Current error: 0.00116440121797

Current iteration: 2563
Current error: 0.00113434883738

Current iteration: 2564
Current error: 0.00110233539868

Current iteration: 2565
Current error: 0.00107319302711

Current iteration: 2566
Current error: 0.00104546740649

Current iteration: 2567
Current error: 0.00101801509089

Current iteration: 2568
Current error: 0.000992121488333

Current iteration: 2569
Current error: 0.000967125258571

Current iteration: 2570
Current error: 0.000943706386827

Current iteration: 2571
Current error: 0.000921342468993

Current iteration: 2572
Current error: 0.000897585798962

Current iteration: 2573
Current error: 0.000875793365306

Current iteration: 2574
Current error: 0.000855024170626

Current iteration: 2575
Current error: 0.000835963754089

Current iteration: 2576
Current error: 0.00081574547502

Current iteration: 2577
Current error: 0.000797066824955

Current iteration: 2578
Current error: 0.000778767452401

Current iteration: 2579
Current error: 0.000761395157087

Current iteration: 2580
Current error: 0.000744152237407

Current iteration: 2581
Current error: 0.000728083473485

Current iteration: 2582
Current error: 0.00071227242564

Current iteration: 2583
Current error: 0.000696694928968

Current iteration: 2584
Current error: 0.000681814122408

Current iteration: 2585
Current error: 0.000667437207901

Current iteration: 2586
Current error: 0.000653665860811

Current iteration: 2587
Current error: 0.000640436855688

Current iteration: 2588
Current error: 0.000626765128501

Current iteration: 2589
Current error: 0.000614132805719

Current iteration: 2590
Current error: 0.00060177728483

Current iteration: 2591
Current error: 0.000589949798555

Current iteration: 2592
Current error: 0.000578736047818

Current iteration: 2593
Current error: 0.000567045749564

Current iteration: 2594
Current error: 0.467149762237

Current iteration: 2595
Current error: 0.000970637709055

Current iteration: 2596
Current error: 0.000946489210154

Current iteration: 2597
Current error: 0.000923586209088

Current iteration: 2598
Current error: 0.000900487762874

Current iteration: 2599
Current error: 0.000878713456408

Current iteration: 2600
Current error: 0.000858598606626

Current iteration: 2601
Current error: 0.000837684016164

Current iteration: 2602
Current error: 0.000818203348429

Current iteration: 2603
Current error: 0.000799436390426

Current iteration: 2604
Current error: 0.000783305947734

Current iteration: 2605
Current error: 0.000763900167516

Current iteration: 2606
Current error: 0.00074682326917

Current iteration: 2607
Current error: 0.000730575688143

Current iteration: 2608
Current error: 0.000714340015732

Current iteration: 2609
Current error: 0.000699238537486

Current iteration: 2610
Current error: 0.000683950098087

Current iteration: 2611
Current error: 0.000669862820379

Current iteration: 2612
Current error: 0.000655790949437

Current iteration: 2613
Current error: 0.000641726240704

Current iteration: 2614
Current error: 0.00062872857236

Current iteration: 2615
Current error: 0.000616745603293

Current iteration: 2616
Current error: 0.000603527190218

Current iteration: 2617
Current error: 0.000591470154989

Current iteration: 2618
Current error: 0.000580674335138

Current iteration: 2619
Current error: 0.000568380955218

Current iteration: 2620
Current error: 0.000557429715536

Current iteration: 2621
Current error: 0.000546780210839

Current iteration: 2622
Current error: 0.000536940418425

Current iteration: 2623
Current error: 0.000526452547871

Current iteration: 2624
Current error: 0.468331394766

Current iteration: 2625
Current error: 0.000903140346187

Current iteration: 2626
Current error: 0.00088125795051

Current iteration: 2627
Current error: 0.00086012418959

Current iteration: 2628
Current error: 0.00083997544014

Current iteration: 2629
Current error: 0.460160651455

Current iteration: 2630
Current error: 0.448150159489

Current iteration: 2631
Current error: 0.00241707298552

Current iteration: 2632
Current error: 0.00232497179054

Current iteration: 2633
Current error: 0.00223831194485

Current iteration: 2634
Current error: 0.00215616192889

Current iteration: 2635
Current error: 0.00207844662799

Current iteration: 2636
Current error: 0.00200473178836

Current iteration: 2637
Current error: 0.00193394116721

Current iteration: 2638
Current error: 0.00186873945854

Current iteration: 2639
Current error: 0.00180437091337

Current iteration: 2640
Current error: 0.00174455902317

Current iteration: 2641
Current error: 0.0016873118917

Current iteration: 2642
Current error: 0.00163273549226

Current iteration: 2643
Current error: 0.00158113832295

Current iteration: 2644
Current error: 0.00153268411041

Current iteration: 2645
Current error: 0.00148405930444

Current iteration: 2646
Current error: 0.00143904693055

Current iteration: 2647
Current error: 0.00139862137171

Current iteration: 2648
Current error: 0.00135689247748

Current iteration: 2649
Current error: 0.00131505029867

Current iteration: 2650
Current error: 0.00127709235877

Current iteration: 2651
Current error: 0.00124104479657

Current iteration: 2652
Current error: 0.00120765568482

Current iteration: 2653
Current error: 0.00117271174329

Current iteration: 2654
Current error: 0.0011409902758

Current iteration: 2655
Current error: 0.00111107105945

Current iteration: 2656
Current error: 0.00108051110619

Current iteration: 2657
Current error: 0.0010534911449

Current iteration: 2658
Current error: 0.00102516469778

Current iteration: 2659
Current error: 0.000999613644582

Current iteration: 2660
Current error: 0.000973623807705

Current iteration: 2661
Current error: 0.000949796154002

Current iteration: 2662
Current error: 0.000925812381429

Current iteration: 2663
Current error: 0.000903229438773

Current iteration: 2664
Current error: 0.000881413564765

Current iteration: 2665
Current error: 0.000860450746601

Current iteration: 2666
Current error: 0.000840184864646

Current iteration: 2667
Current error: 0.0008210443744

Current iteration: 2668
Current error: 0.000802547427148

Current iteration: 2669
Current error: 0.000784509432224

Current iteration: 2670
Current error: 0.000765595689412

Current iteration: 2671
Current error: 0.000748577062439

Current iteration: 2672
Current error: 0.000732136229498

Current iteration: 2673
Current error: 0.000716039419493

Current iteration: 2674
Current error: 0.00070078007838

Current iteration: 2675
Current error: 0.000686112437228

Current iteration: 2676
Current error: 0.000671401299697

Current iteration: 2677
Current error: 0.000657086358376

Current iteration: 2678
Current error: 0.000643509506335

Current iteration: 2679
Current error: 0.000630250227427

Current iteration: 2680
Current error: 0.000617388784108

Current iteration: 2681
Current error: 0.000604946742515

Current iteration: 2682
Current error: 0.000592945701528

Current iteration: 2683
Current error: 0.466420037456

Current iteration: 2684
Current error: 0.00101351379405

Current iteration: 2685
Current error: 0.000987718305307

Current iteration: 2686
Current error: 0.000963436016109

Current iteration: 2687
Current error: 0.000938921068183

Current iteration: 2688
Current error: 0.000916026457384

Current iteration: 2689
Current error: 0.458512289189

Current iteration: 2690
Current error: 0.00154271842986

Current iteration: 2691
Current error: 0.00149458784309

Current iteration: 2692
Current error: 0.00144900940758

Current iteration: 2693
Current error: 0.00140599910199

Current iteration: 2694
Current error: 0.00136398691758

Current iteration: 2695
Current error: 0.00132416413158

Current iteration: 2696
Current error: 0.00128574582646

Current iteration: 2697
Current error: 0.00124916245631

Current iteration: 2698
Current error: 0.00121460499679

Current iteration: 2699
Current error: 0.0011804169593

Current iteration: 2700
Current error: 0.00114896204039

Current iteration: 2701
Current error: 0.00111701650412

Current iteration: 2702
Current error: 0.00108741452153

Current iteration: 2703
Current error: 0.00105886851535

Current iteration: 2704
Current error: 0.00103101803175

Current iteration: 2705
Current error: 0.00100498062352

Current iteration: 2706
Current error: 0.000979291284812

Current iteration: 2707
Current error: 0.000955063249074

Current iteration: 2708
Current error: 0.000931375591352

Current iteration: 2709
Current error: 0.000908179602381

Current iteration: 2710
Current error: 0.000886744978394

Current iteration: 2711
Current error: 0.000866811463799

Current iteration: 2712
Current error: 0.000845460667206

Current iteration: 2713
Current error: 0.000825278044946

Current iteration: 2714
Current error: 0.000806002165389

Current iteration: 2715
Current error: 0.000787693366589

Current iteration: 2716
Current error: 0.000769681479812

Current iteration: 2717
Current error: 0.000752565873081

Current iteration: 2718
Current error: 0.462292239994

Current iteration: 2719
Current error: 0.00127680161219

Current iteration: 2720
Current error: 0.00124060843638

Current iteration: 2721
Current error: 0.452063966259

Current iteration: 2722
Current error: 0.00206402451931

Current iteration: 2723
Current error: 0.00199110368654

Current iteration: 2724
Current error: 0.00192139257961

Current iteration: 2725
Current error: 0.00185641965872

Current iteration: 2726
Current error: 0.0017933627417

Current iteration: 2727
Current error: 0.0017336882348

Current iteration: 2728
Current error: 0.001676756685

Current iteration: 2729
Current error: 0.00162290176042

Current iteration: 2730
Current error: 0.00157144050192

Current iteration: 2731
Current error: 0.00152260658958

Current iteration: 2732
Current error: 0.00147549417719

Current iteration: 2733
Current error: 0.00143062593953

Current iteration: 2734
Current error: 0.00138812472913

Current iteration: 2735
Current error: 0.0013469353052

Current iteration: 2736
Current error: 0.00130772542393

Current iteration: 2737
Current error: 0.00127082727052

Current iteration: 2738
Current error: 0.00123513619882

Current iteration: 2739
Current error: 0.00120022734289

Current iteration: 2740
Current error: 0.00116682104373

Current iteration: 2741
Current error: 0.00113586303137

Current iteration: 2742
Current error: 0.00110484220408

Current iteration: 2743
Current error: 0.00107520247691

Current iteration: 2744
Current error: 0.00104718739404

Current iteration: 2745
Current error: 0.00102021544864

Current iteration: 2746
Current error: 0.000994045810324

Current iteration: 2747
Current error: 0.000969622768841

Current iteration: 2748
Current error: 0.000945835076658

Current iteration: 2749
Current error: 0.000921523016606

Current iteration: 2750
Current error: 0.000899571111623

Current iteration: 2751
Current error: 0.00087746078261

Current iteration: 2752
Current error: 0.000856572681982

Current iteration: 2753
Current error: 0.000837054776575

Current iteration: 2754
Current error: 0.000816896452407

Current iteration: 2755
Current error: 0.000798211517648

Current iteration: 2756
Current error: 0.000779939900977

Current iteration: 2757
Current error: 0.461638857963

Current iteration: 2758
Current error: 0.0013215702689

Current iteration: 2759
Current error: 0.00128321116334

Current iteration: 2760
Current error: 0.0012469512663

Current iteration: 2761
Current error: 0.00121177120511

Current iteration: 2762
Current error: 0.452552167762

Current iteration: 2763
Current error: 0.00201858737206

Current iteration: 2764
Current error: 0.00194783374567

Current iteration: 2765
Current error: 0.00188218490136

Current iteration: 2766
Current error: 0.0018172407512

Current iteration: 2767
Current error: 0.00175664146774

Current iteration: 2768
Current error: 0.00169995450249

Current iteration: 2769
Current error: 0.444223337612

Current iteration: 2770
Current error: 0.0027851804571

Current iteration: 2771
Current error: 0.00267184378432

Current iteration: 2772
Current error: 0.00256573906885

Current iteration: 2773
Current error: 0.00246587360812

Current iteration: 2774
Current error: 0.00237114799293

Current iteration: 2775
Current error: 0.00228109362349

Current iteration: 2776
Current error: 0.00219834727047

Current iteration: 2777
Current error: 0.00211692904234

Current iteration: 2778
Current error: 0.00204078295236

Current iteration: 2779
Current error: 0.0019707387622

Current iteration: 2780
Current error: 0.00190056415847

Current iteration: 2781
Current error: 0.00183581639633

Current iteration: 2782
Current error: 0.00177426672403

Current iteration: 2783
Current error: 0.00171587468943

Current iteration: 2784
Current error: 0.00166305828299

Current iteration: 2785
Current error: 0.00160643816743

Current iteration: 2786
Current error: 0.00155604438965

Current iteration: 2787
Current error: 0.00150757421859

Current iteration: 2788
Current error: 0.00146183804325

Current iteration: 2789
Current error: 0.00141728280942

Current iteration: 2790
Current error: 0.00137516420657

Current iteration: 2791
Current error: 0.00133463259208

Current iteration: 2792
Current error: 0.00129625195528

Current iteration: 2793
Current error: 0.00125905652685

Current iteration: 2794
Current error: 0.00122351795381

Current iteration: 2795
Current error: 0.00118954678701

Current iteration: 2796
Current error: 0.00115676894332

Current iteration: 2797
Current error: 0.00112549032904

Current iteration: 2798
Current error: 0.00109561876264

Current iteration: 2799
Current error: 0.454800599957

Current iteration: 2800
Current error: 0.00183186157177

Current iteration: 2801
Current error: 0.00177056415376

Current iteration: 2802
Current error: 0.00171674366626

Current iteration: 2803
Current error: 0.00165681910981

Current iteration: 2804
Current error: 0.00160354094986

Current iteration: 2805
Current error: 0.001552758462

Current iteration: 2806
Current error: 0.00150495705142

Current iteration: 2807
Current error: 0.00145845758632

Current iteration: 2808
Current error: 0.00141441285437

Current iteration: 2809
Current error: 0.00137238169877

Current iteration: 2810
Current error: 0.00133498126066

Current iteration: 2811
Current error: 0.001293911614

Current iteration: 2812
Current error: 0.0012567722396

Current iteration: 2813
Current error: 0.0012225813408

Current iteration: 2814
Current error: 0.00119009891549

Current iteration: 2815
Current error: 0.00115491525972

Current iteration: 2816
Current error: 0.00112358246667

Current iteration: 2817
Current error: 0.00109340392008

Current iteration: 2818
Current error: 0.00106464795333

Current iteration: 2819
Current error: 0.00103687170629

Current iteration: 2820
Current error: 0.0010102724761

Current iteration: 2821
Current error: 0.000985835874769

Current iteration: 2822
Current error: 0.000960226721554

Current iteration: 2823
Current error: 0.000936129887111

Current iteration: 2824
Current error: 0.000913055990809

Current iteration: 2825
Current error: 0.000891095708951

Current iteration: 2826
Current error: 0.000869575116936

Current iteration: 2827
Current error: 0.000849044352077

Current iteration: 2828
Current error: 0.000829274920052

Current iteration: 2829
Current error: 0.000810014668345

Current iteration: 2830
Current error: 0.000791469313138

Current iteration: 2831
Current error: 0.000773536831683

Current iteration: 2832
Current error: 0.000756103590471

Current iteration: 2833
Current error: 0.000739731981624

Current iteration: 2834
Current error: 0.000723068649739

Current iteration: 2835
Current error: 0.463022465714

Current iteration: 2836
Current error: 0.00122839922339

Current iteration: 2837
Current error: 0.00119422980343

Current iteration: 2838
Current error: 0.00116237025985

Current iteration: 2839
Current error: 0.00113149440917

Current iteration: 2840
Current error: 0.00109928671238

Current iteration: 2841
Current error: 0.00107034126261

Current iteration: 2842
Current error: 0.00104232150659

Current iteration: 2843
Current error: 0.00101543176265

Current iteration: 2844
Current error: 0.000989550233772

Current iteration: 2845
Current error: 0.000964871103474

Current iteration: 2846
Current error: 0.000940801428406

Current iteration: 2847
Current error: 0.000918274325838

Current iteration: 2848
Current error: 0.000895388693066

Current iteration: 2849
Current error: 0.000874632190941

Current iteration: 2850
Current error: 0.000852979951276

Current iteration: 2851
Current error: 0.000833711647465

Current iteration: 2852
Current error: 0.000813708362669

Current iteration: 2853
Current error: 0.000794945887391

Current iteration: 2854
Current error: 0.000777041649243

Current iteration: 2855
Current error: 0.000759643263219

Current iteration: 2856
Current error: 0.000742704579717

Current iteration: 2857
Current error: 0.000726371264677

Current iteration: 2858
Current error: 0.000713006364795

Current iteration: 2859
Current error: 0.000695204285202

Current iteration: 2860
Current error: 0.000680529908728

Current iteration: 2861
Current error: 0.000666706532624

Current iteration: 2862
Current error: 0.000652240719434

Current iteration: 2863
Current error: 0.000638685045984

Current iteration: 2864
Current error: 0.000625670124087

Current iteration: 2865
Current error: 0.000613017486684

Current iteration: 2866
Current error: 0.000600689497365

Current iteration: 2867
Current error: 0.000589209990915

Current iteration: 2868
Current error: 0.000577224199826

Current iteration: 2869
Current error: 0.00056594844527

Current iteration: 2870
Current error: 0.000554951582517

Current iteration: 2871
Current error: 0.000544313196787

Current iteration: 2872
Current error: 0.000534505527561

Current iteration: 2873
Current error: 0.000524190038527

Current iteration: 2874
Current error: 0.000514222365822

Current iteration: 2875
Current error: 0.000504781955503

Current iteration: 2876
Current error: 0.000495514454613

Current iteration: 2877
Current error: 0.000486496581836

Current iteration: 2878
Current error: 0.000477721320181

Current iteration: 2879
Current error: 0.46975288095

Current iteration: 2880
Current error: 0.000822513208781

Current iteration: 2881
Current error: 0.000802695144682

Current iteration: 2882
Current error: 0.00078446201359

Current iteration: 2883
Current error: 0.000766808304854

Current iteration: 2884
Current error: 0.000749856676914

Current iteration: 2885
Current error: 0.000733420737906

Current iteration: 2886
Current error: 0.000717984963837

Current iteration: 2887
Current error: 0.000701677996883

Current iteration: 2888
Current error: 0.000686509612582

Current iteration: 2889
Current error: 0.00067204386399

Current iteration: 2890
Current error: 0.00065793238605

Current iteration: 2891
Current error: 0.000644481932856

Current iteration: 2892
Current error: 0.000631424822639

Current iteration: 2893
Current error: 0.000618707260317

Current iteration: 2894
Current error: 0.000605853654605

Current iteration: 2895
Current error: 0.000593633399321

Current iteration: 2896
Current error: 0.000581972002149

Current iteration: 2897
Current error: 0.000570640973359

Current iteration: 2898
Current error: 0.000559508483408

Current iteration: 2899
Current error: 0.000549877603117

Current iteration: 2900
Current error: 0.000538295355672

Current iteration: 2901
Current error: 0.000528172313612

Current iteration: 2902
Current error: 0.000518204397005

Current iteration: 2903
Current error: 0.000508702934932

Current iteration: 2904
Current error: 0.000499354469542

Current iteration: 2905
Current error: 0.000490251442244

Current iteration: 2906
Current error: 0.000481482401729

Current iteration: 2907
Current error: 0.000472836099664

Current iteration: 2908
Current error: 0.00046478449736

Current iteration: 2909
Current error: 0.000456270203085

Current iteration: 2910
Current error: 0.000448298910762

Current iteration: 2911
Current error: 0.000440550190319

Current iteration: 2912
Current error: 0.000433328511225

Current iteration: 2913
Current error: 0.000425666815933

Current iteration: 2914
Current error: 0.000418590594785

Current iteration: 2915
Current error: 0.000411485818415

Current iteration: 2916
Current error: 0.000404727362294

Current iteration: 2917
Current error: 0.000398082738771

Current iteration: 2918
Current error: 0.000391524763713

Current iteration: 2919
Current error: 0.0003854148511

Current iteration: 2920
Current error: 0.000379029915879

Current iteration: 2921
Current error: 0.000372932302874

Current iteration: 2922
Current error: 0.000367070532507

Current iteration: 2923
Current error: 0.000361646425438

Current iteration: 2924
Current error: 0.000355673633078

Current iteration: 2925
Current error: 0.000350218454662

Current iteration: 2926
Current error: 0.000344962726096

Current iteration: 2927
Current error: 0.000339614599662

Current iteration: 2928
Current error: 0.000334509938321

Current iteration: 2929
Current error: 0.000329381612375

Current iteration: 2930
Current error: 0.000324641510679

Current iteration: 2931
Current error: 0.000319979247894

Current iteration: 2932
Current error: 0.000316631960624

Current iteration: 2933
Current error: 0.475344562125

Current iteration: 2934
Current error: 0.000547636500038

Current iteration: 2935
Current error: 0.000537162101612

Current iteration: 2936
Current error: 0.000527155244311

Current iteration: 2937
Current error: 0.000517216495164

Current iteration: 2938
Current error: 0.000507854479914

Current iteration: 2939
Current error: 0.000499676866982

Current iteration: 2940
Current error: 0.000489305057695

Current iteration: 2941
Current error: 0.000480572400606

Current iteration: 2942
Current error: 0.000471912761536

Current iteration: 2943
Current error: 0.000463523432825

Current iteration: 2944
Current error: 0.000456183473632

Current iteration: 2945
Current error: 0.000447452306843

Current iteration: 2946
Current error: 0.000439740993762

Current iteration: 2947
Current error: 0.000432524701595

Current iteration: 2948
Current error: 0.000424908517309

Current iteration: 2949
Current error: 0.000417722032458

Current iteration: 2950
Current error: 0.000410913966796

Current iteration: 2951
Current error: 0.000404138447657

Current iteration: 2952
Current error: 0.000397591590783

Current iteration: 2953
Current error: 0.000390950038335

Current iteration: 2954
Current error: 0.472476184272

Current iteration: 2955
Current error: 0.000675677764112

Current iteration: 2956
Current error: 0.000661271625445

Current iteration: 2957
Current error: 0.000647470585583

Current iteration: 2958
Current error: 0.00063401095346

Current iteration: 2959
Current error: 0.46520618425

Current iteration: 2960
Current error: 0.00108106634248

Current iteration: 2961
Current error: 0.0010526051381

Current iteration: 2962
Current error: 0.45566516942

Current iteration: 2963
Current error: 0.00176361889728

Current iteration: 2964
Current error: 0.00170562297231

Current iteration: 2965
Current error: 0.00165011104222

Current iteration: 2966
Current error: 0.0015975824557

Current iteration: 2967
Current error: 0.00154910353238

Current iteration: 2968
Current error: 0.00149929220304

Current iteration: 2969
Current error: 0.00145524093786

Current iteration: 2970
Current error: 0.00140949322105

Current iteration: 2971
Current error: 0.00136785539696

Current iteration: 2972
Current error: 0.00132845645589

Current iteration: 2973
Current error: 0.00128961214558

Current iteration: 2974
Current error: 0.00125284146594

Current iteration: 2975
Current error: 0.00121726141937

Current iteration: 2976
Current error: 0.452448924454

Current iteration: 2977
Current error: 0.00202761810517

Current iteration: 2978
Current error: 0.00195568660334

Current iteration: 2979
Current error: 0.00188867839289

Current iteration: 2980
Current error: 0.00182390250333

Current iteration: 2981
Current error: 0.00176402148013

Current iteration: 2982
Current error: 0.00170511535378

Current iteration: 2983
Current error: 0.00165072776015

Current iteration: 2984
Current error: 0.00159697633357

Current iteration: 2985
Current error: 0.00154994580514

Current iteration: 2986
Current error: 0.00149869943102

Current iteration: 2987
Current error: 0.00145303424052

Current iteration: 2988
Current error: 0.00140902118005

Current iteration: 2989
Current error: 0.00136742464852

Current iteration: 2990
Current error: 0.00132712610035

Current iteration: 2991
Current error: 0.00128891628358

Current iteration: 2992
Current error: 0.00125261561929

Current iteration: 2993
Current error: 0.00121697373383

Current iteration: 2994
Current error: 0.00118349176181

Current iteration: 2995
Current error: 0.00115070566114

Current iteration: 2996
Current error: 0.453717135568

Current iteration: 2997
Current error: 0.00192352707068

Current iteration: 2998
Current error: 0.00185490683305

Current iteration: 2999
Current error: 0.00179397463908

Current iteration: 3000
Current error: 0.00173289096917

Current iteration: 3001
Current error: 0.00167686532521

Current iteration: 3002
Current error: 0.00162279492926

Current iteration: 3003
Current error: 0.00157138516679

Current iteration: 3004
Current error: 0.00152196156527

Current iteration: 3005
Current error: 0.00147549333272

Current iteration: 3006
Current error: 0.00143057760071

Current iteration: 3007
Current error: 0.00138789153069

Current iteration: 3008
Current error: 0.0013501779967

Current iteration: 3009
Current error: 0.00130733595598

Current iteration: 3010
Current error: 0.00127010619304

Current iteration: 3011
Current error: 0.00123427217197

Current iteration: 3012
Current error: 0.00119966951382

Current iteration: 3013
Current error: 0.452752655683

Current iteration: 3014
Current error: 0.00199892451993

Current iteration: 3015
Current error: 0.00193230896688

Current iteration: 3016
Current error: 0.00186236378956

Current iteration: 3017
Current error: 0.441699182975

Current iteration: 3018
Current error: 0.00303998357652

Current iteration: 3019
Current error: 0.0029113819079

Current iteration: 3020
Current error: 0.00279118724049

Current iteration: 3021
Current error: 0.00267995984936

Current iteration: 3022
Current error: 0.00257123492498

Current iteration: 3023
Current error: 0.00247312342776

Current iteration: 3024
Current error: 0.00237553429774

Current iteration: 3025
Current error: 0.00228699116914

Current iteration: 3026
Current error: 0.00220081053936

Current iteration: 3027
Current error: 0.00212095381878

Current iteration: 3028
Current error: 0.00204492112691

Current iteration: 3029
Current error: 0.00197287489401

Current iteration: 3030
Current error: 0.440101264772

Current iteration: 3031
Current error: 0.422884602033

Current iteration: 3032
Current error: 0.402244788809

Current iteration: 3033
Current error: 0.00850100404384

Current iteration: 3034
Current error: 0.0079486893295

Current iteration: 3035
Current error: 0.38514118887

Current iteration: 3036
Current error: 0.0116810791115

Current iteration: 3037
Current error: 0.01081007276

Current iteration: 3038
Current error: 0.0100286652139

Current iteration: 3039
Current error: 0.00932584468296

Current iteration: 3040
Current error: 0.00868858850833

Current iteration: 3041
Current error: 0.00811302957761

Current iteration: 3042
Current error: 0.00759106908415

Current iteration: 3043
Current error: 0.387544694051

Current iteration: 3044
Current error: 0.0112149165442

Current iteration: 3045
Current error: 0.0103916613553

Current iteration: 3046
Current error: 0.00965187795182

Current iteration: 3047
Current error: 0.00898366337715

Current iteration: 3048
Current error: 0.00838163269106

Current iteration: 3049
Current error: 0.382472085687

Current iteration: 3050
Current error: 0.0122750247554

Current iteration: 3051
Current error: 0.0113376713352

Current iteration: 3052
Current error: 0.0105041497791

Current iteration: 3053
Current error: 0.00976637168758

Current iteration: 3054
Current error: 0.00907438892967

Current iteration: 3055
Current error: 0.00846234341734

Current iteration: 3056
Current error: 0.00791720237584

Current iteration: 3057
Current error: 0.00740694039084

Current iteration: 3058
Current error: 0.00694611934672

Current iteration: 3059
Current error: 0.00652535347216

Current iteration: 3060
Current error: 0.00614362927896

Current iteration: 3061
Current error: 0.00579299903234

Current iteration: 3062
Current error: 0.00547120703198

Current iteration: 3063
Current error: 0.00516747605485

Current iteration: 3064
Current error: 0.405702664133

Current iteration: 3065
Current error: 0.00788945423579

Current iteration: 3066
Current error: 0.00738711621978

Current iteration: 3067
Current error: 0.00692953205866

Current iteration: 3068
Current error: 0.00651157685612

Current iteration: 3069
Current error: 0.00612989235316

Current iteration: 3070
Current error: 0.00577911973491

Current iteration: 3071
Current error: 0.00545511571592

Current iteration: 3072
Current error: 0.00515776541322

Current iteration: 3073
Current error: 0.00488379632798

Current iteration: 3074
Current error: 0.408196650494

Current iteration: 3075
Current error: 0.00749515474044

Current iteration: 3076
Current error: 0.00702429492281

Current iteration: 3077
Current error: 0.00661132215925

Current iteration: 3078
Current error: 0.00620886393498

Current iteration: 3079
Current error: 0.00585556648232

Current iteration: 3080
Current error: 0.00552199536807

Current iteration: 3081
Current error: 0.00521981705536

Current iteration: 3082
Current error: 0.00494077282163

Current iteration: 3083
Current error: 0.00468597682827

Current iteration: 3084
Current error: 0.00444351247966

Current iteration: 3085
Current error: 0.00422120773346

Current iteration: 3086
Current error: 0.00401528957289

Current iteration: 3087
Current error: 0.00382413346724

Current iteration: 3088
Current error: 0.00364570132772

Current iteration: 3089
Current error: 0.00347827825545

Current iteration: 3090
Current error: 0.00332263569032

Current iteration: 3091
Current error: 0.00317670457985

Current iteration: 3092
Current error: 0.0030404154561

Current iteration: 3093
Current error: 0.00291191723977

Current iteration: 3094
Current error: 0.00279255126062

Current iteration: 3095
Current error: 0.00267824780769

Current iteration: 3096
Current error: 0.430699752281

Current iteration: 3097
Current error: 0.00428224815215

Current iteration: 3098
Current error: 0.00407231740549

Current iteration: 3099
Current error: 0.00387746254806

Current iteration: 3100
Current error: 0.00369401403312

Current iteration: 3101
Current error: 0.419298703843

Current iteration: 3102
Current error: 0.00578230802768

Current iteration: 3103
Current error: 0.00546002667495

Current iteration: 3104
Current error: 0.00516165878401

Current iteration: 3105
Current error: 0.00488760859915

Current iteration: 3106
Current error: 0.00463310061135

Current iteration: 3107
Current error: 0.00439796238879

Current iteration: 3108
Current error: 0.00417898821244

Current iteration: 3109
Current error: 0.00397626807131

Current iteration: 3110
Current error: 0.00378714054451

Current iteration: 3111
Current error: 0.00361352670623

Current iteration: 3112
Current error: 0.00344661059123

Current iteration: 3113
Current error: 0.00329265360401

Current iteration: 3114
Current error: 0.00315073866899

Current iteration: 3115
Current error: 0.00301369854307

Current iteration: 3116
Current error: 0.426746723994

Current iteration: 3117
Current error: 0.00478479865814

Current iteration: 3118
Current error: 0.00453762797579

Current iteration: 3119
Current error: 0.00430896743039

Current iteration: 3120
Current error: 0.00409737849163

Current iteration: 3121
Current error: 0.00390022882393

Current iteration: 3122
Current error: 0.00371734324178

Current iteration: 3123
Current error: 0.00354456373444

Current iteration: 3124
Current error: 0.00338866531829

Current iteration: 3125
Current error: 0.00323473427842

Current iteration: 3126
Current error: 0.00309446997191

Current iteration: 3127
Current error: 0.425775712606

Current iteration: 3128
Current error: 0.00490208975586

Current iteration: 3129
Current error: 0.00464690461677

Current iteration: 3130
Current error: 0.00441051151252

Current iteration: 3131
Current error: 0.00419088121782

Current iteration: 3132
Current error: 0.00398928527343

Current iteration: 3133
Current error: 0.00379799667236

Current iteration: 3134
Current error: 0.00362164251349

Current iteration: 3135
Current error: 0.00346081511479

Current iteration: 3136
Current error: 0.00330260382191

Current iteration: 3137
Current error: 0.00315672814637

Current iteration: 3138
Current error: 0.00302126228947

Current iteration: 3139
Current error: 0.00289408285209

Current iteration: 3140
Current error: 0.00277473305215

Current iteration: 3141
Current error: 0.00266265155938

Current iteration: 3142
Current error: 0.00255679467809

Current iteration: 3143
Current error: 0.432138374799

Current iteration: 3144
Current error: 0.00410191828898

Current iteration: 3145
Current error: 0.00390139277532

Current iteration: 3146
Current error: 0.00371889589583

Current iteration: 3147
Current error: 0.00354990957611

Current iteration: 3148
Current error: 0.00339166221428

Current iteration: 3149
Current error: 0.0032376216319

Current iteration: 3150
Current error: 0.00309534918003

Current iteration: 3151
Current error: 0.00296354007193

Current iteration: 3152
Current error: 0.00283991971092

Current iteration: 3153
Current error: 0.00272602445472

Current iteration: 3154
Current error: 0.00261467296822

Current iteration: 3155
Current error: 0.0025112810242

Current iteration: 3156
Current error: 0.00241387512668

Current iteration: 3157
Current error: 0.00232615681271

Current iteration: 3158
Current error: 0.00223576795307

Current iteration: 3159
Current error: 0.00215375089202

Current iteration: 3160
Current error: 0.00207566819421

Current iteration: 3161
Current error: 0.00200767798793

Current iteration: 3162
Current error: 0.00193187830265

Current iteration: 3163
Current error: 0.440633944849

Current iteration: 3164
Current error: 0.00314629387225

Current iteration: 3165
Current error: 0.00301344443649

Current iteration: 3166
Current error: 0.426792797851

Current iteration: 3167
Current error: 0.00478291280779

Current iteration: 3168
Current error: 0.00454147591462

Current iteration: 3169
Current error: 0.00430780541995

Current iteration: 3170
Current error: 0.00409604396464

Current iteration: 3171
Current error: 0.00389768472041

Current iteration: 3172
Current error: 0.00371777749938

Current iteration: 3173
Current error: 0.00354329049997

Current iteration: 3174
Current error: 0.00338352443063

Current iteration: 3175
Current error: 0.00323400830093

Current iteration: 3176
Current error: 0.00309352511918

Current iteration: 3177
Current error: 0.00296133670064

Current iteration: 3178
Current error: 0.00283901759227

Current iteration: 3179
Current error: 0.00272351327081

Current iteration: 3180
Current error: 0.0026128979489

Current iteration: 3181
Current error: 0.0025096270354

Current iteration: 3182
Current error: 0.432812424176

Current iteration: 3183
Current error: 0.00402945964205

Current iteration: 3184
Current error: 0.00383661241947

Current iteration: 3185
Current error: 0.00365717340729

Current iteration: 3186
Current error: 0.0034900207416

Current iteration: 3187
Current error: 0.00333523771163

Current iteration: 3188
Current error: 0.00318652792078

Current iteration: 3189
Current error: 0.0030499236007

Current iteration: 3190
Current error: 0.00292041242822

Current iteration: 3191
Current error: 0.00280175690816

Current iteration: 3192
Current error: 0.00268541887472

Current iteration: 3193
Current error: 0.00257858830244

Current iteration: 3194
Current error: 0.00247716877295

Current iteration: 3195
Current error: 0.00238414416702

Current iteration: 3196
Current error: 0.00229300189083

Current iteration: 3197
Current error: 0.00220808005284

Current iteration: 3198
Current error: 0.00212775181415

Current iteration: 3199
Current error: 0.00205015454298

Current iteration: 3200
Current error: 0.00197763951271

Current iteration: 3201
Current error: 0.00190904331935

Current iteration: 3202
Current error: 0.00184386041695

Current iteration: 3203
Current error: 0.441894438257

Current iteration: 3204
Current error: 0.00301238406349

Current iteration: 3205
Current error: 0.426682607935

Current iteration: 3206
Current error: 0.00477652599696

Current iteration: 3207
Current error: 0.00454562157805

Current iteration: 3208
Current error: 0.0043014337898

Current iteration: 3209
Current error: 0.00408946724165

Current iteration: 3210
Current error: 0.00389341675818

Current iteration: 3211
Current error: 0.00371033995339

Current iteration: 3212
Current error: 0.00353948920579

Current iteration: 3213
Current error: 0.00338015217304

Current iteration: 3214
Current error: 0.00322976995257

Current iteration: 3215
Current error: 0.00308984638631

Current iteration: 3216
Current error: 0.00295827609285

Current iteration: 3217
Current error: 0.00283798870751

Current iteration: 3218
Current error: 0.00271927734197

Current iteration: 3219
Current error: 0.00261044110912

Current iteration: 3220
Current error: 0.00250695378809

Current iteration: 3221
Current error: 0.0024098797551

Current iteration: 3222
Current error: 0.00232210840637

Current iteration: 3223
Current error: 0.00223330386475

Current iteration: 3224
Current error: 0.00215096604627

Current iteration: 3225
Current error: 0.0020739149809

Current iteration: 3226
Current error: 0.00199971915901

Current iteration: 3227
Current error: 0.00192934615818

Current iteration: 3228
Current error: 0.00186325134444

Current iteration: 3229
Current error: 0.00179999210326

Current iteration: 3230
Current error: 0.00174030924625

Current iteration: 3231
Current error: 0.00168340018013

Current iteration: 3232
Current error: 0.00162900592808

Current iteration: 3233
Current error: 0.00157721053017

Current iteration: 3234
Current error: 0.00152781240474

Current iteration: 3235
Current error: 0.00148083151415

Current iteration: 3236
Current error: 0.00143573636693

Current iteration: 3237
Current error: 0.00139350950308

Current iteration: 3238
Current error: 0.00135164975358

Current iteration: 3239
Current error: 0.00131203149388

Current iteration: 3240
Current error: 0.00127447514983

Current iteration: 3241
Current error: 0.0012384620508

Current iteration: 3242
Current error: 0.00120925830097

Current iteration: 3243
Current error: 0.00117165828867

Current iteration: 3244
Current error: 0.00113923366674

Current iteration: 3245
Current error: 0.00110970100491

Current iteration: 3246
Current error: 0.00107846443292

Current iteration: 3247
Current error: 0.00105039499793

Current iteration: 3248
Current error: 0.00102341080849

Current iteration: 3249
Current error: 0.000996851226538

Current iteration: 3250
Current error: 0.00097194827856

Current iteration: 3251
Current error: 0.000947562463886

Current iteration: 3252
Current error: 0.000924657100244

Current iteration: 3253
Current error: 0.000901543138079

Current iteration: 3254
Current error: 0.000879889190045

Current iteration: 3255
Current error: 0.000858858584301

Current iteration: 3256
Current error: 0.459776542323

Current iteration: 3257
Current error: 0.447431500342

Current iteration: 3258
Current error: 0.00246650327716

Current iteration: 3259
Current error: 0.0023719550339

Current iteration: 3260
Current error: 0.00228247179441

Current iteration: 3261
Current error: 0.00219766098674

Current iteration: 3262
Current error: 0.00211756038756

Current iteration: 3263
Current error: 0.00204238725975

Current iteration: 3264
Current error: 0.00196987847023

Current iteration: 3265
Current error: 0.440035456684

Current iteration: 3266
Current error: 0.00320596178476

Current iteration: 3267
Current error: 0.003066090867

Current iteration: 3268
Current error: 0.00293611678963

Current iteration: 3269
Current error: 0.00281412932933

Current iteration: 3270
Current error: 0.00270034216378

Current iteration: 3271
Current error: 0.00259145564944

Current iteration: 3272
Current error: 0.00248971140683

Current iteration: 3273
Current error: 0.00239509665514

Current iteration: 3274
Current error: 0.00230308828078

Current iteration: 3275
Current error: 0.00221725575561

Current iteration: 3276
Current error: 0.00213689075042

Current iteration: 3277
Current error: 0.00205936002996

Current iteration: 3278
Current error: 0.00198752634445

Current iteration: 3279
Current error: 0.00191740334408

Current iteration: 3280
Current error: 0.00185283516452

Current iteration: 3281
Current error: 0.00179440439624

Current iteration: 3282
Current error: 0.00173051292948

Current iteration: 3283
Current error: 0.00167382856988

Current iteration: 3284
Current error: 0.00162054966983

Current iteration: 3285
Current error: 0.00156924985228

Current iteration: 3286
Current error: 0.00151969058701

Current iteration: 3287
Current error: 0.00147499549154

Current iteration: 3288
Current error: 0.00142799340704

Current iteration: 3289
Current error: 0.00138530897637

Current iteration: 3290
Current error: 0.00134515077112

Current iteration: 3291
Current error: 0.00130556275518

Current iteration: 3292
Current error: 0.00127009800202

Current iteration: 3293
Current error: 0.00123258731443

Current iteration: 3294
Current error: 0.00119772718576

Current iteration: 3295
Current error: 0.001164710615

Current iteration: 3296
Current error: 0.00113331695991

Current iteration: 3297
Current error: 0.00110269874571

Current iteration: 3298
Current error: 0.00107363475556

Current iteration: 3299
Current error: 0.001045465455

Current iteration: 3300
Current error: 0.0010187598213

Current iteration: 3301
Current error: 0.000992309696841

Current iteration: 3302
Current error: 0.000967574971712

Current iteration: 3303
Current error: 0.000944555458138

Current iteration: 3304
Current error: 0.000919977323449

Current iteration: 3305
Current error: 0.000901085039311

Current iteration: 3306
Current error: 0.458901840272

Current iteration: 3307
Current error: 0.446312647462

Current iteration: 3308
Current error: 0.430875108722

Current iteration: 3309
Current error: 0.411474850718

Current iteration: 3310
Current error: 0.00696025537783

Current iteration: 3311
Current error: 0.00653891193904

Current iteration: 3312
Current error: 0.0061537234387

Current iteration: 3313
Current error: 0.00580097912688

Current iteration: 3314
Current error: 0.00547645755265

Current iteration: 3315
Current error: 0.0051766826956

Current iteration: 3316
Current error: 0.00490146538028

Current iteration: 3317
Current error: 0.00464574385732

Current iteration: 3318
Current error: 0.00440917578483

Current iteration: 3319
Current error: 0.00418983991516

Current iteration: 3320
Current error: 0.00398821098143

Current iteration: 3321
Current error: 0.00379678750795

Current iteration: 3322
Current error: 0.00361994946128

Current iteration: 3323
Current error: 0.00345660066895

Current iteration: 3324
Current error: 0.00330120477531

Current iteration: 3325
Current error: 0.00315683269225

Current iteration: 3326
Current error: 0.00302626567362

Current iteration: 3327
Current error: 0.00289332218232

Current iteration: 3328
Current error: 0.00277395905605

Current iteration: 3329
Current error: 0.00266171321589

Current iteration: 3330
Current error: 0.00255593385252

Current iteration: 3331
Current error: 0.00245721161403

Current iteration: 3332
Current error: 0.00236475128042

Current iteration: 3333
Current error: 0.00227536199327

Current iteration: 3334
Current error: 0.002196941707

Current iteration: 3335
Current error: 0.00210918518591

Current iteration: 3336
Current error: 0.00203414937272

Current iteration: 3337
Current error: 0.00196257372362

Current iteration: 3338
Current error: 0.00189441203807

Current iteration: 3339
Current error: 0.00183009564369

Current iteration: 3340
Current error: 0.00176887638303

Current iteration: 3341
Current error: 0.00171052689429

Current iteration: 3342
Current error: 0.00165484005816

Current iteration: 3343
Current error: 0.00160168796757

Current iteration: 3344
Current error: 0.00155128256861

Current iteration: 3345
Current error: 0.00150307730094

Current iteration: 3346
Current error: 0.00145803663025

Current iteration: 3347
Current error: 0.00141352156846

Current iteration: 3348
Current error: 0.00137312551354

Current iteration: 3349
Current error: 0.0013332043636

Current iteration: 3350
Current error: 0.00129237824858

Current iteration: 3351
Current error: 0.00125542936411

Current iteration: 3352
Current error: 0.00122003248411

Current iteration: 3353
Current error: 0.00118684342687

Current iteration: 3354
Current error: 0.00115376949229

Current iteration: 3355
Current error: 0.00112674644114

Current iteration: 3356
Current error: 0.0010927595181

Current iteration: 3357
Current error: 0.00106379397642

Current iteration: 3358
Current error: 0.0010364766086

Current iteration: 3359
Current error: 0.00100993932613

Current iteration: 3360
Current error: 0.456488353612

Current iteration: 3361
Current error: 0.00169305377413

Current iteration: 3362
Current error: 0.00163928962731

Current iteration: 3363
Current error: 0.0015861367782

Current iteration: 3364
Current error: 0.446002005648

Current iteration: 3365
Current error: 0.00261150292566

Current iteration: 3366
Current error: 0.431459264096

Current iteration: 3367
Current error: 0.00417832724151

Current iteration: 3368
Current error: 0.00397531008649

Current iteration: 3369
Current error: 0.416526872977

Current iteration: 3370
Current error: 0.00619189280254

Current iteration: 3371
Current error: 0.00583727428921

Current iteration: 3372
Current error: 0.00550851260704

Current iteration: 3373
Current error: 0.00520687109443

Current iteration: 3374
Current error: 0.00493867282588

Current iteration: 3375
Current error: 0.00467716752693

Current iteration: 3376
Current error: 0.00443280822151

Current iteration: 3377
Current error: 0.00421390975464

Current iteration: 3378
Current error: 0.00400679294925

Current iteration: 3379
Current error: 0.00381593346592

Current iteration: 3380
Current error: 0.00363771380483

Current iteration: 3381
Current error: 0.0034719009711

Current iteration: 3382
Current error: 0.00331904011964

Current iteration: 3383
Current error: 0.00317155417448

Current iteration: 3384
Current error: 0.00303425173005

Current iteration: 3385
Current error: 0.00290687113417

Current iteration: 3386
Current error: 0.00278636185841

Current iteration: 3387
Current error: 0.00267332675857

Current iteration: 3388
Current error: 0.00256701106919

Current iteration: 3389
Current error: 0.00247469045608

Current iteration: 3390
Current error: 0.00237152064106

Current iteration: 3391
Current error: 0.00228219903594

Current iteration: 3392
Current error: 0.00219767986112

Current iteration: 3393
Current error: 0.00211746025382

Current iteration: 3394
Current error: 0.0020419487788

Current iteration: 3395
Current error: 0.00197093344098

Current iteration: 3396
Current error: 0.0019013426823

Current iteration: 3397
Current error: 0.00183640351886

Current iteration: 3398
Current error: 0.00177581526446

Current iteration: 3399
Current error: 0.00171655018415

Current iteration: 3400
Current error: 0.00166039201804

Current iteration: 3401
Current error: 0.00160709928108

Current iteration: 3402
Current error: 0.00155633490927

Current iteration: 3403
Current error: 0.00151595350444

Current iteration: 3404
Current error: 0.00146193390332

Current iteration: 3405
Current error: 0.00141769124437

Current iteration: 3406
Current error: 0.00137581064052

Current iteration: 3407
Current error: 0.00133493334902

Current iteration: 3408
Current error: 0.00129791468803

Current iteration: 3409
Current error: 0.00125946122329

Current iteration: 3410
Current error: 0.00122381477324

Current iteration: 3411
Current error: 0.00119002400069

Current iteration: 3412
Current error: 0.00115708890724

Current iteration: 3413
Current error: 0.00112580039367

Current iteration: 3414
Current error: 0.00109552492671

Current iteration: 3415
Current error: 0.00106757910998

Current iteration: 3416
Current error: 0.00103886277703

Current iteration: 3417
Current error: 0.00101222548384

Current iteration: 3418
Current error: 0.000988695878453

Current iteration: 3419
Current error: 0.00096177999106

Current iteration: 3420
Current error: 0.000938172591291

Current iteration: 3421
Current error: 0.000914633153582

Current iteration: 3422
Current error: 0.000892759229879

Current iteration: 3423
Current error: 0.000871081084552

Current iteration: 3424
Current error: 0.000850725669279

Current iteration: 3425
Current error: 0.000830535079479

Current iteration: 3426
Current error: 0.000811149412095

Current iteration: 3427
Current error: 0.000792522771453

Current iteration: 3428
Current error: 0.000775051405371

Current iteration: 3429
Current error: 0.00075760228869

Current iteration: 3430
Current error: 0.000740634265718

Current iteration: 3431
Current error: 0.000724259503658

Current iteration: 3432
Current error: 0.00070893060948

Current iteration: 3433
Current error: 0.000693330645374

Current iteration: 3434
Current error: 0.000678995023538

Current iteration: 3435
Current error: 0.000664296581233

Current iteration: 3436
Current error: 0.000650330525973

Current iteration: 3437
Current error: 0.000637009311233

Current iteration: 3438
Current error: 0.000623937607854

Current iteration: 3439
Current error: 0.000611310552256

Current iteration: 3440
Current error: 0.000599070045788

Current iteration: 3441
Current error: 0.000587277759393

Current iteration: 3442
Current error: 0.000575694631949

Current iteration: 3443
Current error: 0.000565354289211

Current iteration: 3444
Current error: 0.000553689399332

Current iteration: 3445
Current error: 0.46748722361

Current iteration: 3446
Current error: 0.000948472431818

Current iteration: 3447
Current error: 0.000924940934661

Current iteration: 3448
Current error: 0.000902561946686

Current iteration: 3449
Current error: 0.000880265054918

Current iteration: 3450
Current error: 0.000863800149538

Current iteration: 3451
Current error: 0.000839093997799

Current iteration: 3452
Current error: 0.000819674311795

Current iteration: 3453
Current error: 0.0008020762227

Current iteration: 3454
Current error: 0.000782489781387

Current iteration: 3455
Current error: 0.000764749679712

Current iteration: 3456
Current error: 0.000747779652617

Current iteration: 3457
Current error: 0.000731188829086

Current iteration: 3458
Current error: 0.000715343371429

Current iteration: 3459
Current error: 0.000700630049814

Current iteration: 3460
Current error: 0.000684942631145

Current iteration: 3461
Current error: 0.000670432521005

Current iteration: 3462
Current error: 0.000656478404215

Current iteration: 3463
Current error: 0.00064312510206

Current iteration: 3464
Current error: 0.000629551189168

Current iteration: 3465
Current error: 0.000617111298726

Current iteration: 3466
Current error: 0.000604339038921

Current iteration: 3467
Current error: 0.00059233884774

Current iteration: 3468
Current error: 0.000580613477264

Current iteration: 3469
Current error: 0.000569236544516

Current iteration: 3470
Current error: 0.000558340726049

Current iteration: 3471
Current error: 0.000547541327458

Current iteration: 3472
Current error: 0.000537105867573

Current iteration: 3473
Current error: 0.000526927599412

Current iteration: 3474
Current error: 0.00051719335557

Current iteration: 3475
Current error: 0.468556006159

Current iteration: 3476
Current error: 0.000887581863221

Current iteration: 3477
Current error: 0.00086623217883

Current iteration: 3478
Current error: 0.000846475515262

Current iteration: 3479
Current error: 0.000825873089822

Current iteration: 3480
Current error: 0.000807023279553

Current iteration: 3481
Current error: 0.00079126781987

Current iteration: 3482
Current error: 0.461389419176

Current iteration: 3483
Current error: 0.00133496991198

Current iteration: 3484
Current error: 0.00129627539666

Current iteration: 3485
Current error: 0.00125911129042

Current iteration: 3486
Current error: 0.00122390531925

Current iteration: 3487
Current error: 0.00118952379844

Current iteration: 3488
Current error: 0.00115697919427

Current iteration: 3489
Current error: 0.00112570625562

Current iteration: 3490
Current error: 0.00109558034124

Current iteration: 3491
Current error: 0.00106685013699

Current iteration: 3492
Current error: 0.00103869885525

Current iteration: 3493
Current error: 0.00101220767813

Current iteration: 3494
Current error: 0.000986477664248

Current iteration: 3495
Current error: 0.000962284013762

Current iteration: 3496
Current error: 0.000937739618727

Current iteration: 3497
Current error: 0.000914646923652

Current iteration: 3498
Current error: 0.000892480853464

Current iteration: 3499
Current error: 0.000871090881758

Current iteration: 3500
Current error: 0.000850357231254

Current iteration: 3501
Current error: 0.000830583795741

Current iteration: 3502
Current error: 0.000811112058379

Current iteration: 3503
Current error: 0.460761941266

Current iteration: 3504
Current error: 0.00137149475036

Current iteration: 3505
Current error: 0.00133132648521

Current iteration: 3506
Current error: 0.00129265317529

Current iteration: 3507
Current error: 0.00125578145715

Current iteration: 3508
Current error: 0.00122070704003

Current iteration: 3509
Current error: 0.00118696281995

Current iteration: 3510
Current error: 0.001154577673

Current iteration: 3511
Current error: 0.00112354251636

Current iteration: 3512
Current error: 0.00109295900221

Current iteration: 3513
Current error: 0.00106417663464

Current iteration: 3514
Current error: 0.0010362695751

Current iteration: 3515
Current error: 0.00101062385421

Current iteration: 3516
Current error: 0.000984142213279

Current iteration: 3517
Current error: 0.000959583138351

Current iteration: 3518
Current error: 0.000935500948522

Current iteration: 3519
Current error: 0.457965737554

Current iteration: 3520
Current error: 0.00157516656709

Current iteration: 3521
Current error: 0.00152388751062

Current iteration: 3522
Current error: 0.00147702661604

Current iteration: 3523
Current error: 0.00143552256912

Current iteration: 3524
Current error: 0.00138933842612

Current iteration: 3525
Current error: 0.00134839570924

Current iteration: 3526
Current error: 0.00130911015311

Current iteration: 3527
Current error: 0.00127151665623

Current iteration: 3528
Current error: 0.451390974205

Current iteration: 3529
Current error: 0.436898495406

Current iteration: 3530
Current error: 0.419062357908

Current iteration: 3531
Current error: 0.00581772439862

Current iteration: 3532
Current error: 0.00549106227995

Current iteration: 3533
Current error: 0.00519131745769

Current iteration: 3534
Current error: 0.00491474549216

Current iteration: 3535
Current error: 0.00465772118862

Current iteration: 3536
Current error: 0.00442099975707

Current iteration: 3537
Current error: 0.00420039743634

Current iteration: 3538
Current error: 0.0039965126647

Current iteration: 3539
Current error: 0.00380575674634

Current iteration: 3540
Current error: 0.00362892601402

Current iteration: 3541
Current error: 0.00346264300037

Current iteration: 3542
Current error: 0.421659991869

Current iteration: 3543
Current error: 0.00544398887363

Current iteration: 3544
Current error: 0.00515111250729

Current iteration: 3545
Current error: 0.00487497626705

Current iteration: 3546
Current error: 0.00462170938075

Current iteration: 3547
Current error: 0.00439016470991

Current iteration: 3548
Current error: 0.412719403439

Current iteration: 3549
Current error: 0.00678569680174

Current iteration: 3550
Current error: 0.00638117533941

Current iteration: 3551
Current error: 0.00600954206579

Current iteration: 3552
Current error: 0.0056670108075

Current iteration: 3553
Current error: 0.401675216023

Current iteration: 3554
Current error: 0.00859215618555

Current iteration: 3555
Current error: 0.00802513529113

Current iteration: 3556
Current error: 0.007512389609

Current iteration: 3557
Current error: 0.00704216248207

Current iteration: 3558
Current error: 0.00661486563166

Current iteration: 3559
Current error: 0.00622323926554

Current iteration: 3560
Current error: 0.00586433252196

Current iteration: 3561
Current error: 0.00553450245229

Current iteration: 3562
Current error: 0.00523160721114

Current iteration: 3563
Current error: 0.00495861232879

Current iteration: 3564
Current error: 0.00469268253722

Current iteration: 3565
Current error: 0.00445210363132

Current iteration: 3566
Current error: 0.0042349042396

Current iteration: 3567
Current error: 0.00402390654704

Current iteration: 3568
Current error: 0.00383081795773

Current iteration: 3569
Current error: 0.00365356812517

Current iteration: 3570
Current error: 0.00348828307147

Current iteration: 3571
Current error: 0.0033298002792

Current iteration: 3572
Current error: 0.42340049798

Current iteration: 3573
Current error: 0.00525246952

Current iteration: 3574
Current error: 0.0049728663117

Current iteration: 3575
Current error: 0.00471136103554

Current iteration: 3576
Current error: 0.00448155042017

Current iteration: 3577
Current error: 0.00424611219301

Current iteration: 3578
Current error: 0.00403829235018

Current iteration: 3579
Current error: 0.00385513006995

Current iteration: 3580
Current error: 0.00366475067157

Current iteration: 3581
Current error: 0.419665909338

Current iteration: 3582
Current error: 0.00574232758728

Current iteration: 3583
Current error: 0.00542194723544

Current iteration: 3584
Current error: 0.00513046268995

Current iteration: 3585
Current error: 0.00485534730238

Current iteration: 3586
Current error: 0.00460347817842

Current iteration: 3587
Current error: 0.0043697190147

Current iteration: 3588
Current error: 0.00415347650708

Current iteration: 3589
Current error: 0.00395212587806

Current iteration: 3590
Current error: 0.00377067102212

Current iteration: 3591
Current error: 0.00359058627939

Current iteration: 3592
Current error: 0.003426958844

Current iteration: 3593
Current error: 0.00327466636241

Current iteration: 3594
Current error: 0.00313165071742

Current iteration: 3595
Current error: 0.00299830515612

Current iteration: 3596
Current error: 0.00287208125398

Current iteration: 3597
Current error: 0.00275413024138

Current iteration: 3598
Current error: 0.00264334630454

Current iteration: 3599
Current error: 0.431015551161

Current iteration: 3600
Current error: 0.00423406290261

Current iteration: 3601
Current error: 0.00402359261115

Current iteration: 3602
Current error: 0.00382875453481

Current iteration: 3603
Current error: 0.00364987935961

Current iteration: 3604
Current error: 0.00348307965996

Current iteration: 3605
Current error: 0.421571930518

Current iteration: 3606
Current error: 0.00547611950396

Current iteration: 3607
Current error: 0.00517775764545

Current iteration: 3608
Current error: 0.0049049472728

Current iteration: 3609
Current error: 0.00464681575039

Current iteration: 3610
Current error: 0.00440967009415

Current iteration: 3611
Current error: 0.00419049932692

Current iteration: 3612
Current error: 0.0039864301741

Current iteration: 3613
Current error: 0.0037979029336

Current iteration: 3614
Current error: 0.00362038067216

Current iteration: 3615
Current error: 0.420034787028

Current iteration: 3616
Current error: 0.00567519337119

Current iteration: 3617
Current error: 0.0053603702054

Current iteration: 3618
Current error: 0.00507006886612

Current iteration: 3619
Current error: 0.00480197878257

Current iteration: 3620
Current error: 0.408832934917

Current iteration: 3621
Current error: 0.00737417267839

Current iteration: 3622
Current error: 0.00691821897826

Current iteration: 3623
Current error: 0.0065009637596

Current iteration: 3624
Current error: 0.00612095573203

Current iteration: 3625
Current error: 0.00576863621783

Current iteration: 3626
Current error: 0.00544673131292

Current iteration: 3627
Current error: 0.005149986146

Current iteration: 3628
Current error: 0.00487622834638

Current iteration: 3629
Current error: 0.00462275797312

Current iteration: 3630
Current error: 0.00438838047091

Current iteration: 3631
Current error: 0.00417075367511

Current iteration: 3632
Current error: 0.00396813463507

Current iteration: 3633
Current error: 0.00377938534248

Current iteration: 3634
Current error: 0.00360399495044

Current iteration: 3635
Current error: 0.00344013982228

Current iteration: 3636
Current error: 0.00328686167484

Current iteration: 3637
Current error: 0.00314304353623

Current iteration: 3638
Current error: 0.00300833298911

Current iteration: 3639
Current error: 0.00288728525831

Current iteration: 3640
Current error: 0.00276360485433

Current iteration: 3641
Current error: 0.00265150395774

Current iteration: 3642
Current error: 0.430803406182

Current iteration: 3643
Current error: 0.00424084013707

Current iteration: 3644
Current error: 0.00403211559022

Current iteration: 3645
Current error: 0.00383987624114

Current iteration: 3646
Current error: 0.00365920350347

Current iteration: 3647
Current error: 0.00349180605673

Current iteration: 3648
Current error: 0.00333485567762

Current iteration: 3649
Current error: 0.00318935452574

Current iteration: 3650
Current error: 0.00306249284165

Current iteration: 3651
Current error: 0.00292191851399

Current iteration: 3652
Current error: 0.00280127144661

Current iteration: 3653
Current error: 0.0026875723072

Current iteration: 3654
Current error: 0.00257979476744

Current iteration: 3655
Current error: 0.00247945644805

Current iteration: 3656
Current error: 0.00238333417993

Current iteration: 3657
Current error: 0.00229297350407

Current iteration: 3658
Current error: 0.00220875048732

Current iteration: 3659
Current error: 0.00212768619129

Current iteration: 3660
Current error: 0.00205115912032

Current iteration: 3661
Current error: 0.00198069823377

Current iteration: 3662
Current error: 0.00190992840809

Current iteration: 3663
Current error: 0.00184476456852

Current iteration: 3664
Current error: 0.00178312224403

Current iteration: 3665
Current error: 0.00172341068056

Current iteration: 3666
Current error: 0.00166728248547

Current iteration: 3667
Current error: 0.0016136326483

Current iteration: 3668
Current error: 0.0015661797727

Current iteration: 3669
Current error: 0.00151421038523

Current iteration: 3670
Current error: 0.00146749927986

Current iteration: 3671
Current error: 0.00142639679201

Current iteration: 3672
Current error: 0.00138096459802

Current iteration: 3673
Current error: 0.0013399586122

Current iteration: 3674
Current error: 0.00130251570348

Current iteration: 3675
Current error: 0.00126387310437

Current iteration: 3676
Current error: 0.00122823722481

Current iteration: 3677
Current error: 0.00119399351048

Current iteration: 3678
Current error: 0.00116127814879

Current iteration: 3679
Current error: 0.00113076594366

Current iteration: 3680
Current error: 0.00109995244177

Current iteration: 3681
Current error: 0.00107036113997

Current iteration: 3682
Current error: 0.00104227768157

Current iteration: 3683
Current error: 0.00101595058656

Current iteration: 3684
Current error: 0.000989541766277

Current iteration: 3685
Current error: 0.000964614378503

Current iteration: 3686
Current error: 0.457361911889

Current iteration: 3687
Current error: 0.00162080320726

Current iteration: 3688
Current error: 0.00157076813242

Current iteration: 3689
Current error: 0.00152014162233

Current iteration: 3690
Current error: 0.00147346160142

Current iteration: 3691
Current error: 0.00142887742345

Current iteration: 3692
Current error: 0.00138595886978

Current iteration: 3693
Current error: 0.00134603290944

Current iteration: 3694
Current error: 0.00130604626617

Current iteration: 3695
Current error: 0.00126850313288

Current iteration: 3696
Current error: 0.00123308010083

Current iteration: 3697
Current error: 0.00119838115676

Current iteration: 3698
Current error: 0.0011652790797

Current iteration: 3699
Current error: 0.00113364666898

Current iteration: 3700
Current error: 0.00110318990097

Current iteration: 3701
Current error: 0.454595705487

Current iteration: 3702
Current error: 0.00184482397002

Current iteration: 3703
Current error: 0.00178207897128

Current iteration: 3704
Current error: 0.0017232294268

Current iteration: 3705
Current error: 0.00166716558316

Current iteration: 3706
Current error: 0.00161350324727

Current iteration: 3707
Current error: 0.00156241036068

Current iteration: 3708
Current error: 0.00151379869049

Current iteration: 3709
Current error: 0.00146738390879

Current iteration: 3710
Current error: 0.00142333660143

Current iteration: 3711
Current error: 0.00138042001837

Current iteration: 3712
Current error: 0.00133980604751

Current iteration: 3713
Current error: 0.00130089938023

Current iteration: 3714
Current error: 0.00126393018574

Current iteration: 3715
Current error: 0.00122800220796

Current iteration: 3716
Current error: 0.00119390799454

Current iteration: 3717
Current error: 0.00116122418131

Current iteration: 3718
Current error: 0.453452176177

Current iteration: 3719
Current error: 0.43947046057

Current iteration: 3720
Current error: 0.00326277313201

Current iteration: 3721
Current error: 0.00311892854717

Current iteration: 3722
Current error: 0.00298584255465

Current iteration: 3723
Current error: 0.00286405186592

Current iteration: 3724
Current error: 0.00274521292755

Current iteration: 3725
Current error: 0.00263322716983

Current iteration: 3726
Current error: 0.00252878676776

Current iteration: 3727
Current error: 0.00243605395536

Current iteration: 3728
Current error: 0.00233798193269

Current iteration: 3729
Current error: 0.00225053341014

Current iteration: 3730
Current error: 0.0021683570119

Current iteration: 3731
Current error: 0.4370724388

Current iteration: 3732
Current error: 0.00350532569909

Current iteration: 3733
Current error: 0.00334719115349

Current iteration: 3734
Current error: 0.00319985175971

Current iteration: 3735
Current error: 0.00306174978246

Current iteration: 3736
Current error: 0.00293202045592

Current iteration: 3737
Current error: 0.00281123192332

Current iteration: 3738
Current error: 0.00269629643054

Current iteration: 3739
Current error: 0.00258813627673

Current iteration: 3740
Current error: 0.00248692259475

Current iteration: 3741
Current error: 0.00239160301825

Current iteration: 3742
Current error: 0.00230032276273

Current iteration: 3743
Current error: 0.00221450031709

Current iteration: 3744
Current error: 0.00213348631351

Current iteration: 3745
Current error: 0.00205817147742

Current iteration: 3746
Current error: 0.00198438916618

Current iteration: 3747
Current error: 0.00191509593482

Current iteration: 3748
Current error: 0.00184978364788

Current iteration: 3749
Current error: 0.00179714080312

Current iteration: 3750
Current error: 0.00172793694693

Current iteration: 3751
Current error: 0.00167188749299

Current iteration: 3752
Current error: 0.00161852216254

Current iteration: 3753
Current error: 0.00156666751908

Current iteration: 3754
Current error: 0.00151776838538

Current iteration: 3755
Current error: 0.00147126917823

Current iteration: 3756
Current error: 0.00142650005193

Current iteration: 3757
Current error: 0.00138538965986

Current iteration: 3758
Current error: 0.00134320931114

Current iteration: 3759
Current error: 0.00131069292818

Current iteration: 3760
Current error: 0.0012668232291

Current iteration: 3761
Current error: 0.0012310104355

Current iteration: 3762
Current error: 0.00119654816865

Current iteration: 3763
Current error: 0.001165941431

Current iteration: 3764
Current error: 0.00113303302076

Current iteration: 3765
Current error: 0.00110161857932

Current iteration: 3766
Current error: 0.0010730462502

Current iteration: 3767
Current error: 0.00104433446988

Current iteration: 3768
Current error: 0.00101747354023

Current iteration: 3769
Current error: 0.000991491870346

Current iteration: 3770
Current error: 0.456766089157

Current iteration: 3771
Current error: 0.00166398861694

Current iteration: 3772
Current error: 0.0016105109185

Current iteration: 3773
Current error: 0.00156015288779

Current iteration: 3774
Current error: 0.00151110799532

Current iteration: 3775
Current error: 0.00146471855228

Current iteration: 3776
Current error: 0.00142088148477

Current iteration: 3777
Current error: 0.00137831904591

Current iteration: 3778
Current error: 0.00133763335583

Current iteration: 3779
Current error: 0.00129874317278

Current iteration: 3780
Current error: 0.00126199615697

Current iteration: 3781
Current error: 0.00122591128196

Current iteration: 3782
Current error: 0.00119264502191

Current iteration: 3783
Current error: 0.00115916296914

Current iteration: 3784
Current error: 0.00112765664033

Current iteration: 3785
Current error: 0.00109752143035

Current iteration: 3786
Current error: 0.00107163704102

Current iteration: 3787
Current error: 0.00104066358745

Current iteration: 3788
Current error: 0.0010137716177

Current iteration: 3789
Current error: 0.000988713971421

Current iteration: 3790
Current error: 0.000963906416863

Current iteration: 3791
Current error: 0.000939086431608

Current iteration: 3792
Current error: 0.000916228716106

Current iteration: 3793
Current error: 0.000893940796914

Current iteration: 3794
Current error: 0.000872415180038

Current iteration: 3795
Current error: 0.000851678000269

Current iteration: 3796
Current error: 0.00083369008931

Current iteration: 3797
Current error: 0.000812445289738

Current iteration: 3798
Current error: 0.000794011413746

Current iteration: 3799
Current error: 0.000776409358953

Current iteration: 3800
Current error: 0.000758418218439

Current iteration: 3801
Current error: 0.000741617726822

Current iteration: 3802
Current error: 0.000725611162508

Current iteration: 3803
Current error: 0.000709683218426

Current iteration: 3804
Current error: 0.000694407707546

Current iteration: 3805
Current error: 0.000682507373924

Current iteration: 3806
Current error: 0.000665165502467

Current iteration: 3807
Current error: 0.000651166498563

Current iteration: 3808
Current error: 0.000639482429061

Current iteration: 3809
Current error: 0.000624741404051

Current iteration: 3810
Current error: 0.000612169566258

Current iteration: 3811
Current error: 0.000599990958708

Current iteration: 3812
Current error: 0.000587941066746

Current iteration: 3813
Current error: 0.000576396229257

Current iteration: 3814
Current error: 0.000565509658218

Current iteration: 3815
Current error: 0.467116593588

Current iteration: 3816
Current error: 0.000970081408469

Current iteration: 3817
Current error: 0.000942818574689

Current iteration: 3818
Current error: 0.000919680236463

Current iteration: 3819
Current error: 0.000897249925667

Current iteration: 3820
Current error: 0.458831934943

Current iteration: 3821
Current error: 0.00151172297364

Current iteration: 3822
Current error: 0.00146581249078

Current iteration: 3823
Current error: 0.00142106214453

Current iteration: 3824
Current error: 0.44866139543

Current iteration: 3825
Current error: 0.00234904831581

Current iteration: 3826
Current error: 0.00226088435517

Current iteration: 3827
Current error: 0.0021772613707

Current iteration: 3828
Current error: 0.00209821117987

Current iteration: 3829
Current error: 0.00202320086841

Current iteration: 3830
Current error: 0.00195251386077

Current iteration: 3831
Current error: 0.00188501180466

Current iteration: 3832
Current error: 0.00182078364472

Current iteration: 3833
Current error: 0.00175990679568

Current iteration: 3834
Current error: 0.00170217070589

Current iteration: 3835
Current error: 0.00164688155376

Current iteration: 3836
Current error: 0.00159438279298

Current iteration: 3837
Current error: 0.00154437022502

Current iteration: 3838
Current error: 0.00149844629849

Current iteration: 3839
Current error: 0.0014551037435

Current iteration: 3840
Current error: 0.00140694315144

Current iteration: 3841
Current error: 0.00136877297327

Current iteration: 3842
Current error: 0.0013251976156

Current iteration: 3843
Current error: 0.00128694249923

Current iteration: 3844
Current error: 0.451065960848

Current iteration: 3845
Current error: 0.00213683208038

Current iteration: 3846
Current error: 0.00206062940253

Current iteration: 3847
Current error: 0.00198713082394

Current iteration: 3848
Current error: 0.00191930275975

Current iteration: 3849
Current error: 0.00185221623479

Current iteration: 3850
Current error: 0.00178989614224

Current iteration: 3851
Current error: 0.442528084544

Current iteration: 3852
Current error: 0.00292452281751

Current iteration: 3853
Current error: 0.00280308317702

Current iteration: 3854
Current error: 0.00269019700914

Current iteration: 3855
Current error: 0.00258168612764

Current iteration: 3856
Current error: 0.00248046836221

Current iteration: 3857
Current error: 0.00238540161574

Current iteration: 3858
Current error: 0.00229489997437

Current iteration: 3859
Current error: 0.00221227714555

Current iteration: 3860
Current error: 0.436621104109

Current iteration: 3861
Current error: 0.00357077747288

Current iteration: 3862
Current error: 0.00340915209926

Current iteration: 3863
Current error: 0.00325804734089

Current iteration: 3864
Current error: 0.00311602232009

Current iteration: 3865
Current error: 0.00298323355022

Current iteration: 3866
Current error: 0.00285823079032

Current iteration: 3867
Current error: 0.00274088930469

Current iteration: 3868
Current error: 0.00263658506496

Current iteration: 3869
Current error: 0.00252697348161

Current iteration: 3870
Current error: 0.00242846117675

Current iteration: 3871
Current error: 0.00233850747266

Current iteration: 3872
Current error: 0.00224842975932

Current iteration: 3873
Current error: 0.00216597871692

Current iteration: 3874
Current error: 0.00208701712308

Current iteration: 3875
Current error: 0.00201287885892

Current iteration: 3876
Current error: 0.00194402464791

Current iteration: 3877
Current error: 0.00187546868185

Current iteration: 3878
Current error: 0.00181181186698

Current iteration: 3879
Current error: 0.00175267403788

Current iteration: 3880
Current error: 0.443197278801

Current iteration: 3881
Current error: 0.00286536978223

Current iteration: 3882
Current error: 0.00275019468485

Current iteration: 3883
Current error: 0.00263661184824

Current iteration: 3884
Current error: 0.00253229328342

Current iteration: 3885
Current error: 0.00243376973569

Current iteration: 3886
Current error: 0.433654189977

Current iteration: 3887
Current error: 0.00391252770542

Current iteration: 3888
Current error: 0.00374110013652

Current iteration: 3889
Current error: 0.0035586695188

Current iteration: 3890
Current error: 0.00339466745512

Current iteration: 3891
Current error: 0.00324419014024

Current iteration: 3892
Current error: 0.00310344400259

Current iteration: 3893
Current error: 0.00297100498115

Current iteration: 3894
Current error: 0.00285326535239

Current iteration: 3895
Current error: 0.0027308287811

Current iteration: 3896
Current error: 0.00262032579715

Current iteration: 3897
Current error: 0.00251903893746

Current iteration: 3898
Current error: 0.00241966359586

Current iteration: 3899
Current error: 0.00232748778846

Current iteration: 3900
Current error: 0.00224038340806

Current iteration: 3901
Current error: 0.00216010757203

Current iteration: 3902
Current error: 0.00208045528286

Current iteration: 3903
Current error: 0.00200593162505

Current iteration: 3904
Current error: 0.00193618815848

Current iteration: 3905
Current error: 0.00186930428968

Current iteration: 3906
Current error: 0.0018063025813

Current iteration: 3907
Current error: 0.00174594949939

Current iteration: 3908
Current error: 0.00168886266756

Current iteration: 3909
Current error: 0.00163445238493

Current iteration: 3910
Current error: 0.00158217439315

Current iteration: 3911
Current error: 0.00153267722258

Current iteration: 3912
Current error: 0.00148545460788

Current iteration: 3913
Current error: 0.00144056436303

Current iteration: 3914
Current error: 0.00139686018098

Current iteration: 3915
Current error: 0.00135558791031

Current iteration: 3916
Current error: 0.00131601491938

Current iteration: 3917
Current error: 0.00127814517171

Current iteration: 3918
Current error: 0.00124183645229

Current iteration: 3919
Current error: 0.00120710683822

Current iteration: 3920
Current error: 0.00117361321497

Current iteration: 3921
Current error: 0.00114186095179

Current iteration: 3922
Current error: 0.001111390397

Current iteration: 3923
Current error: 0.0010815105029

Current iteration: 3924
Current error: 0.00105302479978

Current iteration: 3925
Current error: 0.00102611672144

Current iteration: 3926
Current error: 0.000999411192619

Current iteration: 3927
Current error: 0.000974209494668

Current iteration: 3928
Current error: 0.000949852127148

Current iteration: 3929
Current error: 0.000926315377477

Current iteration: 3930
Current error: 0.000903803643638

Current iteration: 3931
Current error: 0.000882597183942

Current iteration: 3932
Current error: 0.000860966825849

Current iteration: 3933
Current error: 0.000840639341643

Current iteration: 3934
Current error: 0.000821154284575

Current iteration: 3935
Current error: 0.000802367928746

Current iteration: 3936
Current error: 0.000784211099327

Current iteration: 3937
Current error: 0.000766175864383

Current iteration: 3938
Current error: 0.000749059864381

Current iteration: 3939
Current error: 0.000732694948724

Current iteration: 3940
Current error: 0.000716704614175

Current iteration: 3941
Current error: 0.000701041099822

Current iteration: 3942
Current error: 0.000687164539209

Current iteration: 3943
Current error: 0.000671565483936

Current iteration: 3944
Current error: 0.000657425349161

Current iteration: 3945
Current error: 0.464576150796

Current iteration: 3946
Current error: 0.00111945823826

Current iteration: 3947
Current error: 0.00108961751256

Current iteration: 3948
Current error: 0.00106089905124

Current iteration: 3949
Current error: 0.00103339589636

Current iteration: 3950
Current error: 0.00100718290356

Current iteration: 3951
Current error: 0.000981229860651

Current iteration: 3952
Current error: 0.000957062236062

Current iteration: 3953
Current error: 0.000932987209233

Current iteration: 3954
Current error: 0.000910007012651

Current iteration: 3955
Current error: 0.458467104778

Current iteration: 3956
Current error: 0.00153226673663

Current iteration: 3957
Current error: 0.00148482015165

Current iteration: 3958
Current error: 0.00143929648156

Current iteration: 3959
Current error: 0.00139730277774

Current iteration: 3960
Current error: 0.00135540295268

Current iteration: 3961
Current error: 0.00131522263463

Current iteration: 3962
Current error: 0.00127740137171

Current iteration: 3963
Current error: 0.00124428718067

Current iteration: 3964
Current error: 0.00120644799027

Current iteration: 3965
Current error: 0.00117316526148

Current iteration: 3966
Current error: 0.453338437519

Current iteration: 3967
Current error: 0.0019579642347

Current iteration: 3968
Current error: 0.00188956213453

Current iteration: 3969
Current error: 0.00182539278626

Current iteration: 3970
Current error: 0.00176434153957

Current iteration: 3971
Current error: 0.00170592958594

Current iteration: 3972
Current error: 0.44397320206

Current iteration: 3973
Current error: 0.00279562416205

Current iteration: 3974
Current error: 0.00268188609967

Current iteration: 3975
Current error: 0.00257521651299

Current iteration: 3976
Current error: 0.00247651980541

Current iteration: 3977
Current error: 0.00237890182729

Current iteration: 3978
Current error: 0.434382770182

Current iteration: 3979
Current error: 0.00382951151477

Current iteration: 3980
Current error: 0.00365029758932

Current iteration: 3981
Current error: 0.00348330745954

Current iteration: 3982
Current error: 0.00333092480799

Current iteration: 3983
Current error: 0.00318134093435

Current iteration: 3984
Current error: 0.00304390960763

Current iteration: 3985
Current error: 0.00291613491013

Current iteration: 3986
Current error: 0.00279503000824

Current iteration: 3987
Current error: 0.00268999744263

Current iteration: 3988
Current error: 0.00257435885522

Current iteration: 3989
Current error: 0.00247357036837

Current iteration: 3990
Current error: 0.00237892093079

Current iteration: 3991
Current error: 0.00228869078297

Current iteration: 3992
Current error: 0.00220381982406

Current iteration: 3993
Current error: 0.00212310756193

Current iteration: 3994
Current error: 0.00204957436764

Current iteration: 3995
Current error: 0.0019748316397

Current iteration: 3996
Current error: 0.00190635201265

Current iteration: 3997
Current error: 0.00184117068494

Current iteration: 3998
Current error: 0.00177930082429

Current iteration: 3999
Current error: 0.00172154325563

Current iteration: 4000
Current error: 0.00166516114858

Current iteration: 4001
Current error: 0.00161093469344

Current iteration: 4002
Current error: 0.00156088892822

Current iteration: 4003
Current error: 0.00151155956301

Current iteration: 4004
Current error: 0.00146543497549

Current iteration: 4005
Current error: 0.00142072276501

Current iteration: 4006
Current error: 0.00137860771101

Current iteration: 4007
Current error: 0.00133989020598

Current iteration: 4008
Current error: 0.00129918511003

Current iteration: 4009
Current error: 0.00126190403252

Current iteration: 4010
Current error: 0.00122630757098

Current iteration: 4011
Current error: 0.00119223953147

Current iteration: 4012
Current error: 0.452881900389

Current iteration: 4013
Current error: 0.00198693546773

Current iteration: 4014
Current error: 0.0019181123124

Current iteration: 4015
Current error: 0.00185314965262

Current iteration: 4016
Current error: 0.00178962706379

Current iteration: 4017
Current error: 0.00173626967241

Current iteration: 4018
Current error: 0.00167967687573

Current iteration: 4019
Current error: 0.00162065979585

Current iteration: 4020
Current error: 0.00156845629183

Current iteration: 4021
Current error: 0.00151953688576

Current iteration: 4022
Current error: 0.00147370033136

Current iteration: 4023
Current error: 0.00142822197766

Current iteration: 4024
Current error: 0.00138616503828

Current iteration: 4025
Current error: 0.00134466812052

Current iteration: 4026
Current error: 0.00130553672007

Current iteration: 4027
Current error: 0.00126815156042

Current iteration: 4028
Current error: 0.00123236484322

Current iteration: 4029
Current error: 0.00119787974805

Current iteration: 4030
Current error: 0.00116556896443

Current iteration: 4031
Current error: 0.00113314583216

Current iteration: 4032
Current error: 0.00110294861427

Current iteration: 4033
Current error: 0.00108009504102

Current iteration: 4034
Current error: 0.00104553477364

Current iteration: 4035
Current error: 0.00101845043958

Current iteration: 4036
Current error: 0.000992708722288

Current iteration: 4037
Current error: 0.000968880705033

Current iteration: 4038
Current error: 0.000944321908294

Current iteration: 4039
Current error: 0.000920562622523

Current iteration: 4040
Current error: 0.000898191767777

Current iteration: 4041
Current error: 0.000880769073849

Current iteration: 4042
Current error: 0.000855231005298

Current iteration: 4043
Current error: 0.000835137122768

Current iteration: 4044
Current error: 0.000815769859672

Current iteration: 4045
Current error: 0.000797609610797

Current iteration: 4046
Current error: 0.000784935033806

Current iteration: 4047
Current error: 0.00076287702223

Current iteration: 4048
Current error: 0.000744719257874

Current iteration: 4049
Current error: 0.00072845299683

Current iteration: 4050
Current error: 0.000712165809919

Current iteration: 4051
Current error: 0.000696893481747

Current iteration: 4052
Current error: 0.46348966649

Current iteration: 4053
Current error: 0.00118418314747

Current iteration: 4054
Current error: 0.00115123273149

Current iteration: 4055
Current error: 0.00112046883276

Current iteration: 4056
Current error: 0.00109145423037

Current iteration: 4057
Current error: 0.00106167674567

Current iteration: 4058
Current error: 0.455312054238

Current iteration: 4059
Current error: 0.00177672539675

Current iteration: 4060
Current error: 0.00171957032883

Current iteration: 4061
Current error: 0.00167324525374

Current iteration: 4062
Current error: 0.00160842526636

Current iteration: 4063
Current error: 0.00155786263861

Current iteration: 4064
Current error: 0.00150934709029

Current iteration: 4065
Current error: 0.00146291311086

Current iteration: 4066
Current error: 0.00141867899322

Current iteration: 4067
Current error: 0.00137848094052

Current iteration: 4068
Current error: 0.00133947081776

Current iteration: 4069
Current error: 0.00129749863129

Current iteration: 4070
Current error: 0.00126033333806

Current iteration: 4071
Current error: 0.00123516744924

Current iteration: 4072
Current error: 0.00119102763832

Current iteration: 4073
Current error: 0.00116315976946

Current iteration: 4074
Current error: 0.00112994817728

Current iteration: 4075
Current error: 0.453999386919

Current iteration: 4076
Current error: 0.00188202399149

Current iteration: 4077
Current error: 0.00181631132261

Current iteration: 4078
Current error: 0.0017557184637

Current iteration: 4079
Current error: 0.00169819756839

Current iteration: 4080
Current error: 0.00164315344063

Current iteration: 4081
Current error: 0.00159424392102

Current iteration: 4082
Current error: 0.00154071408216

Current iteration: 4083
Current error: 0.0014927724436

Current iteration: 4084
Current error: 0.0014475125871

Current iteration: 4085
Current error: 0.00140682563585

Current iteration: 4086
Current error: 0.448844382173

Current iteration: 4087
Current error: 0.00232167320064

Current iteration: 4088
Current error: 0.00223869494946

Current iteration: 4089
Current error: 0.0021517840667

Current iteration: 4090
Current error: 0.00207462977099

Current iteration: 4091
Current error: 0.00200079436488

Current iteration: 4092
Current error: 0.00193081065995

Current iteration: 4093
Current error: 0.00186442173305

Current iteration: 4094
Current error: 0.00180126784703

Current iteration: 4095
Current error: 0.00174138610268

Current iteration: 4096
Current error: 0.0016842177457

Current iteration: 4097
Current error: 0.00163003612037

Current iteration: 4098
Current error: 0.00157825853734

Current iteration: 4099
Current error: 0.00152871206431

Current iteration: 4100
Current error: 0.00148164494405

Current iteration: 4101
Current error: 0.0014374340807

Current iteration: 4102
Current error: 0.00139396626137

Current iteration: 4103
Current error: 0.00135262028974

Current iteration: 4104
Current error: 0.00131370641287

Current iteration: 4105
Current error: 0.00127528925212

Current iteration: 4106
Current error: 0.00123911023142

Current iteration: 4107
Current error: 0.00120676323051

Current iteration: 4108
Current error: 0.00117167397628

Current iteration: 4109
Current error: 0.00113943294364

Current iteration: 4110
Current error: 0.00110856329797

Current iteration: 4111
Current error: 0.00107909226114

Current iteration: 4112
Current error: 0.454802914035

Current iteration: 4113
Current error: 0.00180334635771

Current iteration: 4114
Current error: 0.00174963203145

Current iteration: 4115
Current error: 0.00168625048974

Current iteration: 4116
Current error: 0.00163866182674

Current iteration: 4117
Current error: 0.00158026345645

Current iteration: 4118
Current error: 0.00153041604392

Current iteration: 4119
Current error: 0.00148341191611

Current iteration: 4120
Current error: 0.00143806590945

Current iteration: 4121
Current error: 0.00139480403326

Current iteration: 4122
Current error: 0.00135527870052

Current iteration: 4123
Current error: 0.00131421882402

Current iteration: 4124
Current error: 0.450555320607

Current iteration: 4125
Current error: 0.00217994776063

Current iteration: 4126
Current error: 0.00210105071246

Current iteration: 4127
Current error: 0.438170618861

Current iteration: 4128
Current error: 0.00340729732695

Current iteration: 4129
Current error: 0.00325527888687

Current iteration: 4130
Current error: 0.00311621188351

Current iteration: 4131
Current error: 0.425326952459

Current iteration: 4132
Current error: 0.00492664052996

Current iteration: 4133
Current error: 0.00466918975501

Current iteration: 4134
Current error: 0.00443232164283

Current iteration: 4135
Current error: 0.00421161337735

Current iteration: 4136
Current error: 0.00400573772379

Current iteration: 4137
Current error: 0.00381776473267

Current iteration: 4138
Current error: 0.00363917745809

Current iteration: 4139
Current error: 0.00347385349817

Current iteration: 4140
Current error: 0.00331472985875

Current iteration: 4141
Current error: 0.00316965021114

Current iteration: 4142
Current error: 0.00303320392605

Current iteration: 4143
Current error: 0.0029053302338

Current iteration: 4144
Current error: 0.0027853849215

Current iteration: 4145
Current error: 0.00267231277606

Current iteration: 4146
Current error: 0.00256587616727

Current iteration: 4147
Current error: 0.00246680194627

Current iteration: 4148
Current error: 0.00237079285713

Current iteration: 4149
Current error: 0.00228739660726

Current iteration: 4150
Current error: 0.00219679004584

Current iteration: 4151
Current error: 0.00211683858963

Current iteration: 4152
Current error: 0.00204122383222

Current iteration: 4153
Current error: 0.00196904802984

Current iteration: 4154
Current error: 0.001900749409

Current iteration: 4155
Current error: 0.441066503012

Current iteration: 4156
Current error: 0.00309857150374

Current iteration: 4157
Current error: 0.00296709783497

Current iteration: 4158
Current error: 0.00285288269585

Current iteration: 4159
Current error: 0.00272745667636

Current iteration: 4160
Current error: 0.00261693957244

Current iteration: 4161
Current error: 0.00251677326284

Current iteration: 4162
Current error: 0.00241645832403

Current iteration: 4163
Current error: 0.00232414776395

Current iteration: 4164
Current error: 0.00223792650033

Current iteration: 4165
Current error: 0.00215500706816

Current iteration: 4166
Current error: 0.00207729790828

Current iteration: 4167
Current error: 0.0020043439269

Current iteration: 4168
Current error: 0.00193355924037

Current iteration: 4169
Current error: 0.00187428240087

Current iteration: 4170
Current error: 0.00181306761346

Current iteration: 4171
Current error: 0.00174521430438

Current iteration: 4172
Current error: 0.00168668844321

Current iteration: 4173
Current error: 0.00163240872548

Current iteration: 4174
Current error: 0.00158037029382

Current iteration: 4175
Current error: 0.00153089490664

Current iteration: 4176
Current error: 0.00148357162819

Current iteration: 4177
Current error: 0.00143833426032

Current iteration: 4178
Current error: 0.0013952125504

Current iteration: 4179
Current error: 0.00135468943133

Current iteration: 4180
Current error: 0.00131465121749

Current iteration: 4181
Current error: 0.00127674075874

Current iteration: 4182
Current error: 0.00124051820968

Current iteration: 4183
Current error: 0.00120579017033

Current iteration: 4184
Current error: 0.0011724779472

Current iteration: 4185
Current error: 0.00114053582054

Current iteration: 4186
Current error: 0.0011098330937

Current iteration: 4187
Current error: 0.00108063704617

Current iteration: 4188
Current error: 0.00105199966323

Current iteration: 4189
Current error: 0.00102540097158

Current iteration: 4190
Current error: 0.000998445851454

Current iteration: 4191
Current error: 0.00097318231149

Current iteration: 4192
Current error: 0.000949005545102

Current iteration: 4193
Current error: 0.000925583154606

Current iteration: 4194
Current error: 0.000903113398752

Current iteration: 4195
Current error: 0.000881239394621

Current iteration: 4196
Current error: 0.000860473887015

Current iteration: 4197
Current error: 0.000839910289112

Current iteration: 4198
Current error: 0.00082114940932

Current iteration: 4199
Current error: 0.000801389126803

Current iteration: 4200
Current error: 0.00078312250194

Current iteration: 4201
Current error: 0.000765483087651

Current iteration: 4202
Current error: 0.000748582545064

Current iteration: 4203
Current error: 0.000731948349333

Current iteration: 4204
Current error: 0.000716894951323

Current iteration: 4205
Current error: 0.000700803643064

Current iteration: 4206
Current error: 0.000685685985442

Current iteration: 4207
Current error: 0.000670987699021

Current iteration: 4208
Current error: 0.000656939173911

Current iteration: 4209
Current error: 0.000643468024706

Current iteration: 4210
Current error: 0.000630090432925

Current iteration: 4211
Current error: 0.000617318232258

Current iteration: 4212
Current error: 0.000605071542461

Current iteration: 4213
Current error: 0.000592806990729

Current iteration: 4214
Current error: 0.000581086118587

Current iteration: 4215
Current error: 0.000569748529439

Current iteration: 4216
Current error: 0.000558780475935

Current iteration: 4217
Current error: 0.000547991132524

Current iteration: 4218
Current error: 0.00053748259058

Current iteration: 4219
Current error: 0.000527395679523

Current iteration: 4220
Current error: 0.000517594535276

Current iteration: 4221
Current error: 0.00050807745185

Current iteration: 4222
Current error: 0.000498672678362

Current iteration: 4223
Current error: 0.000490340069721

Current iteration: 4224
Current error: 0.000481683225705

Current iteration: 4225
Current error: 0.000472157711538

Current iteration: 4226
Current error: 0.000463828596279

Current iteration: 4227
Current error: 0.000456214579211

Current iteration: 4228
Current error: 0.000447842947184

Current iteration: 4229
Current error: 0.000440023609004

Current iteration: 4230
Current error: 0.000432502409011

Current iteration: 4231
Current error: 0.000425233837421

Current iteration: 4232
Current error: 0.000419217615235

Current iteration: 4233
Current error: 0.000411005704346

Current iteration: 4234
Current error: 0.000404841603783

Current iteration: 4235
Current error: 0.000397491129788

Current iteration: 4236
Current error: 0.000391149320569

Current iteration: 4237
Current error: 0.00038473406999

Current iteration: 4238
Current error: 0.000378551906001

Current iteration: 4239
Current error: 0.000372477382311

Current iteration: 4240
Current error: 0.00036703844916

Current iteration: 4241
Current error: 0.000360902985975

Current iteration: 4242
Current error: 0.000355289282249

Current iteration: 4243
Current error: 0.000350160733215

Current iteration: 4244
Current error: 0.000344500949548

Current iteration: 4245
Current error: 0.000339205784191

Current iteration: 4246
Current error: 0.0003340600935

Current iteration: 4247
Current error: 0.474604928832

Current iteration: 4248
Current error: 0.000579887366809

Current iteration: 4249
Current error: 0.000568567608346

Current iteration: 4250
Current error: 0.000557911996962

Current iteration: 4251
Current error: 0.000547049692292

Current iteration: 4252
Current error: 0.000536435764333

Current iteration: 4253
Current error: 0.000526330056689

Current iteration: 4254
Current error: 0.468245492601

Current iteration: 4255
Current error: 0.000902605624712

Current iteration: 4256
Current error: 0.458724128421

Current iteration: 4257
Current error: 0.00152028768853

Current iteration: 4258
Current error: 0.00147370190513

Current iteration: 4259
Current error: 0.00142978752155

Current iteration: 4260
Current error: 0.00138638562031

Current iteration: 4261
Current error: 0.00134567082244

Current iteration: 4262
Current error: 0.00130623872545

Current iteration: 4263
Current error: 0.450642465835

Current iteration: 4264
Current error: 0.00216695890455

Current iteration: 4265
Current error: 0.00208858658146

Current iteration: 4266
Current error: 0.00201425977174

Current iteration: 4267
Current error: 0.00194414392483

Current iteration: 4268
Current error: 0.00187668941432

Current iteration: 4269
Current error: 0.0018129972573

Current iteration: 4270
Current error: 0.0017523071257

Current iteration: 4271
Current error: 0.00169481998788

Current iteration: 4272
Current error: 0.00164009077844

Current iteration: 4273
Current error: 0.00158776452776

Current iteration: 4274
Current error: 0.00153787396952

Current iteration: 4275
Current error: 0.00149036368894

Current iteration: 4276
Current error: 0.00144761917441

Current iteration: 4277
Current error: 0.00140318586894

Current iteration: 4278
Current error: 0.00136009365114

Current iteration: 4279
Current error: 0.449674522364

Current iteration: 4280
Current error: 0.00225203701737

Current iteration: 4281
Current error: 0.00216891526205

Current iteration: 4282
Current error: 0.00209011472876

Current iteration: 4283
Current error: 0.00202575275491

Current iteration: 4284
Current error: 0.00194508329853

Current iteration: 4285
Current error: 0.00187799356806

Current iteration: 4286
Current error: 0.00181474519152

Current iteration: 4287
Current error: 0.00175416765712

Current iteration: 4288
Current error: 0.00169627934981

Current iteration: 4289
Current error: 0.00164291168721

Current iteration: 4290
Current error: 0.00159872919776

Current iteration: 4291
Current error: 0.00154518182473

Current iteration: 4292
Current error: 0.00149127260705

Current iteration: 4293
Current error: 0.00144586994116

Current iteration: 4294
Current error: 0.00140244295857

Current iteration: 4295
Current error: 0.00136111147039

Current iteration: 4296
Current error: 0.00132160847115

Current iteration: 4297
Current error: 0.00128312966764

Current iteration: 4298
Current error: 0.00124682768967

Current iteration: 4299
Current error: 0.00121176070771

Current iteration: 4300
Current error: 0.00117864646358

Current iteration: 4301
Current error: 0.00114588621559

Current iteration: 4302
Current error: 0.00111521725733

Current iteration: 4303
Current error: 0.00108613874393

Current iteration: 4304
Current error: 0.00105673927249

Current iteration: 4305
Current error: 0.00102962913948

Current iteration: 4306
Current error: 0.00100278379741

Current iteration: 4307
Current error: 0.000977741062953

Current iteration: 4308
Current error: 0.000952942545235

Current iteration: 4309
Current error: 0.000929421296083

Current iteration: 4310
Current error: 0.458119681092

Current iteration: 4311
Current error: 0.00156555703069

Current iteration: 4312
Current error: 0.00151478807195

Current iteration: 4313
Current error: 0.0014686596066

Current iteration: 4314
Current error: 0.00142397637774

Current iteration: 4315
Current error: 0.00138133480223

Current iteration: 4316
Current error: 0.00134072519185

Current iteration: 4317
Current error: 0.00130186211299

Current iteration: 4318
Current error: 0.00126466598746

Current iteration: 4319
Current error: 0.0012288331077

Current iteration: 4320
Current error: 0.00119473812024

Current iteration: 4321
Current error: 0.00116169210177

Current iteration: 4322
Current error: 0.00113010467105

Current iteration: 4323
Current error: 0.00110075464722

Current iteration: 4324
Current error: 0.454566418919

Current iteration: 4325
Current error: 0.00183845624459

Current iteration: 4326
Current error: 0.00177650789992

Current iteration: 4327
Current error: 0.0017182180063

Current iteration: 4328
Current error: 0.0016617579817

Current iteration: 4329
Current error: 0.00161053436692

Current iteration: 4330
Current error: 0.00155763077918

Current iteration: 4331
Current error: 0.00150926868298

Current iteration: 4332
Current error: 0.00146314108874

Current iteration: 4333
Current error: 0.00141882309635

Current iteration: 4334
Current error: 0.00137674128949

Current iteration: 4335
Current error: 0.00134128307084

Current iteration: 4336
Current error: 0.00129728680478

Current iteration: 4337
Current error: 0.00126022809096

Current iteration: 4338
Current error: 0.00122466634873

Current iteration: 4339
Current error: 0.00119047931839

Current iteration: 4340
Current error: 0.00115801404158

Current iteration: 4341
Current error: 0.00112660746691

Current iteration: 4342
Current error: 0.00109647885281

Current iteration: 4343
Current error: 0.00107331904481

Current iteration: 4344
Current error: 0.00103968424136

Current iteration: 4345
Current error: 0.00102188828018

Current iteration: 4346
Current error: 0.00098848713847

Current iteration: 4347
Current error: 0.000962032453681

Current iteration: 4348
Current error: 0.000938533813534

Current iteration: 4349
Current error: 0.000915164091857

Current iteration: 4350
Current error: 0.000892950088717

Current iteration: 4351
Current error: 0.459032847896

Current iteration: 4352
Current error: 0.00150548490662

Current iteration: 4353
Current error: 0.0014593633679

Current iteration: 4354
Current error: 0.00142266953335

Current iteration: 4355
Current error: 0.00137301374286

Current iteration: 4356
Current error: 0.00133264143578

Current iteration: 4357
Current error: 0.00129415937642

Current iteration: 4358
Current error: 0.0012572610476

Current iteration: 4359
Current error: 0.00122191416274

Current iteration: 4360
Current error: 0.00118781597552

Current iteration: 4361
Current error: 0.00115547038798

Current iteration: 4362
Current error: 0.00112399424735

Current iteration: 4363
Current error: 0.00110087247378

Current iteration: 4364
Current error: 0.00106566377784

Current iteration: 4365
Current error: 0.00103721208429

Current iteration: 4366
Current error: 0.00101484940729

Current iteration: 4367
Current error: 0.000984816825

Current iteration: 4368
Current error: 0.00096003103957

Current iteration: 4369
Current error: 0.000936402237347

Current iteration: 4370
Current error: 0.000913621245553

Current iteration: 4371
Current error: 0.000891212248376

Current iteration: 4372
Current error: 0.000869799695334

Current iteration: 4373
Current error: 0.000849125689582

Current iteration: 4374
Current error: 0.000830056962727

Current iteration: 4375
Current error: 0.00081008955893

Current iteration: 4376
Current error: 0.00079148396755

Current iteration: 4377
Current error: 0.000773707910077

Current iteration: 4378
Current error: 0.000756582253321

Current iteration: 4379
Current error: 0.00073949085577

Current iteration: 4380
Current error: 0.000723257687729

Current iteration: 4381
Current error: 0.000707813631575

Current iteration: 4382
Current error: 0.000692386324676

Current iteration: 4383
Current error: 0.000677659840383

Current iteration: 4384
Current error: 0.000663385901504

Current iteration: 4385
Current error: 0.000649879565419

Current iteration: 4386
Current error: 0.000636727635882

Current iteration: 4387
Current error: 0.000623186210523

Current iteration: 4388
Current error: 0.000610588681838

Current iteration: 4389
Current error: 0.000601248517922

Current iteration: 4390
Current error: 0.000588437435004

Current iteration: 4391
Current error: 0.000575243104006

Current iteration: 4392
Current error: 0.000563718495918

Current iteration: 4393
Current error: 0.000552898686728

Current iteration: 4394
Current error: 0.000542320598691

Current iteration: 4395
Current error: 0.000532406214757

Current iteration: 4396
Current error: 0.000525919254576

Current iteration: 4397
Current error: 0.00051231557733

Current iteration: 4398
Current error: 0.000502941535069

Current iteration: 4399
Current error: 0.000494239902172

Current iteration: 4400
Current error: 0.000484775622995

Current iteration: 4401
Current error: 0.000476168557165

Current iteration: 4402
Current error: 0.000467685495058

Current iteration: 4403
Current error: 0.000459430950658

Current iteration: 4404
Current error: 0.000451373648233

Current iteration: 4405
Current error: 0.000443494981781

Current iteration: 4406
Current error: 0.000436673767459

Current iteration: 4407
Current error: 0.000428599954782

Current iteration: 4408
Current error: 0.00042119026605

Current iteration: 4409
Current error: 0.000414115378664

Current iteration: 4410
Current error: 0.000408036216751

Current iteration: 4411
Current error: 0.000400649681776

Current iteration: 4412
Current error: 0.00039408189955

Current iteration: 4413
Current error: 0.00038766304585

Current iteration: 4414
Current error: 0.000381361663718

Current iteration: 4415
Current error: 0.000375351933512

Current iteration: 4416
Current error: 0.000369707678832

Current iteration: 4417
Current error: 0.000363474620773

Current iteration: 4418
Current error: 0.000357838129465

Current iteration: 4419
Current error: 0.000352284914896

Current iteration: 4420
Current error: 0.000346855398122

Current iteration: 4421
Current error: 0.000341598989524

Current iteration: 4422
Current error: 0.000336428302383

Current iteration: 4423
Current error: 0.000333515466197

Current iteration: 4424
Current error: 0.000327671198469

Current iteration: 4425
Current error: 0.000321600534832

Current iteration: 4426
Current error: 0.000316799575227

Current iteration: 4427
Current error: 0.000312775719229

Current iteration: 4428
Current error: 0.000307754425567

Current iteration: 4429
Current error: 0.00030320618261

Current iteration: 4430
Current error: 0.000298922924868

Current iteration: 4431
Current error: 0.000294636286142

Current iteration: 4432
Current error: 0.000290500428136

Current iteration: 4433
Current error: 0.000286466633827

Current iteration: 4434
Current error: 0.000282420566008

Current iteration: 4435
Current error: 0.000278521176568

Current iteration: 4436
Current error: 0.000274651571191

Current iteration: 4437
Current error: 0.476918116283

Current iteration: 4438
Current error: 0.000478878358677

Current iteration: 4439
Current error: 0.000470271470638

Current iteration: 4440
Current error: 0.000462027802279

Current iteration: 4441
Current error: 0.000453926883028

Current iteration: 4442
Current error: 0.000446078603865

Current iteration: 4443
Current error: 0.000438383356163

Current iteration: 4444
Current error: 0.00043098067515

Current iteration: 4445
Current error: 0.000423562865685

Current iteration: 4446
Current error: 0.000416438786969

Current iteration: 4447
Current error: 0.00040946475271

Current iteration: 4448
Current error: 0.000402684385962

Current iteration: 4449
Current error: 0.000396168556857

Current iteration: 4450
Current error: 0.000389695843924

Current iteration: 4451
Current error: 0.0003833628441

Current iteration: 4452
Current error: 0.000377266068535

Current iteration: 4453
Current error: 0.000371263944664

Current iteration: 4454
Current error: 0.000365363669863

Current iteration: 4455
Current error: 0.473418753768

Current iteration: 4456
Current error: 0.000632633060986

Current iteration: 4457
Current error: 0.000619905084207

Current iteration: 4458
Current error: 0.465428840436

Current iteration: 4459
Current error: 0.454675014595

Current iteration: 4460
Current error: 0.00181276461295

Current iteration: 4461
Current error: 0.00175221921547

Current iteration: 4462
Current error: 0.00169499411636

Current iteration: 4463
Current error: 0.00163995771565

Current iteration: 4464
Current error: 0.00159894832249

Current iteration: 4465
Current error: 0.00153824337141

Current iteration: 4466
Current error: 0.00149153893322

Current iteration: 4467
Current error: 0.00144513163633

Current iteration: 4468
Current error: 0.00140332664759

Current iteration: 4469
Current error: 0.00135975391843

Current iteration: 4470
Current error: 0.00132002700611

Current iteration: 4471
Current error: 0.00128210511773

Current iteration: 4472
Current error: 0.00124569985999

Current iteration: 4473
Current error: 0.00121073554924

Current iteration: 4474
Current error: 0.00117725910241

Current iteration: 4475
Current error: 0.00114498728743

Current iteration: 4476
Current error: 0.00111636354773

Current iteration: 4477
Current error: 0.00108582816358

Current iteration: 4478
Current error: 0.00105593118955

Current iteration: 4479
Current error: 0.00102843584298

Current iteration: 4480
Current error: 0.00100614942517

Current iteration: 4481
Current error: 0.456518178314

Current iteration: 4482
Current error: 0.00168060806347

Current iteration: 4483
Current error: 0.00162645547461

Current iteration: 4484
Current error: 0.00157480295269

Current iteration: 4485
Current error: 0.0015255403418

Current iteration: 4486
Current error: 0.00147955918418

Current iteration: 4487
Current error: 0.00144044669228

Current iteration: 4488
Current error: 0.00139232161124

Current iteration: 4489
Current error: 0.00136013063443

Current iteration: 4490
Current error: 0.00131024493601

Current iteration: 4491
Current error: 0.00127268990117

Current iteration: 4492
Current error: 0.00123719286863

Current iteration: 4493
Current error: 0.00120200361443

Current iteration: 4494
Current error: 0.00117095859455

Current iteration: 4495
Current error: 0.00113698621105

Current iteration: 4496
Current error: 0.00111291922938

Current iteration: 4497
Current error: 0.00107711252103

Current iteration: 4498
Current error: 0.00104896386172

Current iteration: 4499
Current error: 0.00102175294479

Current iteration: 4500
Current error: 0.000995623734158

Current iteration: 4501
Current error: 0.000970453307496

Current iteration: 4502
Current error: 0.000946295265646

Current iteration: 4503
Current error: 0.000922916863637

Current iteration: 4504
Current error: 0.000901760412453

Current iteration: 4505
Current error: 0.458549518211

Current iteration: 4506
Current error: 0.00151506498599

Current iteration: 4507
Current error: 0.00146872225876

Current iteration: 4508
Current error: 0.00142405079436

Current iteration: 4509
Current error: 0.00138155658719

Current iteration: 4510
Current error: 0.00134105615574

Current iteration: 4511
Current error: 0.00130203556752

Current iteration: 4512
Current error: 0.0012649837858

Current iteration: 4513
Current error: 0.0012290932658

Current iteration: 4514
Current error: 0.00119497973607

Current iteration: 4515
Current error: 0.00116209164899

Current iteration: 4516
Current error: 0.0011303442747

Current iteration: 4517
Current error: 0.00110027145591

Current iteration: 4518
Current error: 0.00107107477779

Current iteration: 4519
Current error: 0.00104532828402

Current iteration: 4520
Current error: 0.00101617608882

Current iteration: 4521
Current error: 0.00099009674359

Current iteration: 4522
Current error: 0.000965170474565

Current iteration: 4523
Current error: 0.000942540197231

Current iteration: 4524
Current error: 0.00091807591656

Current iteration: 4525
Current error: 0.000895725285163

Current iteration: 4526
Current error: 0.000874359642128

Current iteration: 4527
Current error: 0.000853513958472

Current iteration: 4528
Current error: 0.000833504022129

Current iteration: 4529
Current error: 0.000814026154432

Current iteration: 4530
Current error: 0.000795325129816

Current iteration: 4531
Current error: 0.000777279733522

Current iteration: 4532
Current error: 0.000759786728879

Current iteration: 4533
Current error: 0.000742917003629

Current iteration: 4534
Current error: 0.000726785646242

Current iteration: 4535
Current error: 0.000710808914289

Current iteration: 4536
Current error: 0.000695981819639

Current iteration: 4537
Current error: 0.000680737251282

Current iteration: 4538
Current error: 0.000666289204965

Current iteration: 4539
Current error: 0.000652983100294

Current iteration: 4540
Current error: 0.000639082699045

Current iteration: 4541
Current error: 0.00062589054394

Current iteration: 4542
Current error: 0.000613126675537

Current iteration: 4543
Current error: 0.00060086527511

Current iteration: 4544
Current error: 0.00058892153656

Current iteration: 4545
Current error: 0.000577592976839

Current iteration: 4546
Current error: 0.000566035873951

Current iteration: 4547
Current error: 0.000559834238536

Current iteration: 4548
Current error: 0.000545380699933

Current iteration: 4549
Current error: 0.000534154200512

Current iteration: 4550
Current error: 0.000524117049313

Current iteration: 4551
Current error: 0.000514343993461

Current iteration: 4552
Current error: 0.000505406245312

Current iteration: 4553
Current error: 0.000496211799902

Current iteration: 4554
Current error: 0.000488713481188

Current iteration: 4555
Current error: 0.000477944895157

Current iteration: 4556
Current error: 0.000469435312658

Current iteration: 4557
Current error: 0.000461081802286

Current iteration: 4558
Current error: 0.000453042284638

Current iteration: 4559
Current error: 0.000446365341967

Current iteration: 4560
Current error: 0.000437683612878

Current iteration: 4561
Current error: 0.000430110264159

Current iteration: 4562
Current error: 0.000422767636249

Current iteration: 4563
Current error: 0.000415849238838

Current iteration: 4564
Current error: 0.000408761069428

Current iteration: 4565
Current error: 0.000403917010178

Current iteration: 4566
Current error: 0.000395330553121

Current iteration: 4567
Current error: 0.000392212172946

Current iteration: 4568
Current error: 0.472345724737

Current iteration: 4569
Current error: 0.000671428812416

Current iteration: 4570
Current error: 0.000657382882567

Current iteration: 4571
Current error: 0.00064493552813

Current iteration: 4572
Current error: 0.000630347358554

Current iteration: 4573
Current error: 0.000618245838651

Current iteration: 4574
Current error: 0.000605301059461

Current iteration: 4575
Current error: 0.000593067292653

Current iteration: 4576
Current error: 0.000581363192699

Current iteration: 4577
Current error: 0.000569990529618

Current iteration: 4578
Current error: 0.000560832164829

Current iteration: 4579
Current error: 0.000548282817746

Current iteration: 4580
Current error: 0.467495905285

Current iteration: 4581
Current error: 0.000938238796322

Current iteration: 4582
Current error: 0.000915416994798

Current iteration: 4583
Current error: 0.458606592186

Current iteration: 4584
Current error: 0.00154207205744

Current iteration: 4585
Current error: 0.00149435035707

Current iteration: 4586
Current error: 0.00144882597317

Current iteration: 4587
Current error: 0.00140522647281

Current iteration: 4588
Current error: 0.00136343024779

Current iteration: 4589
Current error: 0.00134049593787

Current iteration: 4590
Current error: 0.0012852606401

Current iteration: 4591
Current error: 0.00124890977026

Current iteration: 4592
Current error: 0.00121420494021

Current iteration: 4593
Current error: 0.00118001858391

Current iteration: 4594
Current error: 0.00114762237886

Current iteration: 4595
Current error: 0.00111668569942

Current iteration: 4596
Current error: 0.00108691368174

Current iteration: 4597
Current error: 0.00105851831924

Current iteration: 4598
Current error: 0.0010361999846

Current iteration: 4599
Current error: 0.00100433680355

Current iteration: 4600
Current error: 0.000979107609817

Current iteration: 4601
Current error: 0.000954490564734

Current iteration: 4602
Current error: 0.000931771916699

Current iteration: 4603
Current error: 0.000908098950355

Current iteration: 4604
Current error: 0.000886076274694

Current iteration: 4605
Current error: 0.000875143324868

Current iteration: 4606
Current error: 0.000844591627444

Current iteration: 4607
Current error: 0.000824591927885

Current iteration: 4608
Current error: 0.000805566761922

Current iteration: 4609
Current error: 0.000787669712499

Current iteration: 4610
Current error: 0.000769378731751

Current iteration: 4611
Current error: 0.000752251823005

Current iteration: 4612
Current error: 0.000735499623056

Current iteration: 4613
Current error: 0.000722665326488

Current iteration: 4614
Current error: 0.000703794239898

Current iteration: 4615
Current error: 0.000688899552651

Current iteration: 4616
Current error: 0.000674197670229

Current iteration: 4617
Current error: 0.000661127711265

Current iteration: 4618
Current error: 0.00064627329063

Current iteration: 4619
Current error: 0.464823375306

Current iteration: 4620
Current error: 0.00110097290493

Current iteration: 4621
Current error: 0.00107178693732

Current iteration: 4622
Current error: 0.00104384640162

Current iteration: 4623
Current error: 0.455404311506

Current iteration: 4624
Current error: 0.00174602438151

Current iteration: 4625
Current error: 0.443328104045

Current iteration: 4626
Current error: 0.0028569824139

Current iteration: 4627
Current error: 0.00273952355679

Current iteration: 4628
Current error: 0.00262951262294

Current iteration: 4629
Current error: 0.00252556129524

Current iteration: 4630
Current error: 0.00242760016947

Current iteration: 4631
Current error: 0.00233466164567

Current iteration: 4632
Current error: 0.0022494810162

Current iteration: 4633
Current error: 0.00216702356331

Current iteration: 4634
Current error: 0.00208758719122

Current iteration: 4635
Current error: 0.00201207478542

Current iteration: 4636
Current error: 0.0019413948672

Current iteration: 4637
Current error: 0.00187457870819

Current iteration: 4638
Current error: 0.00181092417114

Current iteration: 4639
Current error: 0.00175078820172

Current iteration: 4640
Current error: 0.00170025505121

Current iteration: 4641
Current error: 0.00164010814939

Current iteration: 4642
Current error: 0.00158615420686

Current iteration: 4643
Current error: 0.00153646619915

Current iteration: 4644
Current error: 0.00148966148444

Current iteration: 4645
Current error: 0.00144351386827

Current iteration: 4646
Current error: 0.00140027981521

Current iteration: 4647
Current error: 0.00135877915009

Current iteration: 4648
Current error: 0.00131924586367

Current iteration: 4649
Current error: 0.450662733189

Current iteration: 4650
Current error: 0.435462457629

Current iteration: 4651
Current error: 0.00366556798518

Current iteration: 4652
Current error: 0.00350098907343

Current iteration: 4653
Current error: 0.00334016606299

Current iteration: 4654
Current error: 0.00319357432933

Current iteration: 4655
Current error: 0.00305582522035

Current iteration: 4656
Current error: 0.00292649124629

Current iteration: 4657
Current error: 0.00280541154037

Current iteration: 4658
Current error: 0.00269177026045

Current iteration: 4659
Current error: 0.00258369575888

Current iteration: 4660
Current error: 0.00248241488338

Current iteration: 4661
Current error: 0.00238656722124

Current iteration: 4662
Current error: 0.43408089973

Current iteration: 4663
Current error: 0.00383776954049

Current iteration: 4664
Current error: 0.416966215446

Current iteration: 4665
Current error: 0.00597773975175

Current iteration: 4666
Current error: 0.00563699718731

Current iteration: 4667
Current error: 0.00532457554276

Current iteration: 4668
Current error: 0.00504256668198

Current iteration: 4669
Current error: 0.00477181494057

Current iteration: 4670
Current error: 0.00452627250249

Current iteration: 4671
Current error: 0.0042985898445

Current iteration: 4672
Current error: 0.00408807874352

Current iteration: 4673
Current error: 0.415118590325

Current iteration: 4674
Current error: 0.00634678756613

Current iteration: 4675
Current error: 0.00597916249998

Current iteration: 4676
Current error: 0.00563984792256

Current iteration: 4677
Current error: 0.00532746041047

Current iteration: 4678
Current error: 0.00503951577514

Current iteration: 4679
Current error: 0.00477391886426

Current iteration: 4680
Current error: 0.00452813253774

Current iteration: 4681
Current error: 0.00430148164479

Current iteration: 4682
Current error: 0.00408887230407

Current iteration: 4683
Current error: 0.0038923485925

Current iteration: 4684
Current error: 0.00370895845132

Current iteration: 4685
Current error: 0.00353819749223

Current iteration: 4686
Current error: 0.00337846554199

Current iteration: 4687
Current error: 0.00322893389923

Current iteration: 4688
Current error: 0.00308908013554

Current iteration: 4689
Current error: 0.00295807302813

Current iteration: 4690
Current error: 0.00283445032079

Current iteration: 4691
Current error: 0.00271930265431

Current iteration: 4692
Current error: 0.00260970706843

Current iteration: 4693
Current error: 0.0025068858159

Current iteration: 4694
Current error: 0.00241202897514

Current iteration: 4695
Current error: 0.00232763963207

Current iteration: 4696
Current error: 0.00223153472398

Current iteration: 4697
Current error: 0.00215127021768

Current iteration: 4698
Current error: 0.00207272731859

Current iteration: 4699
Current error: 0.00199848632934

Current iteration: 4700
Current error: 0.00192878616469

Current iteration: 4701
Current error: 0.0018629124227

Current iteration: 4702
Current error: 0.0017997112759

Current iteration: 4703
Current error: 0.00173982226374

Current iteration: 4704
Current error: 0.443204739101

Current iteration: 4705
Current error: 0.00284518684657

Current iteration: 4706
Current error: 0.00272858701529

Current iteration: 4707
Current error: 0.00261898442133

Current iteration: 4708
Current error: 0.00251665803997

Current iteration: 4709
Current error: 0.432516904626

Current iteration: 4710
Current error: 0.00403467116991

Current iteration: 4711
Current error: 0.00384162561691

Current iteration: 4712
Current error: 0.00366201540416

Current iteration: 4713
Current error: 0.00349525837608

Current iteration: 4714
Current error: 0.00335028159979

Current iteration: 4715
Current error: 0.00319026010927

Current iteration: 4716
Current error: 0.0030531162394

Current iteration: 4717
Current error: 0.00292417399926

Current iteration: 4718
Current error: 0.00280383049703

Current iteration: 4719
Current error: 0.00268917677606

Current iteration: 4720
Current error: 0.00258107492742

Current iteration: 4721
Current error: 0.00247996555265

Current iteration: 4722
Current error: 0.00238432079329

Current iteration: 4723
Current error: 0.433771708676

Current iteration: 4724
Current error: 0.415806800663

Current iteration: 4725
Current error: 0.0062593733936

Current iteration: 4726
Current error: 0.00589238889884

Current iteration: 4727
Current error: 0.00556026766015

Current iteration: 4728
Current error: 0.00525623177742

Current iteration: 4729
Current error: 0.00497302228044

Current iteration: 4730
Current error: 0.00471480095431

Current iteration: 4731
Current error: 0.409722382575

Current iteration: 4732
Current error: 0.00725029268974

Current iteration: 4733
Current error: 0.38957658128

Current iteration: 4734
Current error: 0.010773664066

Current iteration: 4735
Current error: 0.00997185116811

Current iteration: 4736
Current error: 0.00927314480256

Current iteration: 4737
Current error: 0.00864606671457

Current iteration: 4738
Current error: 0.00807163199151

Current iteration: 4739
Current error: 0.0075528543368

Current iteration: 4740
Current error: 0.00707981975849

Current iteration: 4741
Current error: 0.391115566469

Current iteration: 4742
Current error: 0.010529876361

Current iteration: 4743
Current error: 0.00986844254409

Current iteration: 4744
Current error: 0.00910619642507

Current iteration: 4745
Current error: 0.00848243065839

Current iteration: 4746
Current error: 0.0079251382132

Current iteration: 4747
Current error: 0.00742245975248

Current iteration: 4748
Current error: 0.00695868345883

Current iteration: 4749
Current error: 0.00653952656092

Current iteration: 4750
Current error: 0.00615330452357

Current iteration: 4751
Current error: 0.00580605985278

Current iteration: 4752
Current error: 0.00549307934104

Current iteration: 4753
Current error: 0.00517629086986

Current iteration: 4754
Current error: 0.405133087589

Current iteration: 4755
Current error: 0.00789173048615

Current iteration: 4756
Current error: 0.00738927003127

Current iteration: 4757
Current error: 0.00693163674973

Current iteration: 4758
Current error: 0.00655918852235

Current iteration: 4759
Current error: 0.00612935156563

Current iteration: 4760
Current error: 0.00577856348618

Current iteration: 4761
Current error: 0.00545553900369

Current iteration: 4762
Current error: 0.00515843277222

Current iteration: 4763
Current error: 0.405405600897

Current iteration: 4764
Current error: 0.00787067957232

Current iteration: 4765
Current error: 0.00736786556868

Current iteration: 4766
Current error: 0.388730192787

Current iteration: 4767
Current error: 0.0109056117722

Current iteration: 4768
Current error: 0.0101159085239

Current iteration: 4769
Current error: 0.00940192629856

Current iteration: 4770
Current error: 0.00875864005318

Current iteration: 4771
Current error: 0.00817741722007

Current iteration: 4772
Current error: 0.00764980886923

Current iteration: 4773
Current error: 0.00716829320742

Current iteration: 4774
Current error: 0.00673227809024

Current iteration: 4775
Current error: 0.00632790735889

Current iteration: 4776
Current error: 0.396174518218

Current iteration: 4777
Current error: 0.00949360763342

Current iteration: 4778
Current error: 0.0088428971021

Current iteration: 4779
Current error: 0.00825060566724

Current iteration: 4780
Current error: 0.00771570634161

Current iteration: 4781
Current error: 0.00722925941863

Current iteration: 4782
Current error: 0.00678509933903

Current iteration: 4783
Current error: 0.00637907249037

Current iteration: 4784
Current error: 0.00602540190274

Current iteration: 4785
Current error: 0.00567327183128

Current iteration: 4786
Current error: 0.00535222107257

Current iteration: 4787
Current error: 0.00506252072098

Current iteration: 4788
Current error: 0.00479571521506

Current iteration: 4789
Current error: 0.00455228390651

Current iteration: 4790
Current error: 0.00431965882466

Current iteration: 4791
Current error: 0.00410625001642

Current iteration: 4792
Current error: 0.00390795900094

Current iteration: 4793
Current error: 0.00372367061958

Current iteration: 4794
Current error: 0.0035517335009

Current iteration: 4795
Current error: 0.00339112248777

Current iteration: 4796
Current error: 0.00324089901427

Current iteration: 4797
Current error: 0.00310111034943

Current iteration: 4798
Current error: 0.00296883367232

Current iteration: 4799
Current error: 0.00284433766913

Current iteration: 4800
Current error: 0.00272808749585

Current iteration: 4801
Current error: 0.00261822961082

Current iteration: 4802
Current error: 0.00252708059711

Current iteration: 4803
Current error: 0.00242117618976

Current iteration: 4804
Current error: 0.00232652522894

Current iteration: 4805
Current error: 0.434656139842

Current iteration: 4806
Current error: 0.00374241169935

Current iteration: 4807
Current error: 0.00356886711526

Current iteration: 4808
Current error: 0.00340738031457

Current iteration: 4809
Current error: 0.00325619965206

Current iteration: 4810
Current error: 0.00311970448892

Current iteration: 4811
Current error: 0.00298516311814

Current iteration: 4812
Current error: 0.00285683899298

Current iteration: 4813
Current error: 0.0027394836983

Current iteration: 4814
Current error: 0.00262915579717

Current iteration: 4815
Current error: 0.0025259354922

Current iteration: 4816
Current error: 0.00243099852967

Current iteration: 4817
Current error: 0.00233479956408

Current iteration: 4818
Current error: 0.0022512329544

Current iteration: 4819
Current error: 0.00216440523297

Current iteration: 4820
Current error: 0.00208677486928

Current iteration: 4821
Current error: 0.00201323488369

Current iteration: 4822
Current error: 0.00195399843358

Current iteration: 4823
Current error: 0.00187502683583

Current iteration: 4824
Current error: 0.00181107484091

Current iteration: 4825
Current error: 0.00175064746355

Current iteration: 4826
Current error: 0.0016934535648

Current iteration: 4827
Current error: 0.00163843815387

Current iteration: 4828
Current error: 0.00158622878785

Current iteration: 4829
Current error: 0.00153703976005

Current iteration: 4830
Current error: 0.00148904035873

Current iteration: 4831
Current error: 0.00144353092044

Current iteration: 4832
Current error: 0.00140009597885

Current iteration: 4833
Current error: 0.00135883599038

Current iteration: 4834
Current error: 0.00132113086715

Current iteration: 4835
Current error: 0.00128112069679

Current iteration: 4836
Current error: 0.00124472133417

Current iteration: 4837
Current error: 0.00120969022486

Current iteration: 4838
Current error: 0.00118642886735

Current iteration: 4839
Current error: 0.452494035321

Current iteration: 4840
Current error: 0.00197513080153

Current iteration: 4841
Current error: 0.00189086945179

Current iteration: 4842
Current error: 0.00182449721177

Current iteration: 4843
Current error: 0.00176206674062

Current iteration: 4844
Current error: 0.00170412840103

Current iteration: 4845
Current error: 0.00164872560136

Current iteration: 4846
Current error: 0.00159972925102

Current iteration: 4847
Current error: 0.00154587355935

Current iteration: 4848
Current error: 0.00149792063248

Current iteration: 4849
Current error: 0.00145210949374

Current iteration: 4850
Current error: 0.0014084120156

Current iteration: 4851
Current error: 0.00137165999685

Current iteration: 4852
Current error: 0.00132881510564

Current iteration: 4853
Current error: 0.00128826765606

Current iteration: 4854
Current error: 0.00125155390214

Current iteration: 4855
Current error: 0.00121777057475

Current iteration: 4856
Current error: 0.00118257148445

Current iteration: 4857
Current error: 0.00115116292233

Current iteration: 4858
Current error: 0.00111971057205

Current iteration: 4859
Current error: 0.00108928618902

Current iteration: 4860
Current error: 0.00106052290539

Current iteration: 4861
Current error: 0.00103316331758

Current iteration: 4862
Current error: 0.00100640753882

Current iteration: 4863
Current error: 0.00098220666717

Current iteration: 4864
Current error: 0.000956259252741

Current iteration: 4865
Current error: 0.000933227720107

Current iteration: 4866
Current error: 0.000909754489698

Current iteration: 4867
Current error: 0.000887783085307

Current iteration: 4868
Current error: 0.000866535048456

Current iteration: 4869
Current error: 0.00084603503528

Current iteration: 4870
Current error: 0.000826272811386

Current iteration: 4871
Current error: 0.000808149745212

Current iteration: 4872
Current error: 0.000788933308921

Current iteration: 4873
Current error: 0.000770790694329

Current iteration: 4874
Current error: 0.000753606770389

Current iteration: 4875
Current error: 0.00073699085751

Current iteration: 4876
Current error: 0.000720856762877

Current iteration: 4877
Current error: 0.000705335687807

Current iteration: 4878
Current error: 0.000690261653786

Current iteration: 4879
Current error: 0.000675501695461

Current iteration: 4880
Current error: 0.000661188418635

Current iteration: 4881
Current error: 0.000647552412206

Current iteration: 4882
Current error: 0.000634165580541

Current iteration: 4883
Current error: 0.000621258524179

Current iteration: 4884
Current error: 0.000608623432189

Current iteration: 4885
Current error: 0.000596450246241

Current iteration: 4886
Current error: 0.000584627851428

Current iteration: 4887
Current error: 0.000573241166138

Current iteration: 4888
Current error: 0.000562051504864

Current iteration: 4889
Current error: 0.000551245351186

Current iteration: 4890
Current error: 0.000540694701879

Current iteration: 4891
Current error: 0.00053061934077

Current iteration: 4892
Current error: 0.000520560317616

Current iteration: 4893
Current error: 0.000510884039457

Current iteration: 4894
Current error: 0.468527385242

Current iteration: 4895
Current error: 0.000885083172548

Current iteration: 4896
Current error: 0.00085616090502

Current iteration: 4897
Current error: 0.000835017430616

Current iteration: 4898
Current error: 0.000815771010639

Current iteration: 4899
Current error: 0.000796831357587

Current iteration: 4900
Current error: 0.00077880119956

Current iteration: 4901
Current error: 0.000761376483964

Current iteration: 4902
Current error: 0.000744529073081

Current iteration: 4903
Current error: 0.000727954767958

Current iteration: 4904
Current error: 0.000712086526615

Current iteration: 4905
Current error: 0.000696678870138

Current iteration: 4906
Current error: 0.000681812538004

Current iteration: 4907
Current error: 0.000669582935784

Current iteration: 4908
Current error: 0.000653547275916

Current iteration: 4909
Current error: 0.000640062817255

Current iteration: 4910
Current error: 0.0006269965698

Current iteration: 4911
Current error: 0.000614238673234

Current iteration: 4912
Current error: 0.000602171645269

Current iteration: 4913
Current error: 0.000589871645272

Current iteration: 4914
Current error: 0.000578291394226

Current iteration: 4915
Current error: 0.000566927600335

Current iteration: 4916
Current error: 0.000556219380871

Current iteration: 4917
Current error: 0.000545347220181

Current iteration: 4918
Current error: 0.000535094595144

Current iteration: 4919
Current error: 0.00052495594411

Current iteration: 4920
Current error: 0.000515990972479

Current iteration: 4921
Current error: 0.000505670669555

Current iteration: 4922
Current error: 0.468198817704

Current iteration: 4923
Current error: 0.00086673977772

Current iteration: 4924
Current error: 0.000844403343494

Current iteration: 4925
Current error: 0.000824759013541

Current iteration: 4926
Current error: 0.000805568769607

Current iteration: 4927
Current error: 0.000787214346221

Current iteration: 4928
Current error: 0.000769467001275

Current iteration: 4929
Current error: 0.000752253676679

Current iteration: 4930
Current error: 0.000736168531805

Current iteration: 4931
Current error: 0.000720197469449

Current iteration: 4932
Current error: 0.000705085637274

Current iteration: 4933
Current error: 0.000690297676502

Current iteration: 4934
Current error: 0.000674237862831

Current iteration: 4935
Current error: 0.000660085015375

Current iteration: 4936
Current error: 0.000646254965031

Current iteration: 4937
Current error: 0.464850628646

Current iteration: 4938
Current error: 0.00110104420626

Current iteration: 4939
Current error: 0.00107272646984

Current iteration: 4940
Current error: 0.00104543017203

Current iteration: 4941
Current error: 0.00101728121504

Current iteration: 4942
Current error: 0.000990916325595

Current iteration: 4943
Current error: 0.000966178546058

Current iteration: 4944
Current error: 0.000942142763587

Current iteration: 4945
Current error: 0.000919634645058

Current iteration: 4946
Current error: 0.000896390936837

Current iteration: 4947
Current error: 0.000874846065312

Current iteration: 4948
Current error: 0.000854230219607

Current iteration: 4949
Current error: 0.000834027235444

Current iteration: 4950
Current error: 0.000814678182616

Current iteration: 4951
Current error: 0.000796380232351

Current iteration: 4952
Current error: 0.000777890192642

Current iteration: 4953
Current error: 0.000765259876677

Current iteration: 4954
Current error: 0.00074357560107

Current iteration: 4955
Current error: 0.000727296524146

Current iteration: 4956
Current error: 0.000711583837186

Current iteration: 4957
Current error: 0.00069597710976

Current iteration: 4958
Current error: 0.00068249783432

Current iteration: 4959
Current error: 0.463749765006

Current iteration: 4960
Current error: 0.00115720476249

Current iteration: 4961
Current error: 0.0011258488101

Current iteration: 4962
Current error: 0.00109584210631

Current iteration: 4963
Current error: 0.00106682611325

Current iteration: 4964
Current error: 0.00103896437237

Current iteration: 4965
Current error: 0.00101219291472

Current iteration: 4966
Current error: 0.00098700909493

Current iteration: 4967
Current error: 0.000961725593183

Current iteration: 4968
Current error: 0.00093776852873

Current iteration: 4969
Current error: 0.000915042300698

Current iteration: 4970
Current error: 0.000894053620651

Current iteration: 4971
Current error: 0.000871340919037

Current iteration: 4972
Current error: 0.000850543822263

Current iteration: 4973
Current error: 0.000831073009714

Current iteration: 4974
Current error: 0.000811353884823

Current iteration: 4975
Current error: 0.000792908466269

Current iteration: 4976
Current error: 0.000779370536408

Current iteration: 4977
Current error: 0.000763379663644

Current iteration: 4978
Current error: 0.000740639891898

Current iteration: 4979
Current error: 0.000724267271617

Current iteration: 4980
Current error: 0.000708559374341

Current iteration: 4981
Current error: 0.000693364584354

Current iteration: 4982
Current error: 0.46337391027

Current iteration: 4983
Current error: 0.00117738177909

Current iteration: 4984
Current error: 0.00114451852347

Current iteration: 4985
Current error: 0.00111530326173

Current iteration: 4986
Current error: 0.0010860836255

Current iteration: 4987
Current error: 0.00105723498234

Current iteration: 4988
Current error: 0.455194347087

Current iteration: 4989
Current error: 0.00176624375563

Current iteration: 4990
Current error: 0.00170633941517

Current iteration: 4991
Current error: 0.00165792235854

Current iteration: 4992
Current error: 0.00159836143116

Current iteration: 4993
Current error: 0.00154796185039

Current iteration: 4994
Current error: 0.00149983011291

Current iteration: 4995
Current error: 0.0014539797019

Current iteration: 4996
Current error: 0.00141024590719

Current iteration: 4997
Current error: 0.00136828372156

Current iteration: 4998
Current error: 0.00134301988412

Current iteration: 4999
Current error: 0.00128973811538

Current iteration: 5000
Current error: 0.00126362521068

Current iteration: 5001
Current error: 0.451558573739

Current iteration: 5002
Current error: 0.00208166180849

Current iteration: 5003
Current error: 0.00201245207585

Current iteration: 5004
Current error: 0.00193735613627

Current iteration: 5005
Current error: 0.0018755608613

Current iteration: 5006
Current error: 0.00180727866635

Current iteration: 5007
Current error: 0.00174709029355

Current iteration: 5008
Current error: 0.00168992304912

Current iteration: 5009
Current error: 0.00163596856642

Current iteration: 5010
Current error: 0.00158316915657

Current iteration: 5011
Current error: 0.00153364968841

Current iteration: 5012
Current error: 0.00148807377318

Current iteration: 5013
Current error: 0.00144109529717

Current iteration: 5014
Current error: 0.00139764622523

Current iteration: 5015
Current error: 0.00135758874209

Current iteration: 5016
Current error: 0.00131684024936

Current iteration: 5017
Current error: 0.00127946561225

Current iteration: 5018
Current error: 0.00124259907273

Current iteration: 5019
Current error: 0.00120768609288

Current iteration: 5020
Current error: 0.45243074411

Current iteration: 5021
Current error: 0.00201002168407

Current iteration: 5022
Current error: 0.00193972158413

Current iteration: 5023
Current error: 0.00187310304009

Current iteration: 5024
Current error: 0.441085789553

Current iteration: 5025
Current error: 0.00305080857844

Current iteration: 5026
Current error: 0.00292235177562

Current iteration: 5027
Current error: 0.00280553398446

Current iteration: 5028
Current error: 0.00268639023223

Current iteration: 5029
Current error: 0.0025791659826

Current iteration: 5030
Current error: 0.00247827916311

Current iteration: 5031
Current error: 0.00238267491776

Current iteration: 5032
Current error: 0.0022926904795

Current iteration: 5033
Current error: 0.00220740641542

Current iteration: 5034
Current error: 0.00212698286986

Current iteration: 5035
Current error: 0.00205045765075

Current iteration: 5036
Current error: 0.0019784965557

Current iteration: 5037
Current error: 0.00190989248401

Current iteration: 5038
Current error: 0.00184408909696

Current iteration: 5039
Current error: 0.00178222419791

Current iteration: 5040
Current error: 0.00173366193991

Current iteration: 5041
Current error: 0.0016667926027

Current iteration: 5042
Current error: 0.00161333095492

Current iteration: 5043
Current error: 0.00156250410628

Current iteration: 5044
Current error: 0.00151397170634

Current iteration: 5045
Current error: 0.00146728403127

Current iteration: 5046
Current error: 0.00142303242261

Current iteration: 5047
Current error: 0.00138922429687

Current iteration: 5048
Current error: 0.00134005279589

Current iteration: 5049
Current error: 0.00130074286189

Current iteration: 5050
Current error: 0.00126357181602

Current iteration: 5051
Current error: 0.450992722897

Current iteration: 5052
Current error: 0.00209511003537

Current iteration: 5053
Current error: 0.00202050189201

Current iteration: 5054
Current error: 0.001949570564

Current iteration: 5055
Current error: 0.00188245988066

Current iteration: 5056
Current error: 0.00181987763088

Current iteration: 5057
Current error: 0.00175778800755

Current iteration: 5058
Current error: 0.00169986136104

Current iteration: 5059
Current error: 0.00164511153182

Current iteration: 5060
Current error: 0.00159470496166

Current iteration: 5061
Current error: 0.00154236488133

Current iteration: 5062
Current error: 0.00149446477209

Current iteration: 5063
Current error: 0.00144903152222

Current iteration: 5064
Current error: 0.00140522927528

Current iteration: 5065
Current error: 0.448124754735

Current iteration: 5066
Current error: 0.00231613848836

Current iteration: 5067
Current error: 0.00226162784916

Current iteration: 5068
Current error: 0.00214752025655

Current iteration: 5069
Current error: 0.00207017282412

Current iteration: 5070
Current error: 0.00199711914622

Current iteration: 5071
Current error: 0.00192714232495

Current iteration: 5072
Current error: 0.00186104324109

Current iteration: 5073
Current error: 0.0018134848869

Current iteration: 5074
Current error: 0.00174106449627

Current iteration: 5075
Current error: 0.00168149109136

Current iteration: 5076
Current error: 0.00162743011036

Current iteration: 5077
Current error: 0.00157690907792

Current iteration: 5078
Current error: 0.00152824084073

Current iteration: 5079
Current error: 0.001479248185

Current iteration: 5080
Current error: 0.447260001746

Current iteration: 5081
Current error: 0.00243651634118

Current iteration: 5082
Current error: 0.00234330182742

Current iteration: 5083
Current error: 0.0022698864218

Current iteration: 5084
Current error: 0.00217997028466

Current iteration: 5085
Current error: 0.00209358229831

Current iteration: 5086
Current error: 0.00202231125846

Current iteration: 5087
Current error: 0.0019477005092

Current iteration: 5088
Current error: 0.440550287403

Current iteration: 5089
Current error: 0.00317611802397

Current iteration: 5090
Current error: 0.0030372403959

Current iteration: 5091
Current error: 0.00291009809118

Current iteration: 5092
Current error: 0.00278843238331

Current iteration: 5093
Current error: 0.00267580326027

Current iteration: 5094
Current error: 0.00260693729911

Current iteration: 5095
Current error: 0.00246780207277

Current iteration: 5096
Current error: 0.00237312029776

Current iteration: 5097
Current error: 0.434502402143

Current iteration: 5098
Current error: 0.00382100698803

Current iteration: 5099
Current error: 0.00364254429713

Current iteration: 5100
Current error: 0.419386214561

Current iteration: 5101
Current error: 0.00570030346213

Current iteration: 5102
Current error: 0.00538744230844

Current iteration: 5103
Current error: 0.00511576913575

Current iteration: 5104
Current error: 0.00482143718169

Current iteration: 5105
Current error: 0.00457458012338

Current iteration: 5106
Current error: 0.00435529021315

Current iteration: 5107
Current error: 0.00412689366996

Current iteration: 5108
Current error: 0.00392826132857

Current iteration: 5109
Current error: 0.00374169915759

Current iteration: 5110
Current error: 0.00356838430845

Current iteration: 5111
Current error: 0.00340725620225

Current iteration: 5112
Current error: 0.00325562163679

Current iteration: 5113
Current error: 0.00311408769545

Current iteration: 5114
Current error: 0.425222847391

Current iteration: 5115
Current error: 0.00492601576941

Current iteration: 5116
Current error: 0.00467118204523

Current iteration: 5117
Current error: 0.00443099698317

Current iteration: 5118
Current error: 0.00426487115869

Current iteration: 5119
Current error: 0.00400459278132

Current iteration: 5120
Current error: 0.416038068082

Current iteration: 5121
Current error: 0.00623035700275

Current iteration: 5122
Current error: 0.0058702267453

Current iteration: 5123
Current error: 0.0055408096766

Current iteration: 5124
Current error: 0.00523600798226

Current iteration: 5125
Current error: 0.00495633286967

Current iteration: 5126
Current error: 0.00469958342668

Current iteration: 5127
Current error: 0.00445633179358

Current iteration: 5128
Current error: 0.00423362935402

Current iteration: 5129
Current error: 0.413242389181

Current iteration: 5130
Current error: 0.00654793464765

Current iteration: 5131
Current error: 0.00616208790761

Current iteration: 5132
Current error: 0.00581354916482

Current iteration: 5133
Current error: 0.00548307393264

Current iteration: 5134
Current error: 0.00518385993698

Current iteration: 5135
Current error: 0.00490726696689

Current iteration: 5136
Current error: 0.00465162009336

Current iteration: 5137
Current error: 0.00441488900351

Current iteration: 5138
Current error: 0.00419546070295

Current iteration: 5139
Current error: 0.00399083951826

Current iteration: 5140
Current error: 0.00380099563995

Current iteration: 5141
Current error: 0.00362409847283

Current iteration: 5142
Current error: 0.00345840436299

Current iteration: 5143
Current error: 0.00330454654454

Current iteration: 5144
Current error: 0.00316038166784

Current iteration: 5145
Current error: 0.00302688997865

Current iteration: 5146
Current error: 0.00289664521119

Current iteration: 5147
Current error: 0.00277685864303

Current iteration: 5148
Current error: 0.00266443589963

Current iteration: 5149
Current error: 0.00255829844041

Current iteration: 5150
Current error: 0.00245925536469

Current iteration: 5151
Current error: 0.00236475713219

Current iteration: 5152
Current error: 0.00229166126506

Current iteration: 5153
Current error: 0.00219123212473

Current iteration: 5154
Current error: 0.00211152139439

Current iteration: 5155
Current error: 0.438105031282

Current iteration: 5156
Current error: 0.00342275172685

Current iteration: 5157
Current error: 0.00327184153409

Current iteration: 5158
Current error: 0.00313147467465

Current iteration: 5159
Current error: 0.00299406393939

Current iteration: 5160
Current error: 0.00287336123989

Current iteration: 5161
Current error: 0.00275103679568

Current iteration: 5162
Current error: 0.0026395912343

Current iteration: 5163
Current error: 0.00253532726382

Current iteration: 5164
Current error: 0.00243667535003

Current iteration: 5165
Current error: 0.00234431613078

Current iteration: 5166
Current error: 0.00225576141852

Current iteration: 5167
Current error: 0.436107855917

Current iteration: 5168
Current error: 0.00364379153035

Current iteration: 5169
Current error: 0.00347727242937

Current iteration: 5170
Current error: 0.4215975326

Current iteration: 5171
Current error: 0.00547073959271

Current iteration: 5172
Current error: 0.403496771258

Current iteration: 5173
Current error: 0.00831791013906

Current iteration: 5174
Current error: 0.0077766925127

Current iteration: 5175
Current error: 0.00728399152841

Current iteration: 5176
Current error: 0.00683609179513

Current iteration: 5177
Current error: 0.00642584564941

Current iteration: 5178
Current error: 0.00605760816476

Current iteration: 5179
Current error: 0.00570512727615

Current iteration: 5180
Current error: 0.00538871566929

Current iteration: 5181
Current error: 0.00509597415726

Current iteration: 5182
Current error: 0.0048261758946

Current iteration: 5183
Current error: 0.00457639371208

Current iteration: 5184
Current error: 0.00434532355518

Current iteration: 5185
Current error: 0.00413064173655

Current iteration: 5186
Current error: 0.00393122891965

Current iteration: 5187
Current error: 0.00374490396468

Current iteration: 5188
Current error: 0.00357155830989

Current iteration: 5189
Current error: 0.00340960075661

Current iteration: 5190
Current error: 0.00325854527323

Current iteration: 5191
Current error: 0.00311655824701

Current iteration: 5192
Current error: 0.00298562466196

Current iteration: 5193
Current error: 0.00285892238186

Current iteration: 5194
Current error: 0.00274168913995

Current iteration: 5195
Current error: 0.00263091399401

Current iteration: 5196
Current error: 0.00252685537862

Current iteration: 5197
Current error: 0.00242917446337

Current iteration: 5198
Current error: 0.0023366808537

Current iteration: 5199
Current error: 0.0022485402935

Current iteration: 5200
Current error: 0.00216613609558

Current iteration: 5201
Current error: 0.00208735538028

Current iteration: 5202
Current error: 0.00201523465013

Current iteration: 5203
Current error: 0.0019434479473

Current iteration: 5204
Current error: 0.43984286866

Current iteration: 5205
Current error: 0.00315529739451

Current iteration: 5206
Current error: 0.00301977998891

Current iteration: 5207
Current error: 0.00289304161028

Current iteration: 5208
Current error: 0.00277338109031

Current iteration: 5209
Current error: 0.00266396900051

Current iteration: 5210
Current error: 0.00255539510889

Current iteration: 5211
Current error: 0.0024558795665

Current iteration: 5212
Current error: 0.00236145325569

Current iteration: 5213
Current error: 0.00227300634878

Current iteration: 5214
Current error: 0.00219779356935

Current iteration: 5215
Current error: 0.00210880027687

Current iteration: 5216
Current error: 0.00203351019182

Current iteration: 5217
Current error: 0.00196201493233

Current iteration: 5218
Current error: 0.440242945652

Current iteration: 5219
Current error: 0.0031936360479

Current iteration: 5220
Current error: 0.00305685857397

Current iteration: 5221
Current error: 0.00294150040818

Current iteration: 5222
Current error: 0.0028051144952

Current iteration: 5223
Current error: 0.00269510488232

Current iteration: 5224
Current error: 0.00258333209943

Current iteration: 5225
Current error: 0.00248339496677

Current iteration: 5226
Current error: 0.00238648563516

Current iteration: 5227
Current error: 0.00229609671403

Current iteration: 5228
Current error: 0.00221105019042

Current iteration: 5229
Current error: 0.00213086157953

Current iteration: 5230
Current error: 0.00205504495734

Current iteration: 5231
Current error: 0.00198084489921

Current iteration: 5232
Current error: 0.00192320272296

Current iteration: 5233
Current error: 0.00184680197857

Current iteration: 5234
Current error: 0.00178515451544

Current iteration: 5235
Current error: 0.00172525465758

Current iteration: 5236
Current error: 0.00166966145541

Current iteration: 5237
Current error: 0.001615342208

Current iteration: 5238
Current error: 0.00156435692305

Current iteration: 5239
Current error: 0.00152953510509

Current iteration: 5240
Current error: 0.00146879604757

Current iteration: 5241
Current error: 0.0014244344982

Current iteration: 5242
Current error: 0.00139700233367

Current iteration: 5243
Current error: 0.00134103951631

Current iteration: 5244
Current error: 0.00130215719656

Current iteration: 5245
Current error: 0.00126494159811

Current iteration: 5246
Current error: 0.001229135468

Current iteration: 5247
Current error: 0.00119524600258

Current iteration: 5248
Current error: 0.00116210901426

Current iteration: 5249
Current error: 0.00113040430077

Current iteration: 5250
Current error: 0.00110024908618

Current iteration: 5251
Current error: 0.00109175257741

Current iteration: 5252
Current error: 0.00104309791201

Current iteration: 5253
Current error: 0.0010160369205

Current iteration: 5254
Current error: 0.000990159535754

Current iteration: 5255
Current error: 0.000965239111884

Current iteration: 5256
Current error: 0.000941150964512

Current iteration: 5257
Current error: 0.000918130766791

Current iteration: 5258
Current error: 0.00089569429634

Current iteration: 5259
Current error: 0.000885370760722

Current iteration: 5260
Current error: 0.000853281355708

Current iteration: 5261
Current error: 0.000847685474667

Current iteration: 5262
Current error: 0.000813889697402

Current iteration: 5263
Current error: 0.000797640194241

Current iteration: 5264
Current error: 0.000777160602239

Current iteration: 5265
Current error: 0.000759635115093

Current iteration: 5266
Current error: 0.00074275722087

Current iteration: 5267
Current error: 0.000726543451312

Current iteration: 5268
Current error: 0.000713177621464

Current iteration: 5269
Current error: 0.000695321291955

Current iteration: 5270
Current error: 0.000680482222831

Current iteration: 5271
Current error: 0.000666120865677

Current iteration: 5272
Current error: 0.000652730212496

Current iteration: 5273
Current error: 0.000638773619935

Current iteration: 5274
Current error: 0.00062566970357

Current iteration: 5275
Current error: 0.000613013639869

Current iteration: 5276
Current error: 0.000601570637451

Current iteration: 5277
Current error: 0.000588791257518

Current iteration: 5278
Current error: 0.000577162952689

Current iteration: 5279
Current error: 0.000565913282249

Current iteration: 5280
Current error: 0.000555053033748

Current iteration: 5281
Current error: 0.00054436485807

Current iteration: 5282
Current error: 0.000534199077937

Current iteration: 5283
Current error: 0.000524183022931

Current iteration: 5284
Current error: 0.000514250216743

Current iteration: 5285
Current error: 0.000504976053948

Current iteration: 5286
Current error: 0.468618142808

Current iteration: 5287
Current error: 0.000865307988129

Current iteration: 5288
Current error: 0.000844982558227

Current iteration: 5289
Current error: 0.45984724529

Current iteration: 5290
Current error: 0.00142893070685

Current iteration: 5291
Current error: 0.00138269621122

Current iteration: 5292
Current error: 0.0013418979369

Current iteration: 5293
Current error: 0.0013030351341

Current iteration: 5294
Current error: 0.00126579803793

Current iteration: 5295
Current error: 0.00123002560998

Current iteration: 5296
Current error: 0.00119568172954

Current iteration: 5297
Current error: 0.00116280314329

Current iteration: 5298
Current error: 0.00114217482587

Current iteration: 5299
Current error: 0.00110073280069

Current iteration: 5300
Current error: 0.00107204163779

Current iteration: 5301
Current error: 0.00104502849731

Current iteration: 5302
Current error: 0.00101660726114

Current iteration: 5303
Current error: 0.000991010969216

Current iteration: 5304
Current error: 0.00096574153689

Current iteration: 5305
Current error: 0.000941793504974

Current iteration: 5306
Current error: 0.000918556200271

Current iteration: 5307
Current error: 0.000899166575338

Current iteration: 5308
Current error: 0.000874778583141

Current iteration: 5309
Current error: 0.000853931105256

Current iteration: 5310
Current error: 0.00083634330796

Current iteration: 5311
Current error: 0.00081452663378

Current iteration: 5312
Current error: 0.000795738929387

Current iteration: 5313
Current error: 0.461156731004

Current iteration: 5314
Current error: 0.00134659933686

Current iteration: 5315
Current error: 0.00130793636231

Current iteration: 5316
Current error: 0.450030865444

Current iteration: 5317
Current error: 0.00216352997048

Current iteration: 5318
Current error: 0.00208521442557

Current iteration: 5319
Current error: 0.00201123748858

Current iteration: 5320
Current error: 0.00194075301373

Current iteration: 5321
Current error: 0.00190363989964

Current iteration: 5322
Current error: 0.00181000393265

Current iteration: 5323
Current error: 0.00177972222205

Current iteration: 5324
Current error: 0.00169196286972

Current iteration: 5325
Current error: 0.00163723730875

Current iteration: 5326
Current error: 0.00158510323997

Current iteration: 5327
Current error: 0.0015387861065

Current iteration: 5328
Current error: 0.0014879434506

Current iteration: 5329
Current error: 0.00144277350802

Current iteration: 5330
Current error: 0.00139942042092

Current iteration: 5331
Current error: 0.00135913803577

Current iteration: 5332
Current error: 0.449012331778

Current iteration: 5333
Current error: 0.00224753371126

Current iteration: 5334
Current error: 0.00215982847476

Current iteration: 5335
Current error: 0.00208144990209

Current iteration: 5336
Current error: 0.00200741244301

Current iteration: 5337
Current error: 0.00193724154112

Current iteration: 5338
Current error: 0.00187054648471

Current iteration: 5339
Current error: 0.00180718629043

Current iteration: 5340
Current error: 0.00174738500266

Current iteration: 5341
Current error: 0.0016896739652

Current iteration: 5342
Current error: 0.001635106285

Current iteration: 5343
Current error: 0.00158316301617

Current iteration: 5344
Current error: 0.00153348007828

Current iteration: 5345
Current error: 0.445802663522

Current iteration: 5346
Current error: 0.00251619180445

Current iteration: 5347
Current error: 0.00241868198713

Current iteration: 5348
Current error: 0.00232658427906

Current iteration: 5349
Current error: 0.00223952984914

Current iteration: 5350
Current error: 0.00215721715859

Current iteration: 5351
Current error: 0.00207925557419

Current iteration: 5352
Current error: 0.0020055678192

Current iteration: 5353
Current error: 0.0019353316909

Current iteration: 5354
Current error: 0.00187008366182

Current iteration: 5355
Current error: 0.00180558492258

Current iteration: 5356
Current error: 0.00174537191718

Current iteration: 5357
Current error: 0.00168864454329

Current iteration: 5358
Current error: 0.00163355953232

Current iteration: 5359
Current error: 0.00158198693102

Current iteration: 5360
Current error: 0.00153215935107

Current iteration: 5361
Current error: 0.00148479987498

Current iteration: 5362
Current error: 0.447327867167

Current iteration: 5363
Current error: 0.00244949217873

Current iteration: 5364
Current error: 0.00235357268832

Current iteration: 5365
Current error: 0.00226523974457

Current iteration: 5366
Current error: 0.00218103939106

Current iteration: 5367
Current error: 0.00210176237059

Current iteration: 5368
Current error: 0.00202756063667

Current iteration: 5369
Current error: 0.0019557399826

Current iteration: 5370
Current error: 0.00189625136015

Current iteration: 5371
Current error: 0.00182413359085

Current iteration: 5372
Current error: 0.00176273428056

Current iteration: 5373
Current error: 0.00170457764129

Current iteration: 5374
Current error: 0.00165030573731

Current iteration: 5375
Current error: 0.0015966812391

Current iteration: 5376
Current error: 0.00154644125215

Current iteration: 5377
Current error: 0.00149838777496

Current iteration: 5378
Current error: 0.0014526267951

Current iteration: 5379
Current error: 0.001421850035

Current iteration: 5380
Current error: 0.00136696861785

Current iteration: 5381
Current error: 0.00132688167455

Current iteration: 5382
Current error: 0.00128944324348

Current iteration: 5383
Current error: 0.00127004419174

Current iteration: 5384
Current error: 0.00121649880763

Current iteration: 5385
Current error: 0.00118295252336

Current iteration: 5386
Current error: 0.00115046456713

Current iteration: 5387
Current error: 0.00111942960421

Current iteration: 5388
Current error: 0.00108967919642

Current iteration: 5389
Current error: 0.00106079628354

Current iteration: 5390
Current error: 0.00103328766792

Current iteration: 5391
Current error: 0.0010071576604

Current iteration: 5392
Current error: 0.000981079914626

Current iteration: 5393
Current error: 0.000957381099562

Current iteration: 5394
Current error: 0.000932801165784

Current iteration: 5395
Current error: 0.000910027841278

Current iteration: 5396
Current error: 0.000887937331873

Current iteration: 5397
Current error: 0.000866634952054

Current iteration: 5398
Current error: 0.000847084638667

Current iteration: 5399
Current error: 0.000826468626039

Current iteration: 5400
Current error: 0.000807282170137

Current iteration: 5401
Current error: 0.000788822258478

Current iteration: 5402
Current error: 0.000771178950533

Current iteration: 5403
Current error: 0.00075379590993

Current iteration: 5404
Current error: 0.000737299168501

Current iteration: 5405
Current error: 0.462387766235

Current iteration: 5406
Current error: 0.00124945297755

Current iteration: 5407
Current error: 0.451865350016

Current iteration: 5408
Current error: 0.00207844361673

Current iteration: 5409
Current error: 0.00202046013604

Current iteration: 5410
Current error: 0.00193551273771

Current iteration: 5411
Current error: 0.00187442752417

Current iteration: 5412
Current error: 0.00182201499736

Current iteration: 5413
Current error: 0.00174428455396

Current iteration: 5414
Current error: 0.00168820380803

Current iteration: 5415
Current error: 0.00163282848787

Current iteration: 5416
Current error: 0.00158823257541

Current iteration: 5417
Current error: 0.00153120891408

Current iteration: 5418
Current error: 0.00149272290228

Current iteration: 5419
Current error: 0.00143871837732

Current iteration: 5420
Current error: 0.00141775702116

Current iteration: 5421
Current error: 0.00135413638635

Current iteration: 5422
Current error: 0.00131451955077

Current iteration: 5423
Current error: 0.00127871980011

Current iteration: 5424
Current error: 0.00124173302432

Current iteration: 5425
Current error: 0.00121760272338

Current iteration: 5426
Current error: 0.00119186906065

Current iteration: 5427
Current error: 0.00114027168589

Current iteration: 5428
Current error: 0.00111027581441

Current iteration: 5429
Current error: 0.00108002030364

Current iteration: 5430
Current error: 0.00105167834573

Current iteration: 5431
Current error: 0.00103278220682

Current iteration: 5432
Current error: 0.000998191308372

Current iteration: 5433
Current error: 0.000973208284245

Current iteration: 5434
Current error: 0.000949796880143

Current iteration: 5435
Current error: 0.000925255113189

Current iteration: 5436
Current error: 0.000902752762286

Current iteration: 5437
Current error: 0.000881114344654

Current iteration: 5438
Current error: 0.000859859819119

Current iteration: 5439
Current error: 0.000839653072592

Current iteration: 5440
Current error: 0.000823091315099

Current iteration: 5441
Current error: 0.000801182583684

Current iteration: 5442
Current error: 0.000782987869478

Current iteration: 5443
Current error: 0.000765511378525

Current iteration: 5444
Current error: 0.000748631638693

Current iteration: 5445
Current error: 0.000731711067325

Current iteration: 5446
Current error: 0.000718486102441

Current iteration: 5447
Current error: 0.000700217124909

Current iteration: 5448
Current error: 0.00068528903712

Current iteration: 5449
Current error: 0.000670826529957

Current iteration: 5450
Current error: 0.000656790825446

Current iteration: 5451
Current error: 0.000643383455985

Current iteration: 5452
Current error: 0.000630417577214

Current iteration: 5453
Current error: 0.000621914013966

Current iteration: 5454
Current error: 0.000604766204232

Current iteration: 5455
Current error: 0.000592580937915

Current iteration: 5456
Current error: 0.000581156003041

Current iteration: 5457
Current error: 0.000569519348574

Current iteration: 5458
Current error: 0.000558531883364

Current iteration: 5459
Current error: 0.000549029103915

Current iteration: 5460
Current error: 0.000537408223933

Current iteration: 5461
Current error: 0.000527231061045

Current iteration: 5462
Current error: 0.000517362885456

Current iteration: 5463
Current error: 0.000508076748954

Current iteration: 5464
Current error: 0.000498511280382

Current iteration: 5465
Current error: 0.000489473140872

Current iteration: 5466
Current error: 0.000482049511711

Current iteration: 5467
Current error: 0.000472142303189

Current iteration: 5468
Current error: 0.000464862821738

Current iteration: 5469
Current error: 0.000455780805965

Current iteration: 5470
Current error: 0.000450142980244

Current iteration: 5471
Current error: 0.000439819259807

Current iteration: 5472
Current error: 0.470378788982

Current iteration: 5473
Current error: 0.000755606421942

Current iteration: 5474
Current error: 0.00073897612621

Current iteration: 5475
Current error: 0.000722948015158

Current iteration: 5476
Current error: 0.000707305360697

Current iteration: 5477
Current error: 0.000691757088436

Current iteration: 5478
Current error: 0.000677062664919

Current iteration: 5479
Current error: 0.000662809071076

Current iteration: 5480
Current error: 0.000649011749556

Current iteration: 5481
Current error: 0.000636849903054

Current iteration: 5482
Current error: 0.000622692446946

Current iteration: 5483
Current error: 0.000610048688213

Current iteration: 5484
Current error: 0.000597864004246

Current iteration: 5485
Current error: 0.000586121198482

Current iteration: 5486
Current error: 0.000575165597191

Current iteration: 5487
Current error: 0.000563399294665

Current iteration: 5488
Current error: 0.000552488906883

Current iteration: 5489
Current error: 0.000541897362405

Current iteration: 5490
Current error: 0.000531675910765

Current iteration: 5491
Current error: 0.000522062673547

Current iteration: 5492
Current error: 0.000517944878344

Current iteration: 5493
Current error: 0.000502555257976

Current iteration: 5494
Current error: 0.000493390585632

Current iteration: 5495
Current error: 0.000484414373657

Current iteration: 5496
Current error: 0.469013846055

Current iteration: 5497
Current error: 0.000830342775547

Current iteration: 5498
Current error: 0.000811090010274

Current iteration: 5499
Current error: 0.000792518788163

Current iteration: 5500
Current error: 0.000774607548834

Current iteration: 5501
Current error: 0.000757168106912

Current iteration: 5502
Current error: 0.000740393650824

Current iteration: 5503
Current error: 0.000737588159866

Current iteration: 5504
Current error: 0.000708658906958

Current iteration: 5505
Current error: 0.000708019010976

Current iteration: 5506
Current error: 0.000678220230898

Current iteration: 5507
Current error: 0.000664596746546

Current iteration: 5508
Current error: 0.000650525309799

Current iteration: 5509
Current error: 0.000636713427028

Current iteration: 5510
Current error: 0.00062368457186

Current iteration: 5511
Current error: 0.000611319799952

Current iteration: 5512
Current error: 0.000598791538161

Current iteration: 5513
Current error: 0.00058695066919

Current iteration: 5514
Current error: 0.000575424249451

Current iteration: 5515
Current error: 0.000564762773947

Current iteration: 5516
Current error: 0.000553737881812

Current iteration: 5517
Current error: 0.00054284381452

Current iteration: 5518
Current error: 0.000532827233161

Current iteration: 5519
Current error: 0.000522487641079

Current iteration: 5520
Current error: 0.000512838427355

Current iteration: 5521
Current error: 0.000503543135875

Current iteration: 5522
Current error: 0.000494146472155

Current iteration: 5523
Current error: 0.000485438893943

Current iteration: 5524
Current error: 0.000482042733185

Current iteration: 5525
Current error: 0.00046816561069

Current iteration: 5526
Current error: 0.000459778530342

Current iteration: 5527
Current error: 0.000451634411282

Current iteration: 5528
Current error: 0.000443807913209

Current iteration: 5529
Current error: 0.00043635769333

Current iteration: 5530
Current error: 0.0004287784405

Current iteration: 5531
Current error: 0.000422092028824

Current iteration: 5532
Current error: 0.000414676497243

Current iteration: 5533
Current error: 0.000412784029172

Current iteration: 5534
Current error: 0.000400897312438

Current iteration: 5535
Current error: 0.000394911755521

Current iteration: 5536
Current error: 0.472178332086

Current iteration: 5537
Current error: 0.000680575784905

Current iteration: 5538
Current error: 0.000676391623328

Current iteration: 5539
Current error: 0.000652032144781

Current iteration: 5540
Current error: 0.000638596375289

Current iteration: 5541
Current error: 0.000625731316764

Current iteration: 5542
Current error: 0.000612845733152

Current iteration: 5543
Current error: 0.000605534002963

Current iteration: 5544
Current error: 0.000588549943908

Current iteration: 5545
Current error: 0.000577052822604

Current iteration: 5546
Current error: 0.000565765601198

Current iteration: 5547
Current error: 0.000565596382675

Current iteration: 5548
Current error: 0.467098518098

Current iteration: 5549
Current error: 0.456836535809

Current iteration: 5550
Current error: 0.00163054748796

Current iteration: 5551
Current error: 0.00157867104377

Current iteration: 5552
Current error: 0.00152929427359

Current iteration: 5553
Current error: 0.00148211233044

Current iteration: 5554
Current error: 0.00143699836068

Current iteration: 5555
Current error: 0.0013939242925

Current iteration: 5556
Current error: 0.00135317881647

Current iteration: 5557
Current error: 0.00131357610912

Current iteration: 5558
Current error: 0.450327435585

Current iteration: 5559
Current error: 0.00217701298792

Current iteration: 5560
Current error: 0.00209767511838

Current iteration: 5561
Current error: 0.00202423927041

Current iteration: 5562
Current error: 0.00195231865761

Current iteration: 5563
Current error: 0.00188471356847

Current iteration: 5564
Current error: 0.00182485571891

Current iteration: 5565
Current error: 0.0017596397299

Current iteration: 5566
Current error: 0.00170170116791

Current iteration: 5567
Current error: 0.00164760428776

Current iteration: 5568
Current error: 0.00163735509662

Current iteration: 5569
Current error: 0.00154367432216

Current iteration: 5570
Current error: 0.0014956014361

Current iteration: 5571
Current error: 0.00144990603713

Current iteration: 5572
Current error: 0.00140621255273

Current iteration: 5573
Current error: 0.00136506756658

Current iteration: 5574
Current error: 0.00133017566926

Current iteration: 5575
Current error: 0.00128632208111

Current iteration: 5576
Current error: 0.00124967691648

Current iteration: 5577
Current error: 0.00121460209148

Current iteration: 5578
Current error: 0.00118943563194

Current iteration: 5579
Current error: 0.00114867140666

Current iteration: 5580
Current error: 0.00111966992397

Current iteration: 5581
Current error: 0.0011074640187

Current iteration: 5582
Current error: 0.00105897101065

Current iteration: 5583
Current error: 0.001031686346

Current iteration: 5584
Current error: 0.0010050071654

Current iteration: 5585
Current error: 0.000979550244912

Current iteration: 5586
Current error: 0.000954920742803

Current iteration: 5587
Current error: 0.00094227889514

Current iteration: 5588
Current error: 0.000908901520912

Current iteration: 5589
Current error: 0.00088644509155

Current iteration: 5590
Current error: 0.000865424919718

Current iteration: 5591
Current error: 0.00084482003594

Current iteration: 5592
Current error: 0.000825175166883

Current iteration: 5593
Current error: 0.000808245047477

Current iteration: 5594
Current error: 0.460215985257

Current iteration: 5595
Current error: 0.00135829037393

Current iteration: 5596
Current error: 0.00131944108618

Current iteration: 5597
Current error: 0.00128067350978

Current iteration: 5598
Current error: 0.0012454160053

Current iteration: 5599
Current error: 0.00120941597404

Current iteration: 5600
Current error: 0.00117628168171

Current iteration: 5601
Current error: 0.00114377177481

Current iteration: 5602
Current error: 0.00111300486579

Current iteration: 5603
Current error: 0.00108360692122

Current iteration: 5604
Current error: 0.00105532296464

Current iteration: 5605
Current error: 0.00102791740849

Current iteration: 5606
Current error: 0.00100123784864

Current iteration: 5607
Current error: 0.00100728501042

Current iteration: 5608
Current error: 0.000951275487354

Current iteration: 5609
Current error: 0.000927709834685

Current iteration: 5610
Current error: 0.000905491668299

Current iteration: 5611
Current error: 0.000883210700909

Current iteration: 5612
Current error: 0.000862131971787

Current iteration: 5613
Current error: 0.000844272601975

Current iteration: 5614
Current error: 0.000822720109421

Current iteration: 5615
Current error: 0.00080328852299

Current iteration: 5616
Current error: 0.460510410457

Current iteration: 5617
Current error: 0.00135641080124

Current iteration: 5618
Current error: 0.00131585124686

Current iteration: 5619
Current error: 0.0012779893777

Current iteration: 5620
Current error: 0.00124180453038

Current iteration: 5621
Current error: 0.00120739836243

Current iteration: 5622
Current error: 0.00117368669034

Current iteration: 5623
Current error: 0.00114175009085

Current iteration: 5624
Current error: 0.00111082287672

Current iteration: 5625
Current error: 0.453070841712

Current iteration: 5626
Current error: 0.00184856489214

Current iteration: 5627
Current error: 0.00178475749272

Current iteration: 5628
Current error: 0.00175843362264

Current iteration: 5629
Current error: 0.00166837071965

Current iteration: 5630
Current error: 0.00161401357376

Current iteration: 5631
Current error: 0.00156480647713

Current iteration: 5632
Current error: 0.00151416539056

Current iteration: 5633
Current error: 0.00146779488582

Current iteration: 5634
Current error: 0.00142453320419

Current iteration: 5635
Current error: 0.00138086045558

Current iteration: 5636
Current error: 0.00134017524227

Current iteration: 5637
Current error: 0.00130137147181

Current iteration: 5638
Current error: 0.00126722188281

Current iteration: 5639
Current error: 0.00122843227982

Current iteration: 5640
Current error: 0.00119423228202

Current iteration: 5641
Current error: 0.452263264009

Current iteration: 5642
Current error: 0.00198462356413

Current iteration: 5643
Current error: 0.00192072412305

Current iteration: 5644
Current error: 0.00185046630793

Current iteration: 5645
Current error: 0.00178780117921

Current iteration: 5646
Current error: 0.00172848291939

Current iteration: 5647
Current error: 0.00167186308786

Current iteration: 5648
Current error: 0.00161822649061

Current iteration: 5649
Current error: 0.00156925771754

Current iteration: 5650
Current error: 0.00151809082399

Current iteration: 5651
Current error: 0.00147132262184

Current iteration: 5652
Current error: 0.001428967625

Current iteration: 5653
Current error: 0.00138413877625

Current iteration: 5654
Current error: 0.00134341906389

Current iteration: 5655
Current error: 0.00130435857319

Current iteration: 5656
Current error: 0.00126725581058

Current iteration: 5657
Current error: 0.00123114036221

Current iteration: 5658
Current error: 0.00119681132805

Current iteration: 5659
Current error: 0.00116399853478

Current iteration: 5660
Current error: 0.00114672756561

Current iteration: 5661
Current error: 0.00110170593715

Current iteration: 5662
Current error: 0.00107647626732

Current iteration: 5663
Current error: 0.00104916507421

Current iteration: 5664
Current error: 0.00101748307953

Current iteration: 5665
Current error: 0.000991597003702

Current iteration: 5666
Current error: 0.000966519284437

Current iteration: 5667
Current error: 0.456546503602

Current iteration: 5668
Current error: 0.00161858957951

Current iteration: 5669
Current error: 0.00156665908736

Current iteration: 5670
Current error: 0.00151779405341

Current iteration: 5671
Current error: 0.00147109891733

Current iteration: 5672
Current error: 0.00142661186352

Current iteration: 5673
Current error: 0.00138407061399

Current iteration: 5674
Current error: 0.00134315285654

Current iteration: 5675
Current error: 0.00130490555992

Current iteration: 5676
Current error: 0.00128647845932

Current iteration: 5677
Current error: 0.00123078715103

Current iteration: 5678
Current error: 0.451465347946

Current iteration: 5679
Current error: 0.437874207305

Current iteration: 5680
Current error: 0.00347251391122

Current iteration: 5681
Current error: 0.00327920886763

Current iteration: 5682
Current error: 0.00313545079051

Current iteration: 5683
Current error: 0.00300046274472

Current iteration: 5684
Current error: 0.00287863280547

Current iteration: 5685
Current error: 0.427034153999

Current iteration: 5686
Current error: 0.00455772400699

Current iteration: 5687
Current error: 0.00432650752878

Current iteration: 5688
Current error: 0.00411344052643

Current iteration: 5689
Current error: 0.00392332066067

Current iteration: 5690
Current error: 0.0037301098058

Current iteration: 5691
Current error: 0.00355766402503

Current iteration: 5692
Current error: 0.00339685203241

Current iteration: 5693
Current error: 0.00324600010146

Current iteration: 5694
Current error: 0.00310811102393

Current iteration: 5695
Current error: 0.00297281786688

Current iteration: 5696
Current error: 0.426009845271

Current iteration: 5697
Current error: 0.0047296053919

Current iteration: 5698
Current error: 0.00446259980514

Current iteration: 5699
Current error: 0.00429571474236

Current iteration: 5700
Current error: 0.00403153983093

Current iteration: 5701
Current error: 0.00384080395099

Current iteration: 5702
Current error: 0.00365920266073

Current iteration: 5703
Current error: 0.00349160307514

Current iteration: 5704
Current error: 0.00333507833522

Current iteration: 5705
Current error: 0.00318832065407

Current iteration: 5706
Current error: 0.00305067118147

Current iteration: 5707
Current error: 0.00292221740688

Current iteration: 5708
Current error: 0.00282703132563

Current iteration: 5709
Current error: 0.00268645483639

Current iteration: 5710
Current error: 0.42958258715

Current iteration: 5711
Current error: 0.408065403159

Current iteration: 5712
Current error: 0.00688257559279

Current iteration: 5713
Current error: 0.00646828443993

Current iteration: 5714
Current error: 0.00608921110779

Current iteration: 5715
Current error: 0.00574132435472

Current iteration: 5716
Current error: 0.00544800955907

Current iteration: 5717
Current error: 0.00512729002223

Current iteration: 5718
Current error: 0.00485479740513

Current iteration: 5719
Current error: 0.00460255587152

Current iteration: 5720
Current error: 0.00436941213414

Current iteration: 5721
Current error: 0.00415297897829

Current iteration: 5722
Current error: 0.00395178434555

Current iteration: 5723
Current error: 0.00376508000493

Current iteration: 5724
Current error: 0.00359131916202

Current iteration: 5725
Current error: 0.0034268527641

Current iteration: 5726
Current error: 0.00327526801955

Current iteration: 5727
Current error: 0.00313151985576

Current iteration: 5728
Current error: 0.00300059267846

Current iteration: 5729
Current error: 0.00287176157605

Current iteration: 5730
Current error: 0.00275369373052

Current iteration: 5731
Current error: 0.00264246349431

Current iteration: 5732
Current error: 0.00253801967961

Current iteration: 5733
Current error: 0.00243918005388

Current iteration: 5734
Current error: 0.432532261222

Current iteration: 5735
Current error: 0.00397040249045

Current iteration: 5736
Current error: 0.00372064364097

Current iteration: 5737
Current error: 0.00357765391652

Current iteration: 5738
Current error: 0.0033888006666

Current iteration: 5739
Current error: 0.00323789478054

Current iteration: 5740
Current error: 0.00309771933367

Current iteration: 5741
Current error: 0.00296585831964

Current iteration: 5742
Current error: 0.00284185050299

Current iteration: 5743
Current error: 0.00272565010494

Current iteration: 5744
Current error: 0.00261629942723

Current iteration: 5745
Current error: 0.00251305478182

Current iteration: 5746
Current error: 0.00242097500367

Current iteration: 5747
Current error: 0.0023237800585

Current iteration: 5748
Current error: 0.00223682079692

Current iteration: 5749
Current error: 0.00215806224495

Current iteration: 5750
Current error: 0.00207670885394

Current iteration: 5751
Current error: 0.00200307417627

Current iteration: 5752
Current error: 0.00193305303564

Current iteration: 5753
Current error: 0.00186998474174

Current iteration: 5754
Current error: 0.00180342355343

Current iteration: 5755
Current error: 0.00174338316946

Current iteration: 5756
Current error: 0.0016862354425

Current iteration: 5757
Current error: 0.00163520249008

Current iteration: 5758
Current error: 0.00158117891394

Current iteration: 5759
Current error: 0.00153043860917

Current iteration: 5760
Current error: 0.00148338696198

Current iteration: 5761
Current error: 0.00143823958501

Current iteration: 5762
Current error: 0.00139493655112

Current iteration: 5763
Current error: 0.00135378233907

Current iteration: 5764
Current error: 0.00131434851859

Current iteration: 5765
Current error: 0.00127655017431

Current iteration: 5766
Current error: 0.00124120071542

Current iteration: 5767
Current error: 0.00120554200146

Current iteration: 5768
Current error: 0.452168314671

Current iteration: 5769
Current error: 0.00200379129272

Current iteration: 5770
Current error: 0.00193404073871

Current iteration: 5771
Current error: 0.00186752332448

Current iteration: 5772
Current error: 0.0018042814594

Current iteration: 5773
Current error: 0.00174419618777

Current iteration: 5774
Current error: 0.441299990345

Current iteration: 5775
Current error: 0.00283222569472

Current iteration: 5776
Current error: 0.00271641882589

Current iteration: 5777
Current error: 0.00261496280184

Current iteration: 5778
Current error: 0.00250478188799

Current iteration: 5779
Current error: 0.00241062792985

Current iteration: 5780
Current error: 0.00231771883325

Current iteration: 5781
Current error: 0.00222977775821

Current iteration: 5782
Current error: 0.00214806381319

Current iteration: 5783
Current error: 0.00207055728748

Current iteration: 5784
Current error: 0.00199718075231

Current iteration: 5785
Current error: 0.0019278569186

Current iteration: 5786
Current error: 0.001861312092

Current iteration: 5787
Current error: 0.00179840981705

Current iteration: 5788
Current error: 0.00174038239658

Current iteration: 5789
Current error: 0.0016994849704

Current iteration: 5790
Current error: 0.00162742864909

Current iteration: 5791
Current error: 0.00157580945902

Current iteration: 5792
Current error: 0.00152636853019

Current iteration: 5793
Current error: 0.00147959812454

Current iteration: 5794
Current error: 0.00143456719486

Current iteration: 5795
Current error: 0.447626743046

Current iteration: 5796
Current error: 0.00236227350204

Current iteration: 5797
Current error: 0.00227330847068

Current iteration: 5798
Current error: 0.00218933876222

Current iteration: 5799
Current error: 0.00210958503323

Current iteration: 5800
Current error: 0.00203401598023

Current iteration: 5801
Current error: 0.00196250087266

Current iteration: 5802
Current error: 0.0019159347438

Current iteration: 5803
Current error: 0.00182982864601

Current iteration: 5804
Current error: 0.00176857260916

Current iteration: 5805
Current error: 0.00171018737328

Current iteration: 5806
Current error: 0.00167997548146

Current iteration: 5807
Current error: 0.00160137892139

Current iteration: 5808
Current error: 0.00156861534993

Current iteration: 5809
Current error: 0.00150261704698

Current iteration: 5810
Current error: 0.00145673018144

Current iteration: 5811
Current error: 0.00141285696406

Current iteration: 5812
Current error: 0.448475831619

Current iteration: 5813
Current error: 0.00233355140843

Current iteration: 5814
Current error: 0.00224554578839

Current iteration: 5815
Current error: 0.00216282891452

Current iteration: 5816
Current error: 0.00208463425774

Current iteration: 5817
Current error: 0.00201139502122

Current iteration: 5818
Current error: 0.00194936981951

Current iteration: 5819
Current error: 0.00187327699597

Current iteration: 5820
Current error: 0.0018096986933

Current iteration: 5821
Current error: 0.00174935257083

Current iteration: 5822
Current error: 0.00169244819846

Current iteration: 5823
Current error: 0.00163911263198

Current iteration: 5824
Current error: 0.00158579973895

Current iteration: 5825
Current error: 0.0015412725092

Current iteration: 5826
Current error: 0.446688433034

Current iteration: 5827
Current error: 0.00253476394683

Current iteration: 5828
Current error: 0.00243105991408

Current iteration: 5829
Current error: 0.00233765417496

Current iteration: 5830
Current error: 0.00225001380062

Current iteration: 5831
Current error: 0.00216720049497

Current iteration: 5832
Current error: 0.00209048198342

Current iteration: 5833
Current error: 0.00201462538728

Current iteration: 5834
Current error: 0.00194503005505

Current iteration: 5835
Current error: 0.00188215169001

Current iteration: 5836
Current error: 0.00181309140644

Current iteration: 5837
Current error: 0.00175259950185

Current iteration: 5838
Current error: 0.442992470046

Current iteration: 5839
Current error: 0.00286527432151

Current iteration: 5840
Current error: 0.00274778742844

Current iteration: 5841
Current error: 0.00263673210685

Current iteration: 5842
Current error: 0.00255844390791

Current iteration: 5843
Current error: 0.00243373410978

Current iteration: 5844
Current error: 0.00235418387625

Current iteration: 5845
Current error: 0.00225521403892

Current iteration: 5846
Current error: 0.00217156769845

Current iteration: 5847
Current error: 0.00209120271233

Current iteration: 5848
Current error: 0.437021699724

Current iteration: 5849
Current error: 0.00338548574305

Current iteration: 5850
Current error: 0.00322573134629

Current iteration: 5851
Current error: 0.00308626814054

Current iteration: 5852
Current error: 0.00295516651865

Current iteration: 5853
Current error: 0.00283212450798

Current iteration: 5854
Current error: 0.00271592874387

Current iteration: 5855
Current error: 0.00262342352756

Current iteration: 5856
Current error: 0.00250430848666

Current iteration: 5857
Current error: 0.00241295609822

Current iteration: 5858
Current error: 0.00231793807639

Current iteration: 5859
Current error: 0.00222968009282

Current iteration: 5860
Current error: 0.00214764029496

Current iteration: 5861
Current error: 0.00207021397097

Current iteration: 5862
Current error: 0.00199686543996

Current iteration: 5863
Current error: 0.00192711380544

Current iteration: 5864
Current error: 0.439981906029

Current iteration: 5865
Current error: 0.00313052227494

Current iteration: 5866
Current error: 0.00299898258397

Current iteration: 5867
Current error: 0.00287167850068

Current iteration: 5868
Current error: 0.00275292323616

Current iteration: 5869
Current error: 0.00264189572365

Current iteration: 5870
Current error: 0.00253713006321

Current iteration: 5871
Current error: 0.00243862091562

Current iteration: 5872
Current error: 0.00234669275468

Current iteration: 5873
Current error: 0.00225719590441

Current iteration: 5874
Current error: 0.00217401170852

Current iteration: 5875
Current error: 0.00210405650663

Current iteration: 5876
Current error: 0.00202038630665

Current iteration: 5877
Current error: 0.00194954350239

Current iteration: 5878
Current error: 0.00188225301628

Current iteration: 5879
Current error: 0.00181842629399

Current iteration: 5880
Current error: 0.0017575354904

Current iteration: 5881
Current error: 0.00169973127975

Current iteration: 5882
Current error: 0.00164652934809

Current iteration: 5883
Current error: 0.00159218364291

Current iteration: 5884
Current error: 0.00156697163204

Current iteration: 5885
Current error: 0.00149438660931

Current iteration: 5886
Current error: 0.00144873193723

Current iteration: 5887
Current error: 0.00140748258224

Current iteration: 5888
Current error: 0.00136830310707

Current iteration: 5889
Current error: 0.00132335657351

Current iteration: 5890
Current error: 0.00128513926004

Current iteration: 5891
Current error: 0.00124868761073

Current iteration: 5892
Current error: 0.00121435192518

Current iteration: 5893
Current error: 0.00118011870523

Current iteration: 5894
Current error: 0.00114770394015

Current iteration: 5895
Current error: 0.00111674926933

Current iteration: 5896
Current error: 0.0010872358

Current iteration: 5897
Current error: 0.00105846439463

Current iteration: 5898
Current error: 0.00103081633678

Current iteration: 5899
Current error: 0.0010043929093

Current iteration: 5900
Current error: 0.000979106076911

Current iteration: 5901
Current error: 0.000954691369156

Current iteration: 5902
Current error: 0.000930903360141

Current iteration: 5903
Current error: 0.00090805090138

Current iteration: 5904
Current error: 0.000886350384025

Current iteration: 5905
Current error: 0.000864946421052

Current iteration: 5906
Current error: 0.000844528565278

Current iteration: 5907
Current error: 0.000824705901585

Current iteration: 5908
Current error: 0.000805702068897

Current iteration: 5909
Current error: 0.000787356988981

Current iteration: 5910
Current error: 0.000769455218596

Current iteration: 5911
Current error: 0.000752289681185

Current iteration: 5912
Current error: 0.000735854137823

Current iteration: 5913
Current error: 0.00071996421668

Current iteration: 5914
Current error: 0.463024909841

Current iteration: 5915
Current error: 0.00122192263211

Current iteration: 5916
Current error: 0.00118786355649

Current iteration: 5917
Current error: 0.00115534624842

Current iteration: 5918
Current error: 0.00112447670806

Current iteration: 5919
Current error: 0.00109403160624

Current iteration: 5920
Current error: 0.0010650759577

Current iteration: 5921
Current error: 0.00104182571179

Current iteration: 5922
Current error: 0.00101058380587

Current iteration: 5923
Current error: 0.000985447027848

Current iteration: 5924
Current error: 0.000960591138102

Current iteration: 5925
Current error: 0.000936505538753

Current iteration: 5926
Current error: 0.00091331167561

Current iteration: 5927
Current error: 0.000891186205425

Current iteration: 5928
Current error: 0.45861102212

Current iteration: 5929
Current error: 0.00149914552007

Current iteration: 5930
Current error: 0.00148086630033

Current iteration: 5931
Current error: 0.00141636907885

Current iteration: 5932
Current error: 0.00141486749825

Current iteration: 5933
Current error: 0.00132688816695

Current iteration: 5934
Current error: 0.00128859889574

Current iteration: 5935
Current error: 0.00125223265293

Current iteration: 5936
Current error: 0.0012166266881

Current iteration: 5937
Current error: 0.00118292918334

Current iteration: 5938
Current error: 0.00115055143482

Current iteration: 5939
Current error: 0.00111943347817

Current iteration: 5940
Current error: 0.00108955943031

Current iteration: 5941
Current error: 0.00106100990497

Current iteration: 5942
Current error: 0.00103448217986

Current iteration: 5943
Current error: 0.454748335136

Current iteration: 5944
Current error: 0.00172218179372

Current iteration: 5945
Current error: 0.00166605702855

Current iteration: 5946
Current error: 0.00161254856896

Current iteration: 5947
Current error: 0.00156172262287

Current iteration: 5948
Current error: 0.0015129339853

Current iteration: 5949
Current error: 0.00146657335917

Current iteration: 5950
Current error: 0.00142824635985

Current iteration: 5951
Current error: 0.00140073117132

Current iteration: 5952
Current error: 0.00133892379867

Current iteration: 5953
Current error: 0.00130011185496

Current iteration: 5954
Current error: 0.00126321275451

Current iteration: 5955
Current error: 0.00122763200395

Current iteration: 5956
Current error: 0.00119535379311

Current iteration: 5957
Current error: 0.00116042407249

Current iteration: 5958
Current error: 0.001128810788

Current iteration: 5959
Current error: 0.00109849652253

Current iteration: 5960
Current error: 0.00106969843927

Current iteration: 5961
Current error: 0.00104156908833

Current iteration: 5962
Current error: 0.00102344791403

Current iteration: 5963
Current error: 0.000990236279404

Current iteration: 5964
Current error: 0.000963902227141

Current iteration: 5965
Current error: 0.000940368932679

Current iteration: 5966
Current error: 0.000918101010229

Current iteration: 5967
Current error: 0.000894654061249

Current iteration: 5968
Current error: 0.000880763138194

Current iteration: 5969
Current error: 0.000852336481509

Current iteration: 5970
Current error: 0.000832317232843

Current iteration: 5971
Current error: 0.000812937191889

Current iteration: 5972
Current error: 0.000800036532607

Current iteration: 5973
Current error: 0.000776252273454

Current iteration: 5974
Current error: 0.000759078752313

Current iteration: 5975
Current error: 0.0007419348912

Current iteration: 5976
Current error: 0.000725695031556

Current iteration: 5977
Current error: 0.000709960813374

Current iteration: 5978
Current error: 0.000695052804415

Current iteration: 5979
Current error: 0.000680012096543

Current iteration: 5980
Current error: 0.000665521386034

Current iteration: 5981
Current error: 0.000651635899866

Current iteration: 5982
Current error: 0.000640584975731

Current iteration: 5983
Current error: 0.000652223708705

Current iteration: 5984
Current error: 0.000612235287217

Current iteration: 5985
Current error: 0.000600588208891

Current iteration: 5986
Current error: 0.000588022919329

Current iteration: 5987
Current error: 0.000576531819838

Current iteration: 5988
Current error: 0.000565282030109

Current iteration: 5989
Current error: 0.000554918894433

Current iteration: 5990
Current error: 0.000543744547619

Current iteration: 5991
Current error: 0.000533832421394

Current iteration: 5992
Current error: 0.000523456291624

Current iteration: 5993
Current error: 0.00051365575181

Current iteration: 5994
Current error: 0.000504273180722

Current iteration: 5995
Current error: 0.000498568466076

Current iteration: 5996
Current error: 0.000486812796368

Current iteration: 5997
Current error: 0.000477316445159

Current iteration: 5998
Current error: 0.000468721670123

Current iteration: 5999
Current error: 0.000460687514139

Current iteration: 6000
Current error: 0.000464854483611

Current iteration: 6001
Current error: 0.00044453647922

Current iteration: 6002
Current error: 0.000437265778986

Current iteration: 6003
Current error: 0.000430893156484

Current iteration: 6004
Current error: 0.000429408905444

Current iteration: 6005
Current error: 0.000414983679633

Current iteration: 6006
Current error: 0.00040874149989

Current iteration: 6007
Current error: 0.00040157137508

Current iteration: 6008
Current error: 0.000394755596678

Current iteration: 6009
Current error: 0.00038842197523

Current iteration: 6010
Current error: 0.472241063827

Current iteration: 6011
Current error: 0.00066996042657

Current iteration: 6012
Current error: 0.000655910168279

Current iteration: 6013
Current error: 0.000643515961797

Current iteration: 6014
Current error: 0.000629151087544

Current iteration: 6015
Current error: 0.463973727065

Current iteration: 6016
Current error: 0.00106599160125

Current iteration: 6017
Current error: 0.00104017719311

Current iteration: 6018
Current error: 0.00101093776694

Current iteration: 6019
Current error: 0.000985143273669

Current iteration: 6020
Current error: 0.000960370576353

Current iteration: 6021
Current error: 0.000936750346233

Current iteration: 6022
Current error: 0.000913661208489

Current iteration: 6023
Current error: 0.000891398688983

Current iteration: 6024
Current error: 0.000870067267429

Current iteration: 6025
Current error: 0.000849642759264

Current iteration: 6026
Current error: 0.000829617597863

Current iteration: 6027
Current error: 0.000810350978609

Current iteration: 6028
Current error: 0.000791798043074

Current iteration: 6029
Current error: 0.000773822756093

Current iteration: 6030
Current error: 0.000756499416215

Current iteration: 6031
Current error: 0.000739784134596

Current iteration: 6032
Current error: 0.000723465452845

Current iteration: 6033
Current error: 0.000707747498283

Current iteration: 6034
Current error: 0.000692546158431

Current iteration: 6035
Current error: 0.000678770147621

Current iteration: 6036
Current error: 0.000663560364547

Current iteration: 6037
Current error: 0.000652454971654

Current iteration: 6038
Current error: 0.000636347566462

Current iteration: 6039
Current error: 0.000623293980231

Current iteration: 6040
Current error: 0.000616271114986

Current iteration: 6041
Current error: 0.000598804973315

Current iteration: 6042
Current error: 0.000586535770718

Current iteration: 6043
Current error: 0.000575335387401

Current iteration: 6044
Current error: 0.000563838886554

Current iteration: 6045
Current error: 0.000553286197202

Current iteration: 6046
Current error: 0.000542413253394

Current iteration: 6047
Current error: 0.00053212294151

Current iteration: 6048
Current error: 0.467487898125

Current iteration: 6049
Current error: 0.00090919733223

Current iteration: 6050
Current error: 0.000887268154936

Current iteration: 6051
Current error: 0.000866020338563

Current iteration: 6052
Current error: 0.00084555650441

Current iteration: 6053
Current error: 0.000825935599643

Current iteration: 6054
Current error: 0.000806720634308

Current iteration: 6055
Current error: 0.000802186393457

Current iteration: 6056
Current error: 0.000770473089424

Current iteration: 6057
Current error: 0.00075321711667

Current iteration: 6058
Current error: 0.000736607675957

Current iteration: 6059
Current error: 0.000720509377119

Current iteration: 6060
Current error: 0.000704716795346

Current iteration: 6061
Current error: 0.000689562496281

Current iteration: 6062
Current error: 0.000674978785975

Current iteration: 6063
Current error: 0.000660806072017

Current iteration: 6064
Current error: 0.000647002839913

Current iteration: 6065
Current error: 0.00063370467325

Current iteration: 6066
Current error: 0.000620792579121

Current iteration: 6067
Current error: 0.000608238925588

Current iteration: 6068
Current error: 0.00059608745652

Current iteration: 6069
Current error: 0.000584424535594

Current iteration: 6070
Current error: 0.000572883738258

Current iteration: 6071
Current error: 0.000561708595621

Current iteration: 6072
Current error: 0.000550938561718

Current iteration: 6073
Current error: 0.000540425825679

Current iteration: 6074
Current error: 0.000537180054056

Current iteration: 6075
Current error: 0.000520229192085

Current iteration: 6076
Current error: 0.000510561826716

Current iteration: 6077
Current error: 0.000501187800512

Current iteration: 6078
Current error: 0.000492108581198

Current iteration: 6079
Current error: 0.00048489099556

Current iteration: 6080
Current error: 0.000475026083051

Current iteration: 6081
Current error: 0.000466985081421

Current iteration: 6082
Current error: 0.00045784845647

Current iteration: 6083
Current error: 0.000449894439662

Current iteration: 6084
Current error: 0.000442112212689

Current iteration: 6085
Current error: 0.000435643826056

Current iteration: 6086
Current error: 0.000427098935113

Current iteration: 6087
Current error: 0.000420486170608

Current iteration: 6088
Current error: 0.000412886352369

Current iteration: 6089
Current error: 0.000405983650088

Current iteration: 6090
Current error: 0.000399353896013

Current iteration: 6091
Current error: 0.000392909485983

Current iteration: 6092
Current error: 0.000386464588288

Current iteration: 6093
Current error: 0.000380228778671

Current iteration: 6094
Current error: 0.000374266638966

Current iteration: 6095
Current error: 0.000368211257848

Current iteration: 6096
Current error: 0.000362422744728

Current iteration: 6097
Current error: 0.000356830637983

Current iteration: 6098
Current error: 0.472842717817

Current iteration: 6099
Current error: 0.000614810666081

Current iteration: 6100
Current error: 0.000603652553179

Current iteration: 6101
Current error: 0.465101099288

Current iteration: 6102
Current error: 0.00102356798795

Current iteration: 6103
Current error: 0.001019839121

Current iteration: 6104
Current error: 0.000971985089403

Current iteration: 6105
Current error: 0.000947756707881

Current iteration: 6106
Current error: 0.00093134320874

Current iteration: 6107
Current error: 0.000914234851695

Current iteration: 6108
Current error: 0.000879930901986

Current iteration: 6109
Current error: 0.00085911709232

Current iteration: 6110
Current error: 0.000838705911267

Current iteration: 6111
Current error: 0.000819227595143

Current iteration: 6112
Current error: 0.000800359491055

Current iteration: 6113
Current error: 0.000782576354522

Current iteration: 6114
Current error: 0.461520511534

Current iteration: 6115
Current error: 0.00132488974457

Current iteration: 6116
Current error: 0.448978631367

Current iteration: 6117
Current error: 0.00218384868854

Current iteration: 6118
Current error: 0.00210508628359

Current iteration: 6119
Current error: 0.00202977411898

Current iteration: 6120
Current error: 0.00195910818244

Current iteration: 6121
Current error: 0.00189038628852

Current iteration: 6122
Current error: 0.00182590968133

Current iteration: 6123
Current error: 0.00176492961049

Current iteration: 6124
Current error: 0.00170683119478

Current iteration: 6125
Current error: 0.00165148013285

Current iteration: 6126
Current error: 0.0015984843704

Current iteration: 6127
Current error: 0.00154813194629

Current iteration: 6128
Current error: 0.00150008246624

Current iteration: 6129
Current error: 0.445746020898

Current iteration: 6130
Current error: 0.00246065831771

Current iteration: 6131
Current error: 0.0023638478904

Current iteration: 6132
Current error: 0.00227482506394

Current iteration: 6133
Current error: 0.434082204535

Current iteration: 6134
Current error: 0.0036719971999

Current iteration: 6135
Current error: 0.00348233823259

Current iteration: 6136
Current error: 0.00334928433705

Current iteration: 6137
Current error: 0.00318003668852

Current iteration: 6138
Current error: 0.00304288194873

Current iteration: 6139
Current error: 0.00291464391257

Current iteration: 6140
Current error: 0.00279390038949

Current iteration: 6141
Current error: 0.00268054564442

Current iteration: 6142
Current error: 0.00257351475948

Current iteration: 6143
Current error: 0.0024934310179

Current iteration: 6144
Current error: 0.00237753897102

Current iteration: 6145
Current error: 0.00228758770206

Current iteration: 6146
Current error: 0.00220316445506

Current iteration: 6147
Current error: 0.00212238825471

Current iteration: 6148
Current error: 0.00204887483454

Current iteration: 6149
Current error: 0.001974007939

Current iteration: 6150
Current error: 0.00190555536319

Current iteration: 6151
Current error: 0.00184045920374

Current iteration: 6152
Current error: 0.00177877032588

Current iteration: 6153
Current error: 0.0017201032462

Current iteration: 6154
Current error: 0.00166427280497

Current iteration: 6155
Current error: 0.00161039447784

Current iteration: 6156
Current error: 0.444536357518

Current iteration: 6157
Current error: 0.0026362546307

Current iteration: 6158
Current error: 0.00254583785419

Current iteration: 6159
Current error: 0.00243371805955

Current iteration: 6160
Current error: 0.00234215922387

Current iteration: 6161
Current error: 0.00225270779889

Current iteration: 6162
Current error: 0.00216984632073

Current iteration: 6163
Current error: 0.00209118983616

Current iteration: 6164
Current error: 0.0020167492517

Current iteration: 6165
Current error: 0.439352987624

Current iteration: 6166
Current error: 0.00327792408259

Current iteration: 6167
Current error: 0.00313381665093

Current iteration: 6168
Current error: 0.00299967566757

Current iteration: 6169
Current error: 0.00287450600292

Current iteration: 6170
Current error: 0.00275614798757

Current iteration: 6171
Current error: 0.0026443797255

Current iteration: 6172
Current error: 0.00253955557139

Current iteration: 6173
Current error: 0.00244095321176

Current iteration: 6174
Current error: 0.00234760887985

Current iteration: 6175
Current error: 0.00225926738946

Current iteration: 6176
Current error: 0.00218949267466

Current iteration: 6177
Current error: 0.00209686622061

Current iteration: 6178
Current error: 0.00202201650749

Current iteration: 6179
Current error: 0.00195113039356

Current iteration: 6180
Current error: 0.00188401194661

Current iteration: 6181
Current error: 0.00181995772852

Current iteration: 6182
Current error: 0.00175896970746

Current iteration: 6183
Current error: 0.00170108039392

Current iteration: 6184
Current error: 0.00164595371357

Current iteration: 6185
Current error: 0.00159341712171

Current iteration: 6186
Current error: 0.00154335633109

Current iteration: 6187
Current error: 0.00149551047505

Current iteration: 6188
Current error: 0.00144986465035

Current iteration: 6189
Current error: 0.00140621372722

Current iteration: 6190
Current error: 0.00136495380298

Current iteration: 6191
Current error: 0.448092848112

Current iteration: 6192
Current error: 0.00224520834495

Current iteration: 6193
Current error: 0.00216269582726

Current iteration: 6194
Current error: 0.435419479717

Current iteration: 6195
Current error: 0.00347945959525

Current iteration: 6196
Current error: 0.00332065758692

Current iteration: 6197
Current error: 0.00317487647365

Current iteration: 6198
Current error: 0.00303820718226

Current iteration: 6199
Current error: 0.425428869606

Current iteration: 6200
Current error: 0.00480480646282

Current iteration: 6201
Current error: 0.004560670919

Current iteration: 6202
Current error: 0.00432890311778

Current iteration: 6203
Current error: 0.00411320693155

Current iteration: 6204
Current error: 0.0039144203175

Current iteration: 6205
Current error: 0.00372972585059

Current iteration: 6206
Current error: 0.00355784711874

Current iteration: 6207
Current error: 0.00339637830485

Current iteration: 6208
Current error: 0.00324600041066

Current iteration: 6209
Current error: 0.0031050672388

Current iteration: 6210
Current error: 0.00297257879534

Current iteration: 6211
Current error: 0.0028523550219

Current iteration: 6212
Current error: 0.00273169179778

Current iteration: 6213
Current error: 0.00262230050779

Current iteration: 6214
Current error: 0.00254545844143

Current iteration: 6215
Current error: 0.00243364603753

Current iteration: 6216
Current error: 0.00232803096806

Current iteration: 6217
Current error: 0.00224156675763

Current iteration: 6218
Current error: 0.00215889511765

Current iteration: 6219
Current error: 0.00208064169319

Current iteration: 6220
Current error: 0.00200674554541

Current iteration: 6221
Current error: 0.00193715796064

Current iteration: 6222
Current error: 0.00187002298702

Current iteration: 6223
Current error: 0.00180655352896

Current iteration: 6224
Current error: 0.0017471982887

Current iteration: 6225
Current error: 0.00168921436225

Current iteration: 6226
Current error: 0.442447406997

Current iteration: 6227
Current error: 0.00275000549307

Current iteration: 6228
Current error: 0.00263938294338

Current iteration: 6229
Current error: 0.00253469661491

Current iteration: 6230
Current error: 0.00246808883046

Current iteration: 6231
Current error: 0.00234346287687

Current iteration: 6232
Current error: 0.00225734626188

Current iteration: 6233
Current error: 0.00218518882824

Current iteration: 6234
Current error: 0.00209310097668

Current iteration: 6235
Current error: 0.00201824141703

Current iteration: 6236
Current error: 0.00194747493452

Current iteration: 6237
Current error: 0.00188024739087

Current iteration: 6238
Current error: 0.00181650311335

Current iteration: 6239
Current error: 0.0017558217487

Current iteration: 6240
Current error: 0.00169803315667

Current iteration: 6241
Current error: 0.00164303740782

Current iteration: 6242
Current error: 0.0015906879663

Current iteration: 6243
Current error: 0.00154077680451

Current iteration: 6244
Current error: 0.00149306248738

Current iteration: 6245
Current error: 0.00144746901447

Current iteration: 6246
Current error: 0.00140393038215

Current iteration: 6247
Current error: 0.447736164739

Current iteration: 6248
Current error: 0.00231054844729

Current iteration: 6249
Current error: 0.00222438701529

Current iteration: 6250
Current error: 0.00214398828351

Current iteration: 6251
Current error: 0.00209593687102

Current iteration: 6252
Current error: 0.00199400127049

Current iteration: 6253
Current error: 0.00192943053412

Current iteration: 6254
Current error: 0.00185696458653

Current iteration: 6255
Current error: 0.00179413883517

Current iteration: 6256
Current error: 0.00173450527409

Current iteration: 6257
Current error: 0.00167793492711

Current iteration: 6258
Current error: 0.00162376230284

Current iteration: 6259
Current error: 0.00157287989272

Current iteration: 6260
Current error: 0.00152507910419

Current iteration: 6261
Current error: 0.00147620596238

Current iteration: 6262
Current error: 0.00143139132282

Current iteration: 6263
Current error: 0.00138862373417

Current iteration: 6264
Current error: 0.00134772195418

Current iteration: 6265
Current error: 0.00130847641622

Current iteration: 6266
Current error: 0.00127089038257

Current iteration: 6267
Current error: 0.00123509786533

Current iteration: 6268
Current error: 0.00120044724357

Current iteration: 6269
Current error: 0.00116743118967

Current iteration: 6270
Current error: 0.00113660659786

Current iteration: 6271
Current error: 0.00110520366686

Current iteration: 6272
Current error: 0.00107580292434

Current iteration: 6273
Current error: 0.00104756044205

Current iteration: 6274
Current error: 0.0010406387961

Current iteration: 6275
Current error: 0.000994462310805

Current iteration: 6276
Current error: 0.00098353843426

Current iteration: 6277
Current error: 0.000944943621359

Current iteration: 6278
Current error: 0.000924874986634

Current iteration: 6279
Current error: 0.000899117728805

Current iteration: 6280
Current error: 0.00087748433353

Current iteration: 6281
Current error: 0.000856611352627

Current iteration: 6282
Current error: 0.000836497482486

Current iteration: 6283
Current error: 0.00081707802

Current iteration: 6284
Current error: 0.000798269306172

Current iteration: 6285
Current error: 0.0007807226183

Current iteration: 6286
Current error: 0.000762598398331

Current iteration: 6287
Current error: 0.000745609493778

Current iteration: 6288
Current error: 0.000729177639721

Current iteration: 6289
Current error: 0.000713223892647

Current iteration: 6290
Current error: 0.000697849358291

Current iteration: 6291
Current error: 0.000683011195334

Current iteration: 6292
Current error: 0.000668507947022

Current iteration: 6293
Current error: 0.463273871435

Current iteration: 6294
Current error: 0.00113842708185

Current iteration: 6295
Current error: 0.00110156961166

Current iteration: 6296
Current error: 0.00107245419792

Current iteration: 6297
Current error: 0.00104570886941

Current iteration: 6298
Current error: 0.00101744052812

Current iteration: 6299
Current error: 0.000991467821437

Current iteration: 6300
Current error: 0.000968835612301

Current iteration: 6301
Current error: 0.0009427442532

Current iteration: 6302
Current error: 0.00091917502687

Current iteration: 6303
Current error: 0.000897599509351

Current iteration: 6304
Current error: 0.000875255738972

Current iteration: 6305
Current error: 0.000854465852952

Current iteration: 6306
Current error: 0.000834689448256

Current iteration: 6307
Current error: 0.000815062570498

Current iteration: 6308
Current error: 0.000796345415582

Current iteration: 6309
Current error: 0.459888926599

Current iteration: 6310
Current error: 0.00138853908528

Current iteration: 6311
Current error: 0.00130007371692

Current iteration: 6312
Current error: 0.00126289371914

Current iteration: 6313
Current error: 0.00122720223844

Current iteration: 6314
Current error: 0.00119305656843

Current iteration: 6315
Current error: 0.00116034874286

Current iteration: 6316
Current error: 0.00112883203176

Current iteration: 6317
Current error: 0.00109853790077

Current iteration: 6318
Current error: 0.00106947156682

Current iteration: 6319
Current error: 0.00104159133103

Current iteration: 6320
Current error: 0.454023671657

Current iteration: 6321
Current error: 0.00173250544529

Current iteration: 6322
Current error: 0.0016749620108

Current iteration: 6323
Current error: 0.00162109224391

Current iteration: 6324
Current error: 0.00156971294469

Current iteration: 6325
Current error: 0.00152058674765

Current iteration: 6326
Current error: 0.00147446467198

Current iteration: 6327
Current error: 0.0014291784405

Current iteration: 6328
Current error: 0.00138747458107

Current iteration: 6329
Current error: 0.00134558798385

Current iteration: 6330
Current error: 0.00130641238692

Current iteration: 6331
Current error: 0.00126914929148

Current iteration: 6332
Current error: 0.00123307434885

Current iteration: 6333
Current error: 0.00119860278075

Current iteration: 6334
Current error: 0.00117190766077

Current iteration: 6335
Current error: 0.00113396117402

Current iteration: 6336
Current error: 0.00110344033462

Current iteration: 6337
Current error: 0.00110647139381

Current iteration: 6338
Current error: 0.00104582004864

Current iteration: 6339
Current error: 0.00102195094707

Current iteration: 6340
Current error: 0.000992753808126

Current iteration: 6341
Current error: 0.000967759134605

Current iteration: 6342
Current error: 0.000943629643304

Current iteration: 6343
Current error: 0.000920399675159

Current iteration: 6344
Current error: 0.000898045027446

Current iteration: 6345
Current error: 0.456657795678

Current iteration: 6346
Current error: 0.00149805733095

Current iteration: 6347
Current error: 0.00145388209627

Current iteration: 6348
Current error: 0.0014085118552

Current iteration: 6349
Current error: 0.00136955151544

Current iteration: 6350
Current error: 0.00132666259478

Current iteration: 6351
Current error: 0.00128832279472

Current iteration: 6352
Current error: 0.00125549508926

Current iteration: 6353
Current error: 0.451539056295

Current iteration: 6354
Current error: 0.0020793274812

Current iteration: 6355
Current error: 0.00200583822873

Current iteration: 6356
Current error: 0.00193554677466

Current iteration: 6357
Current error: 0.00186882728007

Current iteration: 6358
Current error: 0.00180874323703

Current iteration: 6359
Current error: 0.00174706258065

Current iteration: 6360
Current error: 0.00168820704662

Current iteration: 6361
Current error: 0.00163366463518

Current iteration: 6362
Current error: 0.00158171655227

Current iteration: 6363
Current error: 0.00153271315464

Current iteration: 6364
Current error: 0.00148486081736

Current iteration: 6365
Current error: 0.00143967489739

Current iteration: 6366
Current error: 0.00139643549671

Current iteration: 6367
Current error: 0.00135519425202

Current iteration: 6368
Current error: 0.00131709223662

Current iteration: 6369
Current error: 0.00127902526685

Current iteration: 6370
Current error: 0.00124154178355

Current iteration: 6371
Current error: 0.00120908846431

Current iteration: 6372
Current error: 0.00117337050596

Current iteration: 6373
Current error: 0.0011415076821

Current iteration: 6374
Current error: 0.00112047592051

Current iteration: 6375
Current error: 0.00108105438384

Current iteration: 6376
Current error: 0.00105268183713

Current iteration: 6377
Current error: 0.00102546907081

Current iteration: 6378
Current error: 0.000999154427723

Current iteration: 6379
Current error: 0.000976851213359

Current iteration: 6380
Current error: 0.000950657292709

Current iteration: 6381
Current error: 0.000926555721499

Current iteration: 6382
Current error: 0.000903436236533

Current iteration: 6383
Current error: 0.000881689757279

Current iteration: 6384
Current error: 0.000860689945195

Current iteration: 6385
Current error: 0.000840406000388

Current iteration: 6386
Current error: 0.000820814393539

Current iteration: 6387
Current error: 0.000801875208795

Current iteration: 6388
Current error: 0.000783547278207

Current iteration: 6389
Current error: 0.000766010478208

Current iteration: 6390
Current error: 0.000748790497969

Current iteration: 6391
Current error: 0.000732463225799

Current iteration: 6392
Current error: 0.000717040019539

Current iteration: 6393
Current error: 0.000700799040297

Current iteration: 6394
Current error: 0.000685809140571

Current iteration: 6395
Current error: 0.000671351889154

Current iteration: 6396
Current error: 0.000657233901175

Current iteration: 6397
Current error: 0.000661214302134

Current iteration: 6398
Current error: 0.000630500446808

Current iteration: 6399
Current error: 0.000617492964315

Current iteration: 6400
Current error: 0.000605252016614

Current iteration: 6401
Current error: 0.000593110511615

Current iteration: 6402
Current error: 0.000581266379885

Current iteration: 6403
Current error: 0.466533893181

Current iteration: 6404
Current error: 0.000993052428166

Current iteration: 6405
Current error: 0.000968209875482

Current iteration: 6406
Current error: 0.000943913660688

Current iteration: 6407
Current error: 0.000922935201411

Current iteration: 6408
Current error: 0.000906963314298

Current iteration: 6409
Current error: 0.000876716372325

Current iteration: 6410
Current error: 0.000855837784462

Current iteration: 6411
Current error: 0.000835616367837

Current iteration: 6412
Current error: 0.000816156299771

Current iteration: 6413
Current error: 0.000811047095439

Current iteration: 6414
Current error: 0.000779862970718

Current iteration: 6415
Current error: 0.000761634666885

Current iteration: 6416
Current error: 0.000744869205746

Current iteration: 6417
Current error: 0.000728382308161

Current iteration: 6418
Current error: 0.000712456317362

Current iteration: 6419
Current error: 0.000699548877188

Current iteration: 6420
Current error: 0.000682270599933

Current iteration: 6421
Current error: 0.000667782567235

Current iteration: 6422
Current error: 0.000653915244981

Current iteration: 6423
Current error: 0.000641823432035

Current iteration: 6424
Current error: 0.000628022719236

Current iteration: 6425
Current error: 0.000614448600401

Current iteration: 6426
Current error: 0.00060212311344

Current iteration: 6427
Current error: 0.000590164526719

Current iteration: 6428
Current error: 0.000578501025006

Current iteration: 6429
Current error: 0.000567242397218

Current iteration: 6430
Current error: 0.00055626232306

Current iteration: 6431
Current error: 0.000545585900623

Current iteration: 6432
Current error: 0.000535232516167

Current iteration: 6433
Current error: 0.000525186180735

Current iteration: 6434
Current error: 0.000515815330881

Current iteration: 6435
Current error: 0.000506488814459

Current iteration: 6436
Current error: 0.00049662278491

Current iteration: 6437
Current error: 0.000489515335936

Current iteration: 6438
Current error: 0.000478833917802

Current iteration: 6439
Current error: 0.000470423804592

Current iteration: 6440
Current error: 0.000461951069662

Current iteration: 6441
Current error: 0.00045404238218

Current iteration: 6442
Current error: 0.000445961745523

Current iteration: 6443
Current error: 0.000440280381836

Current iteration: 6444
Current error: 0.000430778219596

Current iteration: 6445
Current error: 0.000423565377509

Current iteration: 6446
Current error: 0.000416355966146

Current iteration: 6447
Current error: 0.000409452923975

Current iteration: 6448
Current error: 0.000402741665286

Current iteration: 6449
Current error: 0.000396097203767

Current iteration: 6450
Current error: 0.00038975372553

Current iteration: 6451
Current error: 0.000404281280201

Current iteration: 6452
Current error: 0.000377056128549

Current iteration: 6453
Current error: 0.000375513645613

Current iteration: 6454
Current error: 0.000365384585386

Current iteration: 6455
Current error: 0.000359461368695

Current iteration: 6456
Current error: 0.000353894301378

Current iteration: 6457
Current error: 0.000348587609186

Current iteration: 6458
Current error: 0.00034311929671

Current iteration: 6459
Current error: 0.000337978495802

Current iteration: 6460
Current error: 0.000333096671728

Current iteration: 6461
Current error: 0.000328018520267

Current iteration: 6462
Current error: 0.000322960762292

Current iteration: 6463
Current error: 0.000320032572535

Current iteration: 6464
Current error: 0.000313562731861

Current iteration: 6465
Current error: 0.000308957947738

Current iteration: 6466
Current error: 0.000304940761665

Current iteration: 6467
Current error: 0.000300142120437

Current iteration: 6468
Current error: 0.00029601456715

Current iteration: 6469
Current error: 0.000291665175394

Current iteration: 6470
Current error: 0.000287550686915

Current iteration: 6471
Current error: 0.000283539837103

Current iteration: 6472
Current error: 0.00027966023329

Current iteration: 6473
Current error: 0.000275820769526

Current iteration: 6474
Current error: 0.000272993891272

Current iteration: 6475
Current error: 0.476391071766

Current iteration: 6476
Current error: 0.000472306817856

Current iteration: 6477
Current error: 0.000463869474163

Current iteration: 6478
Current error: 0.00045573827758

Current iteration: 6479
Current error: 0.000452884819069

Current iteration: 6480
Current error: 0.0004400217569

Current iteration: 6481
Current error: 0.000432889013073

Current iteration: 6482
Current error: 0.000425215678906

Current iteration: 6483
Current error: 0.000418910942718

Current iteration: 6484
Current error: 0.000415959349809

Current iteration: 6485
Current error: 0.000404174810634

Current iteration: 6486
Current error: 0.000397515285759

Current iteration: 6487
Current error: 0.000391053049337

Current iteration: 6488
Current error: 0.000384737400923

Current iteration: 6489
Current error: 0.000378545927759

Current iteration: 6490
Current error: 0.000372500006702

Current iteration: 6491
Current error: 0.000366616098853

Current iteration: 6492
Current error: 0.00036096385779

Current iteration: 6493
Current error: 0.000362238012429

Current iteration: 6494
Current error: 0.000349725585806

Current iteration: 6495
Current error: 0.000344413360766

Current iteration: 6496
Current error: 0.000339178172832

Current iteration: 6497
Current error: 0.000335217097533

Current iteration: 6498
Current error: 0.000328999077773

Current iteration: 6499
Current error: 0.000324549781799

Current iteration: 6500
Current error: 0.000319408258588

Current iteration: 6501
Current error: 0.000314774427307

Current iteration: 6502
Current error: 0.000310046873987

Current iteration: 6503
Current error: 0.000305558330154

Current iteration: 6504
Current error: 0.000301281853585

Current iteration: 6505
Current error: 0.000296872899804

Current iteration: 6506
Current error: 0.475547637963

Current iteration: 6507
Current error: 0.000515100780279

Current iteration: 6508
Current error: 0.000505591078647

Current iteration: 6509
Current error: 0.00049633956341

Current iteration: 6510
Current error: 0.000487350320982

Current iteration: 6511
Current error: 0.000478586512297

Current iteration: 6512
Current error: 0.000478995397594

Current iteration: 6513
Current error: 0.000461668964626

Current iteration: 6514
Current error: 0.000454237161103

Current iteration: 6515
Current error: 0.000445686592839

Current iteration: 6516
Current error: 0.000438069322415

Current iteration: 6517
Current error: 0.468846136486

Current iteration: 6518
Current error: 0.0007462353537

Current iteration: 6519
Current error: 0.000729732137805

Current iteration: 6520
Current error: 0.000713868747634

Current iteration: 6521
Current error: 0.000698465891243

Current iteration: 6522
Current error: 0.000683494781488

Current iteration: 6523
Current error: 0.000669346757674

Current iteration: 6524
Current error: 0.0006584908761

Current iteration: 6525
Current error: 0.000641478893028

Current iteration: 6526
Current error: 0.000628315083094

Current iteration: 6527
Current error: 0.000615563252486

Current iteration: 6528
Current error: 0.000603243026355

Current iteration: 6529
Current error: 0.000591252598691

Current iteration: 6530
Current error: 0.000579529175077

Current iteration: 6531
Current error: 0.000569578391632

Current iteration: 6532
Current error: 0.000557200583444

Current iteration: 6533
Current error: 0.000546505994386

Current iteration: 6534
Current error: 0.000536151763164

Current iteration: 6535
Current error: 0.000527023422243

Current iteration: 6536
Current error: 0.000516228517447

Current iteration: 6537
Current error: 0.000506738364385

Current iteration: 6538
Current error: 0.000497712437293

Current iteration: 6539
Current error: 0.000488793066736

Current iteration: 6540
Current error: 0.000479636516633

Current iteration: 6541
Current error: 0.000471027809456

Current iteration: 6542
Current error: 0.000462660273742

Current iteration: 6543
Current error: 0.000454565400779

Current iteration: 6544
Current error: 0.000446645155874

Current iteration: 6545
Current error: 0.468865337601

Current iteration: 6546
Current error: 0.000762981448627

Current iteration: 6547
Current error: 0.000744738507095

Current iteration: 6548
Current error: 0.000728358151151

Current iteration: 6549
Current error: 0.000712935705501

Current iteration: 6550
Current error: 0.462174901195

Current iteration: 6551
Current error: 0.00122152952889

Current iteration: 6552
Current error: 0.00117527775086

Current iteration: 6553
Current error: 0.00113907083779

Current iteration: 6554
Current error: 0.00110849559195

Current iteration: 6555
Current error: 0.00107903830798

Current iteration: 6556
Current error: 0.00105066965725

Current iteration: 6557
Current error: 0.00102352706238

Current iteration: 6558
Current error: 0.454731966689

Current iteration: 6559
Current error: 0.00170515723285

Current iteration: 6560
Current error: 0.00166016905781

Current iteration: 6561
Current error: 0.00159695425277

Current iteration: 6562
Current error: 0.00157374687049

Current iteration: 6563
Current error: 0.00149882226591

Current iteration: 6564
Current error: 0.00145323721127

Current iteration: 6565
Current error: 0.00140996867193

Current iteration: 6566
Current error: 0.00136727380907

Current iteration: 6567
Current error: 0.00132759962336

Current iteration: 6568
Current error: 0.00128872955615

Current iteration: 6569
Current error: 0.00125376506535

Current iteration: 6570
Current error: 0.00123793639918

Current iteration: 6571
Current error: 0.00118292688625

Current iteration: 6572
Current error: 0.00119867410377

Current iteration: 6573
Current error: 0.00111893113446

Current iteration: 6574
Current error: 0.00108909316979

Current iteration: 6575
Current error: 0.00106037864084

Current iteration: 6576
Current error: 0.00103286224182

Current iteration: 6577
Current error: 0.0010067494271

Current iteration: 6578
Current error: 0.00098076073399

Current iteration: 6579
Current error: 0.000956171819978

Current iteration: 6580
Current error: 0.000932648415211

Current iteration: 6581
Current error: 0.000912155912636

Current iteration: 6582
Current error: 0.000887597062503

Current iteration: 6583
Current error: 0.000867621304707

Current iteration: 6584
Current error: 0.000845891238546

Current iteration: 6585
Current error: 0.000827350684404

Current iteration: 6586
Current error: 0.000807218267106

Current iteration: 6587
Current error: 0.00078853335282

Current iteration: 6588
Current error: 0.000770733306433

Current iteration: 6589
Current error: 0.460734810009

Current iteration: 6590
Current error: 0.449266103863

Current iteration: 6591
Current error: 0.00225598206456

Current iteration: 6592
Current error: 0.00212838831332

Current iteration: 6593
Current error: 0.00205248760844

Current iteration: 6594
Current error: 0.00197962599863

Current iteration: 6595
Current error: 0.00191059016896

Current iteration: 6596
Current error: 0.00184558863729

Current iteration: 6597
Current error: 0.00178328735614

Current iteration: 6598
Current error: 0.00172428904775

Current iteration: 6599
Current error: 0.00166799184617

Current iteration: 6600
Current error: 0.442141683844

Current iteration: 6601
Current error: 0.00271219810075

Current iteration: 6602
Current error: 0.429920011386

Current iteration: 6603
Current error: 0.00432859777871

Current iteration: 6604
Current error: 0.00411510792706

Current iteration: 6605
Current error: 0.00391641730377

Current iteration: 6606
Current error: 0.413608375981

Current iteration: 6607
Current error: 0.00604496892453

Current iteration: 6608
Current error: 0.00570351043061

Current iteration: 6609
Current error: 0.00549079765647

Current iteration: 6610
Current error: 0.0050905747762

Current iteration: 6611
Current error: 0.004821059715

Current iteration: 6612
Current error: 0.00457206009107

Current iteration: 6613
Current error: 0.0043409017475

Current iteration: 6614
Current error: 0.0041268191465

Current iteration: 6615
Current error: 0.00392720567722

Current iteration: 6616
Current error: 0.00374175611725

Current iteration: 6617
Current error: 0.00356867535107

Current iteration: 6618
Current error: 0.00340678468049

Current iteration: 6619
Current error: 0.00325559396473

Current iteration: 6620
Current error: 0.00311388749564

Current iteration: 6621
Current error: 0.00298227065502

Current iteration: 6622
Current error: 0.00285647255619

Current iteration: 6623
Current error: 0.00273924141778

Current iteration: 6624
Current error: 0.00262892109535

Current iteration: 6625
Current error: 0.00252499998528

Current iteration: 6626
Current error: 0.00242703603865

Current iteration: 6627
Current error: 0.00233458921761

Current iteration: 6628
Current error: 0.00224958232287

Current iteration: 6629
Current error: 0.0021642980867

Current iteration: 6630
Current error: 0.00208596161255

Current iteration: 6631
Current error: 0.00201653452444

Current iteration: 6632
Current error: 0.00195801379066

Current iteration: 6633
Current error: 0.00187422304014

Current iteration: 6634
Current error: 0.00181149133034

Current iteration: 6635
Current error: 0.437873730842

Current iteration: 6636
Current error: 0.00291106307916

Current iteration: 6637
Current error: 0.00279118607796

Current iteration: 6638
Current error: 0.0027378479695

Current iteration: 6639
Current error: 0.00257037222177

Current iteration: 6640
Current error: 0.00246958658044

Current iteration: 6641
Current error: 0.00237455789103

Current iteration: 6642
Current error: 0.00228491757742

Current iteration: 6643
Current error: 0.00220014151284

Current iteration: 6644
Current error: 0.00211986541058

Current iteration: 6645
Current error: 0.0020440257423

Current iteration: 6646
Current error: 0.438063487107

Current iteration: 6647
Current error: 0.0034032985294

Current iteration: 6648
Current error: 0.00316400910748

Current iteration: 6649
Current error: 0.00302594288805

Current iteration: 6650
Current error: 0.00289875648077

Current iteration: 6651
Current error: 0.426049247432

Current iteration: 6652
Current error: 0.00458142778676

Current iteration: 6653
Current error: 0.00435231788295

Current iteration: 6654
Current error: 0.408657182085

Current iteration: 6655
Current error: 0.0066474880268

Current iteration: 6656
Current error: 0.00629803875399

Current iteration: 6657
Current error: 0.00594337022392

Current iteration: 6658
Current error: 0.00555894051151

Current iteration: 6659
Current error: 0.00525334811986

Current iteration: 6660
Current error: 0.0049719616433

Current iteration: 6661
Current error: 0.00471135188335

Current iteration: 6662
Current error: 0.0045636853352

Current iteration: 6663
Current error: 0.00424509282019

Current iteration: 6664
Current error: 0.00403749373562

Current iteration: 6665
Current error: 0.00386903588704

Current iteration: 6666
Current error: 0.00370466228942

Current iteration: 6667
Current error: 0.00349555440572

Current iteration: 6668
Current error: 0.00333874294504

Current iteration: 6669
Current error: 0.00319191061701

Current iteration: 6670
Current error: 0.00305421059662

Current iteration: 6671
Current error: 0.0029251620644

Current iteration: 6672
Current error: 0.00283050731208

Current iteration: 6673
Current error: 0.00268981638124

Current iteration: 6674
Current error: 0.00258196387343

Current iteration: 6675
Current error: 0.00248082812616

Current iteration: 6676
Current error: 0.00238512260573

Current iteration: 6677
Current error: 0.0022949380536

Current iteration: 6678
Current error: 0.00220979528973

Current iteration: 6679
Current error: 0.00212892672023

Current iteration: 6680
Current error: 0.00205241622759

Current iteration: 6681
Current error: 0.00197993962938

Current iteration: 6682
Current error: 0.0019111831832

Current iteration: 6683
Current error: 0.00184954220406

Current iteration: 6684
Current error: 0.00183516280145

Current iteration: 6685
Current error: 0.440698136125

Current iteration: 6686
Current error: 0.00289327264419

Current iteration: 6687
Current error: 0.00277357335238

Current iteration: 6688
Current error: 0.00266127783328

Current iteration: 6689
Current error: 0.00255560896807

Current iteration: 6690
Current error: 0.00245585604817

Current iteration: 6691
Current error: 0.00236164239152

Current iteration: 6692
Current error: 0.00227268558288

Current iteration: 6693
Current error: 0.435303038868

Current iteration: 6694
Current error: 0.0036629932557

Current iteration: 6695
Current error: 0.00349459572328

Current iteration: 6696
Current error: 0.00333763708844

Current iteration: 6697
Current error: 0.00319088686648

Current iteration: 6698
Current error: 0.00305320623783

Current iteration: 6699
Current error: 0.424650866417

Current iteration: 6700
Current error: 0.0048175778156

Current iteration: 6701
Current error: 0.00456790329932

Current iteration: 6702
Current error: 0.00440986167415

Current iteration: 6703
Current error: 0.00412236422302

Current iteration: 6704
Current error: 0.00392351070362

Current iteration: 6705
Current error: 0.00373734626521

Current iteration: 6706
Current error: 0.00357712922554

Current iteration: 6707
Current error: 0.0034195225621

Current iteration: 6708
Current error: 0.00325215961654

Current iteration: 6709
Current error: 0.00311052043519

Current iteration: 6710
Current error: 0.00297776855737

Current iteration: 6711
Current error: 0.00286545886631

Current iteration: 6712
Current error: 0.00273616345523

Current iteration: 6713
Current error: 0.00262654883927

Current iteration: 6714
Current error: 0.00252231538861

Current iteration: 6715
Current error: 0.00242470164832

Current iteration: 6716
Current error: 0.00236045703093

Current iteration: 6717
Current error: 0.00224452477671

Current iteration: 6718
Current error: 0.00216181783943

Current iteration: 6719
Current error: 0.00208361904033

Current iteration: 6720
Current error: 0.00200951402874

Current iteration: 6721
Current error: 0.00193952348136

Current iteration: 6722
Current error: 0.0018892276169

Current iteration: 6723
Current error: 0.00180885832226

Current iteration: 6724
Current error: 0.0017486968592

Current iteration: 6725
Current error: 0.00169121844491

Current iteration: 6726
Current error: 0.00163827027234

Current iteration: 6727
Current error: 0.00158442690865

Current iteration: 6728
Current error: 0.00153471453325

Current iteration: 6729
Current error: 0.00148828813865

Current iteration: 6730
Current error: 0.00144646493272

Current iteration: 6731
Current error: 0.00140223953137

Current iteration: 6732
Current error: 0.00135734687301

Current iteration: 6733
Current error: 0.0013872425757

Current iteration: 6734
Current error: 0.00127937347598

Current iteration: 6735
Current error: 0.00124277834537

Current iteration: 6736
Current error: 0.00120793917609

Current iteration: 6737
Current error: 0.00117455296936

Current iteration: 6738
Current error: 0.00114248180269

Current iteration: 6739
Current error: 0.00111175331039

Current iteration: 6740
Current error: 0.00110800494585

Current iteration: 6741
Current error: 0.00105357270707

Current iteration: 6742
Current error: 0.00102646132666

Current iteration: 6743
Current error: 0.000999980609545

Current iteration: 6744
Current error: 0.000974623494382

Current iteration: 6745
Current error: 0.000950657384313

Current iteration: 6746
Current error: 0.000926836493235

Current iteration: 6747
Current error: 0.00090416821002

Current iteration: 6748
Current error: 0.000882370981998

Current iteration: 6749
Current error: 0.457866411402

Current iteration: 6750
Current error: 0.00147858481698

Current iteration: 6751
Current error: 0.00143379093074

Current iteration: 6752
Current error: 0.00140929551784

Current iteration: 6753
Current error: 0.00135412896187

Current iteration: 6754
Current error: 0.00131025532203

Current iteration: 6755
Current error: 0.00127262792927

Current iteration: 6756
Current error: 0.00123655086281

Current iteration: 6757
Current error: 0.00120250444196

Current iteration: 6758
Current error: 0.00116935386331

Current iteration: 6759
Current error: 0.00119847350674

Current iteration: 6760
Current error: 0.00110598084899

Current iteration: 6761
Current error: 0.00110266289098

Current iteration: 6762
Current error: 0.00104857197223

Current iteration: 6763
Current error: 0.00102121425923

Current iteration: 6764
Current error: 0.000994939856622

Current iteration: 6765
Current error: 0.000970074646136

Current iteration: 6766
Current error: 0.000945697310126

Current iteration: 6767
Current error: 0.000923003416307

Current iteration: 6768
Current error: 0.000899829836886

Current iteration: 6769
Current error: 0.000878219740389

Current iteration: 6770
Current error: 0.000857292405547

Current iteration: 6771
Current error: 0.000837239657055

Current iteration: 6772
Current error: 0.000822724350917

Current iteration: 6773
Current error: 0.000800999898303

Current iteration: 6774
Current error: 0.000780620404653

Current iteration: 6775
Current error: 0.000763060196348

Current iteration: 6776
Current error: 0.000746023049507

Current iteration: 6777
Current error: 0.000729581148865

Current iteration: 6778
Current error: 0.000713701026471

Current iteration: 6779
Current error: 0.000698278937677

Current iteration: 6780
Current error: 0.0006840062402

Current iteration: 6781
Current error: 0.00066936014647

Current iteration: 6782
Current error: 0.000654972314085

Current iteration: 6783
Current error: 0.000641392601261

Current iteration: 6784
Current error: 0.000647666959013

Current iteration: 6785
Current error: 0.000615325942797

Current iteration: 6786
Current error: 0.000603046571575

Current iteration: 6787
Current error: 0.000591000110052

Current iteration: 6788
Current error: 0.000579329436517

Current iteration: 6789
Current error: 0.000567977997484

Current iteration: 6790
Current error: 0.000558107707344

Current iteration: 6791
Current error: 0.000546734053095

Current iteration: 6792
Current error: 0.000535983566694

Current iteration: 6793
Current error: 0.000526152767968

Current iteration: 6794
Current error: 0.000516047807204

Current iteration: 6795
Current error: 0.000506527116478

Current iteration: 6796
Current error: 0.000497260188331

Current iteration: 6797
Current error: 0.000497530076772

Current iteration: 6798
Current error: 0.00047973037494

Current iteration: 6799
Current error: 0.000470811076985

Current iteration: 6800
Current error: 0.000462474846966

Current iteration: 6801
Current error: 0.000454405061099

Current iteration: 6802
Current error: 0.46711397858

Current iteration: 6803
Current error: 0.000768675695323

Current iteration: 6804
Current error: 0.000751543185644

Current iteration: 6805
Current error: 0.000735221218267

Current iteration: 6806
Current error: 0.000719018049233

Current iteration: 6807
Current error: 0.000703250641017

Current iteration: 6808
Current error: 0.000688203053771

Current iteration: 6809
Current error: 0.000673659991197

Current iteration: 6810
Current error: 0.000659575833546

Current iteration: 6811
Current error: 0.000646833956007

Current iteration: 6812
Current error: 0.000632594498777

Current iteration: 6813
Current error: 0.463641666914

Current iteration: 6814
Current error: 0.00107008656473

Current iteration: 6815
Current error: 0.001042060034

Current iteration: 6816
Current error: 0.00101591787242

Current iteration: 6817
Current error: 0.000989325287435

Current iteration: 6818
Current error: 0.00099649472433

Current iteration: 6819
Current error: 0.000940159822553

Current iteration: 6820
Current error: 0.000918336428737

Current iteration: 6821
Current error: 0.000896228471574

Current iteration: 6822
Current error: 0.00087358787677

Current iteration: 6823
Current error: 0.000852551844055

Current iteration: 6824
Current error: 0.000832560097921

Current iteration: 6825
Current error: 0.000814363582657

Current iteration: 6826
Current error: 0.00079469312638

Current iteration: 6827
Current error: 0.000776517764482

Current iteration: 6828
Current error: 0.000759109746322

Current iteration: 6829
Current error: 0.000742261805721

Current iteration: 6830
Current error: 0.000725911132525

Current iteration: 6831
Current error: 0.000710407635988

Current iteration: 6832
Current error: 0.000694816476901

Current iteration: 6833
Current error: 0.00068064765505

Current iteration: 6834
Current error: 0.000665681855348

Current iteration: 6835
Current error: 0.000651776817501

Current iteration: 6836
Current error: 0.000638416890474

Current iteration: 6837
Current error: 0.000629362769572

Current iteration: 6838
Current error: 0.000612568454988

Current iteration: 6839
Current error: 0.000600367234

Current iteration: 6840
Current error: 0.000588372288251

Current iteration: 6841
Current error: 0.0005767959286

Current iteration: 6842
Current error: 0.000565555318621

Current iteration: 6843
Current error: 0.000554614735067

Current iteration: 6844
Current error: 0.000544033131141

Current iteration: 6845
Current error: 0.00053377232839

Current iteration: 6846
Current error: 0.000523707034433

Current iteration: 6847
Current error: 0.000514091533037

Current iteration: 6848
Current error: 0.000504648064253

Current iteration: 6849
Current error: 0.467986992861

Current iteration: 6850
Current error: 0.455657671618

Current iteration: 6851
Current error: 0.00146595423

Current iteration: 6852
Current error: 0.00145195145252

Current iteration: 6853
Current error: 0.00137975457637

Current iteration: 6854
Current error: 0.00133855122041

Current iteration: 6855
Current error: 0.001302594414

Current iteration: 6856
Current error: 0.00126234986807

Current iteration: 6857
Current error: 0.00122665322625

Current iteration: 6858
Current error: 0.00119255691351

Current iteration: 6859
Current error: 0.00115975588121

Current iteration: 6860
Current error: 0.00112917278821

Current iteration: 6861
Current error: 0.00109818095739

Current iteration: 6862
Current error: 0.0010704449882

Current iteration: 6863
Current error: 0.00104115729868

Current iteration: 6864
Current error: 0.454383359928

Current iteration: 6865
Current error: 0.00173398638711

Current iteration: 6866
Current error: 0.441627023181

Current iteration: 6867
Current error: 0.00281908897956

Current iteration: 6868
Current error: 0.00270434352376

Current iteration: 6869
Current error: 0.0025957739751

Current iteration: 6870
Current error: 0.00249375893649

Current iteration: 6871
Current error: 0.00239757627888

Current iteration: 6872
Current error: 0.00230670297739

Current iteration: 6873
Current error: 0.00222640140187

Current iteration: 6874
Current error: 0.00214485339136

Current iteration: 6875
Current error: 0.00206728165676

Current iteration: 6876
Current error: 0.00198937495074

Current iteration: 6877
Current error: 0.00192028656592

Current iteration: 6878
Current error: 0.00185430454311

Current iteration: 6879
Current error: 0.0017916487351

Current iteration: 6880
Current error: 0.00173267885969

Current iteration: 6881
Current error: 0.0016779876369

Current iteration: 6882
Current error: 0.00162158714515

Current iteration: 6883
Current error: 0.00157020600959

Current iteration: 6884
Current error: 0.440543722424

Current iteration: 6885
Current error: 0.00253300765496

Current iteration: 6886
Current error: 0.00244398508216

Current iteration: 6887
Current error: 0.00238358284088

Current iteration: 6888
Current error: 0.00225359123867

Current iteration: 6889
Current error: 0.00217012673953

Current iteration: 6890
Current error: 0.00209232343064

Current iteration: 6891
Current error: 0.00201725472324

Current iteration: 6892
Current error: 0.432521091528

Current iteration: 6893
Current error: 0.00320792047202

Current iteration: 6894
Current error: 0.00306438510538

Current iteration: 6895
Current error: 0.00294223406568

Current iteration: 6896
Current error: 0.00293080125136

Current iteration: 6897
Current error: 0.00269656373727

Current iteration: 6898
Current error: 0.00258881245372

Current iteration: 6899
Current error: 0.00248839805859

Current iteration: 6900
Current error: 0.00239154450827

Current iteration: 6901
Current error: 0.00230158452939

Current iteration: 6902
Current error: 0.00221508470093

Current iteration: 6903
Current error: 0.00213439933685

Current iteration: 6904
Current error: 0.00205738007337

Current iteration: 6905
Current error: 0.00198562263568

Current iteration: 6906
Current error: 0.0020041157223

Current iteration: 6907
Current error: 0.001849030858

Current iteration: 6908
Current error: 0.00178899414147

Current iteration: 6909
Current error: 0.00172776852981

Current iteration: 6910
Current error: 0.00167133870927

Current iteration: 6911
Current error: 0.0016175268569

Current iteration: 6912
Current error: 0.00156625304823

Current iteration: 6913
Current error: 0.00151735702774

Current iteration: 6914
Current error: 0.00147083647613

Current iteration: 6915
Current error: 0.00142639930286

Current iteration: 6916
Current error: 0.00138359668318

Current iteration: 6917
Current error: 0.00134279679791

Current iteration: 6918
Current error: 0.00130395893744

Current iteration: 6919
Current error: 0.00126646655229

Current iteration: 6920
Current error: 0.00123065858995

Current iteration: 6921
Current error: 0.00119692707155

Current iteration: 6922
Current error: 0.451336667558

Current iteration: 6923
Current error: 0.00198135697813

Current iteration: 6924
Current error: 0.00191267232949

Current iteration: 6925
Current error: 0.0018491287241

Current iteration: 6926
Current error: 0.00178490425621

Current iteration: 6927
Current error: 0.00172570687214

Current iteration: 6928
Current error: 0.00166955797759

Current iteration: 6929
Current error: 0.00161603320098

Current iteration: 6930
Current error: 0.00156490228635

Current iteration: 6931
Current error: 0.00151809144886

Current iteration: 6932
Current error: 0.0014694767698

Current iteration: 6933
Current error: 0.00142519499444

Current iteration: 6934
Current error: 0.00138227329343

Current iteration: 6935
Current error: 0.0013429138126

Current iteration: 6936
Current error: 0.0013025764332

Current iteration: 6937
Current error: 0.00126531558178

Current iteration: 6938
Current error: 0.00123119913603

Current iteration: 6939
Current error: 0.00119612651572

Current iteration: 6940
Current error: 0.00116235375757

Current iteration: 6941
Current error: 0.00113085982797

Current iteration: 6942
Current error: 0.4528616295

Current iteration: 6943
Current error: 0.00187906638953

Current iteration: 6944
Current error: 0.00181939635846

Current iteration: 6945
Current error: 0.0017552965063

Current iteration: 6946
Current error: 0.00169702161483

Current iteration: 6947
Current error: 0.00164197008233

Current iteration: 6948
Current error: 0.00158961254992

Current iteration: 6949
Current error: 0.00153995614069

Current iteration: 6950
Current error: 0.00149207363604

Current iteration: 6951
Current error: 0.00144662686533

Current iteration: 6952
Current error: 0.00140305210017

Current iteration: 6953
Current error: 0.00136146346165

Current iteration: 6954
Current error: 0.00132165314348

Current iteration: 6955
Current error: 0.00128377233738

Current iteration: 6956
Current error: 0.00124705813817

Current iteration: 6957
Current error: 0.00121210988832

Current iteration: 6958
Current error: 0.00117852763573

Current iteration: 6959
Current error: 0.00116749058607

Current iteration: 6960
Current error: 0.00115819049991

Current iteration: 6961
Current error: 0.00108511278599

Current iteration: 6962
Current error: 0.00105664664494

Current iteration: 6963
Current error: 0.00102957168238

Current iteration: 6964
Current error: 0.00100352534614

Current iteration: 6965
Current error: 0.000977373964579

Current iteration: 6966
Current error: 0.000952882459213

Current iteration: 6967
Current error: 0.000929851572961

Current iteration: 6968
Current error: 0.000906585957665

Current iteration: 6969
Current error: 0.000884680310905

Current iteration: 6970
Current error: 0.000863607545237

Current iteration: 6971
Current error: 0.00086431520708

Current iteration: 6972
Current error: 0.000823684690132

Current iteration: 6973
Current error: 0.000804376543847

Current iteration: 6974
Current error: 0.000785989437863

Current iteration: 6975
Current error: 0.00076822842723

Current iteration: 6976
Current error: 0.461420017061

Current iteration: 6977
Current error: 0.00129994538823

Current iteration: 6978
Current error: 0.00126202767966

Current iteration: 6979
Current error: 0.00122643299816

Current iteration: 6980
Current error: 0.00119395066399

Current iteration: 6981
Current error: 0.00115958997785

Current iteration: 6982
Current error: 0.00117254798404

Current iteration: 6983
Current error: 0.00109922896026

Current iteration: 6984
Current error: 0.00106930682158

Current iteration: 6985
Current error: 0.00104078935679

Current iteration: 6986
Current error: 0.00101998814429

Current iteration: 6987
Current error: 0.000987917521147

Current iteration: 6988
Current error: 0.000963028751213

Current iteration: 6989
Current error: 0.00093909963205

Current iteration: 6990
Current error: 0.000916044375589

Current iteration: 6991
Current error: 0.000893816525568

Current iteration: 6992
Current error: 0.000872691657566

Current iteration: 6993
Current error: 0.000851669639893

Current iteration: 6994
Current error: 0.457684576558

Current iteration: 6995
Current error: 0.00142373182712

Current iteration: 6996
Current error: 0.00138111193395

Current iteration: 6997
Current error: 0.00134042484176

Current iteration: 6998
Current error: 0.00130190606533

Current iteration: 6999
Current error: 0.00126514011175

Current iteration: 7000
Current error: 0.00122873381163

Current iteration: 7001
Current error: 0.449217589295

Current iteration: 7002
Current error: 0.00202093601775

Current iteration: 7003
Current error: 0.0019516626899

Current iteration: 7004
Current error: 0.00188277729328

Current iteration: 7005
Current error: 0.00181861725455

Current iteration: 7006
Current error: 0.00175790627653

Current iteration: 7007
Current error: 0.00170003854378

Current iteration: 7008
Current error: 0.00164493754083

Current iteration: 7009
Current error: 0.00159244910272

Current iteration: 7010
Current error: 0.00154818576043

Current iteration: 7011
Current error: 0.00149459453444

Current iteration: 7012
Current error: 0.001449023793

Current iteration: 7013
Current error: 0.0014056033226

Current iteration: 7014
Current error: 0.00136388218141

Current iteration: 7015
Current error: 0.00133242029015

Current iteration: 7016
Current error: 0.00128551763565

Current iteration: 7017
Current error: 0.00124992244919

Current iteration: 7018
Current error: 0.0012138594494

Current iteration: 7019
Current error: 0.00118023750327

Current iteration: 7020
Current error: 0.00114796718993

Current iteration: 7021
Current error: 0.00111700291125

Current iteration: 7022
Current error: 0.00108831785283

Current iteration: 7023
Current error: 0.00105861774852

Current iteration: 7024
Current error: 0.00103108579126

Current iteration: 7025
Current error: 0.00100458556462

Current iteration: 7026
Current error: 0.00101680456195

Current iteration: 7027
Current error: 0.000955225666864

Current iteration: 7028
Current error: 0.000930634545046

Current iteration: 7029
Current error: 0.000908010768166

Current iteration: 7030
Current error: 0.000885919214673

Current iteration: 7031
Current error: 0.000864920358343

Current iteration: 7032
Current error: 0.00084433041425

Current iteration: 7033
Current error: 0.000824611980611

Current iteration: 7034
Current error: 0.000805533486546

Current iteration: 7035
Current error: 0.000787324315806

Current iteration: 7036
Current error: 0.000769438315712

Current iteration: 7037
Current error: 0.000752537119744

Current iteration: 7038
Current error: 0.000735865507346

Current iteration: 7039
Current error: 0.000719428215603

Current iteration: 7040
Current error: 0.000703873113208

Current iteration: 7041
Current error: 0.000689376516918

Current iteration: 7042
Current error: 0.000674343933373

Current iteration: 7043
Current error: 0.000660078298802

Current iteration: 7044
Current error: 0.00064678436625

Current iteration: 7045
Current error: 0.000633166307356

Current iteration: 7046
Current error: 0.000620097635936

Current iteration: 7047
Current error: 0.000607581503909

Current iteration: 7048
Current error: 0.000595426930873

Current iteration: 7049
Current error: 0.000583691508198

Current iteration: 7050
Current error: 0.000572208111515

Current iteration: 7051
Current error: 0.000561186074127

Current iteration: 7052
Current error: 0.000550316402707

Current iteration: 7053
Current error: 0.000540084682104

Current iteration: 7054
Current error: 0.00052961185969

Current iteration: 7055
Current error: 0.000519813334744

Current iteration: 7056
Current error: 0.000510069046384

Current iteration: 7057
Current error: 0.000500721428185

Current iteration: 7058
Current error: 0.000491557661805

Current iteration: 7059
Current error: 0.000482717244509

Current iteration: 7060
Current error: 0.000474066967974

Current iteration: 7061
Current error: 0.000487239379574

Current iteration: 7062
Current error: 0.000457344354026

Current iteration: 7063
Current error: 0.000449326600712

Current iteration: 7064
Current error: 0.000446741992108

Current iteration: 7065
Current error: 0.000433999025231

Current iteration: 7066
Current error: 0.000426574551692

Current iteration: 7067
Current error: 0.00041939597466

Current iteration: 7068
Current error: 0.000412387569942

Current iteration: 7069
Current error: 0.000405556881616

Current iteration: 7070
Current error: 0.000399835333522

Current iteration: 7071
Current error: 0.000395625441073

Current iteration: 7072
Current error: 0.000385999294882

Current iteration: 7073
Current error: 0.000379746490242

Current iteration: 7074
Current error: 0.000373932839434

Current iteration: 7075
Current error: 0.000367786233139

Current iteration: 7076
Current error: 0.000361998420939

Current iteration: 7077
Current error: 0.000356363052877

Current iteration: 7078
Current error: 0.000350896915116

Current iteration: 7079
Current error: 0.00034547633837

Current iteration: 7080
Current error: 0.00034018780131

Current iteration: 7081
Current error: 0.000335161483683

Current iteration: 7082
Current error: 0.473363642706

Current iteration: 7083
Current error: 0.00057746639416

Current iteration: 7084
Current error: 0.466409059579

Current iteration: 7085
Current error: 0.000997645158348

Current iteration: 7086
Current error: 0.000960744641863

Current iteration: 7087
Current error: 0.000936902755027

Current iteration: 7088
Current error: 0.000913923405836

Current iteration: 7089
Current error: 0.000891806338183

Current iteration: 7090
Current error: 0.000870400521277

Current iteration: 7091
Current error: 0.000849768713028

Current iteration: 7092
Current error: 0.000829894651046

Current iteration: 7093
Current error: 0.000810584216862

Current iteration: 7094
Current error: 0.46071576036

Current iteration: 7095
Current error: 0.00140976657576

Current iteration: 7096
Current error: 0.00135346168755

Current iteration: 7097
Current error: 0.00129092962139

Current iteration: 7098
Current error: 0.00125434267458

Current iteration: 7099
Current error: 0.00121885392843

Current iteration: 7100
Current error: 0.00118516362512

Current iteration: 7101
Current error: 0.0011526043871

Current iteration: 7102
Current error: 0.00112136583097

Current iteration: 7103
Current error: 0.00109144720149

Current iteration: 7104
Current error: 0.00106267058716

Current iteration: 7105
Current error: 0.00103502725151

Current iteration: 7106
Current error: 0.00100867073458

Current iteration: 7107
Current error: 0.000982804579731

Current iteration: 7108
Current error: 0.000958357775498

Current iteration: 7109
Current error: 0.000934405340057

Current iteration: 7110
Current error: 0.000911766596359

Current iteration: 7111
Current error: 0.000896834107721

Current iteration: 7112
Current error: 0.000868006434803

Current iteration: 7113
Current error: 0.457973552415

Current iteration: 7114
Current error: 0.00145630454863

Current iteration: 7115
Current error: 0.447491117879

Current iteration: 7116
Current error: 0.00239585320829

Current iteration: 7117
Current error: 0.00230500413393

Current iteration: 7118
Current error: 0.00221924575146

Current iteration: 7119
Current error: 0.00213828817294

Current iteration: 7120
Current error: 0.00206736360381

Current iteration: 7121
Current error: 0.00198793940704

Current iteration: 7122
Current error: 0.00191871181202

Current iteration: 7123
Current error: 0.00185372135657

Current iteration: 7124
Current error: 0.00179053381287

Current iteration: 7125
Current error: 0.00173129565066

Current iteration: 7126
Current error: 0.00167459986589

Current iteration: 7127
Current error: 0.00162453021413

Current iteration: 7128
Current error: 0.00156928529996

Current iteration: 7129
Current error: 0.00152112348894

Current iteration: 7130
Current error: 0.00147349708463

Current iteration: 7131
Current error: 0.00142965248851

Current iteration: 7132
Current error: 0.00138615743375

Current iteration: 7133
Current error: 0.00134525234778

Current iteration: 7134
Current error: 0.00130624798446

Current iteration: 7135
Current error: 0.00126871297274

Current iteration: 7136
Current error: 0.00123280091328

Current iteration: 7137
Current error: 0.00119847964554

Current iteration: 7138
Current error: 0.00116538361889

Current iteration: 7139
Current error: 0.00114523023193

Current iteration: 7140
Current error: 0.00110327150576

Current iteration: 7141
Current error: 0.00107495545481

Current iteration: 7142
Current error: 0.00104597323392

Current iteration: 7143
Current error: 0.00101885794115

Current iteration: 7144
Current error: 0.000992832593165

Current iteration: 7145
Current error: 0.452020649374

Current iteration: 7146
Current error: 0.00163421815533

Current iteration: 7147
Current error: 0.00158230991944

Current iteration: 7148
Current error: 0.00153279080699

Current iteration: 7149
Current error: 0.00148531389406

Current iteration: 7150
Current error: 0.00144033999529

Current iteration: 7151
Current error: 0.00140267103109

Current iteration: 7152
Current error: 0.00135553874863

Current iteration: 7153
Current error: 0.00131607961387

Current iteration: 7154
Current error: 0.00128058125837

Current iteration: 7155
Current error: 0.00124211673816

Current iteration: 7156
Current error: 0.00120710532716

Current iteration: 7157
Current error: 0.0011739174271

Current iteration: 7158
Current error: 0.00114184258433

Current iteration: 7159
Current error: 0.001110938068

Current iteration: 7160
Current error: 0.00108141502234

Current iteration: 7161
Current error: 0.0010532809348

Current iteration: 7162
Current error: 0.0010257979511

Current iteration: 7163
Current error: 0.000999444774288

Current iteration: 7164
Current error: 0.000974186033018

Current iteration: 7165
Current error: 0.000950262082404

Current iteration: 7166
Current error: 0.000926783637819

Current iteration: 7167
Current error: 0.000903810338615

Current iteration: 7168
Current error: 0.000882108760883

Current iteration: 7169
Current error: 0.000860899082266

Current iteration: 7170
Current error: 0.000841809375538

Current iteration: 7171
Current error: 0.00082183625629

Current iteration: 7172
Current error: 0.000803299515193

Current iteration: 7173
Current error: 0.000803328726801

Current iteration: 7174
Current error: 0.000766922997055

Current iteration: 7175
Current error: 0.000751883191735

Current iteration: 7176
Current error: 0.000732342840498

Current iteration: 7177
Current error: 0.000716303504994

Current iteration: 7178
Current error: 0.000700823750859

Current iteration: 7179
Current error: 0.000685888016263

Current iteration: 7180
Current error: 0.000671347747283

Current iteration: 7181
Current error: 0.463960950151

Current iteration: 7182
Current error: 0.00114243692893

Current iteration: 7183
Current error: 0.00111035234916

Current iteration: 7184
Current error: 0.00108084918898

Current iteration: 7185
Current error: 0.00105350379605

Current iteration: 7186
Current error: 0.00102536576302

Current iteration: 7187
Current error: 0.000998967292289

Current iteration: 7188
Current error: 0.00097374153652

Current iteration: 7189
Current error: 0.000949797545689

Current iteration: 7190
Current error: 0.00100035353035

Current iteration: 7191
Current error: 0.000902729070349

Current iteration: 7192
Current error: 0.000894340695999

Current iteration: 7193
Current error: 0.000875553707429

Current iteration: 7194
Current error: 0.000839738122309

Current iteration: 7195
Current error: 0.000819869152988

Current iteration: 7196
Current error: 0.000800986605351

Current iteration: 7197
Current error: 0.457717811803

Current iteration: 7198
Current error: 0.00134052317522

Current iteration: 7199
Current error: 0.00129662203663

Current iteration: 7200
Current error: 0.00135789183274

Current iteration: 7201
Current error: 0.00122304221588

Current iteration: 7202
Current error: 0.00118922364091

Current iteration: 7203
Current error: 0.00115642797447

Current iteration: 7204
Current error: 0.00112521200596

Current iteration: 7205
Current error: 0.0010951156652

Current iteration: 7206
Current error: 0.00106616207607

Current iteration: 7207
Current error: 0.00103831228544

Current iteration: 7208
Current error: 0.00101155051874

Current iteration: 7209
Current error: 0.000985942171723

Current iteration: 7210
Current error: 0.000961088279536

Current iteration: 7211
Current error: 0.000949560163419

Current iteration: 7212
Current error: 0.452650632931

Current iteration: 7213
Current error: 0.00154244088454

Current iteration: 7214
Current error: 0.0014946140112

Current iteration: 7215
Current error: 0.00144930148066

Current iteration: 7216
Current error: 0.00140540913048

Current iteration: 7217
Current error: 0.00136368076911

Current iteration: 7218
Current error: 0.00132387361156

Current iteration: 7219
Current error: 0.00128560143273

Current iteration: 7220
Current error: 0.00124900850382

Current iteration: 7221
Current error: 0.00121392744179

Current iteration: 7222
Current error: 0.44999120344

Current iteration: 7223
Current error: 0.00200306766239

Current iteration: 7224
Current error: 0.00193142448826

Current iteration: 7225
Current error: 0.00186497611824

Current iteration: 7226
Current error: 0.00180205258818

Current iteration: 7227
Current error: 0.0017458474193

Current iteration: 7228
Current error: 0.00168489039547

Current iteration: 7229
Current error: 0.00164420107387

Current iteration: 7230
Current error: 0.00157856794599

Current iteration: 7231
Current error: 0.00152910853999

Current iteration: 7232
Current error: 0.44237850719

Current iteration: 7233
Current error: 0.00247890456935

Current iteration: 7234
Current error: 0.00238342695033

Current iteration: 7235
Current error: 0.00229334803272

Current iteration: 7236
Current error: 0.00220828285841

Current iteration: 7237
Current error: 0.432794883707

Current iteration: 7238
Current error: 0.00352425330542

Current iteration: 7239
Current error: 0.00343146355676

Current iteration: 7240
Current error: 0.00329397294809

Current iteration: 7241
Current error: 0.00307595002513

Current iteration: 7242
Current error: 0.00294541519378

Current iteration: 7243
Current error: 0.00282287197201

Current iteration: 7244
Current error: 0.00271258455847

Current iteration: 7245
Current error: 0.00259917520477

Current iteration: 7246
Current error: 0.00249697606746

Current iteration: 7247
Current error: 0.00240049461955

Current iteration: 7248
Current error: 0.00230950274055

Current iteration: 7249
Current error: 0.00222389574074

Current iteration: 7250
Current error: 0.00214194335609

Current iteration: 7251
Current error: 0.0020647795578

Current iteration: 7252
Current error: 0.00199162166995

Current iteration: 7253
Current error: 0.00192222435155

Current iteration: 7254
Current error: 0.437522925441

Current iteration: 7255
Current error: 0.00309612368725

Current iteration: 7256
Current error: 0.00296435705777

Current iteration: 7257
Current error: 0.00284731569916

Current iteration: 7258
Current error: 0.00272435482179

Current iteration: 7259
Current error: 0.0026159621354

Current iteration: 7260
Current error: 0.0025142142443

Current iteration: 7261
Current error: 0.00241446666269

Current iteration: 7262
Current error: 0.00232265998068

Current iteration: 7263
Current error: 0.00224810494007

Current iteration: 7264
Current error: 0.00215363262131

Current iteration: 7265
Current error: 0.00207580851392

Current iteration: 7266
Current error: 0.00200210080202

Current iteration: 7267
Current error: 0.00193225600156

Current iteration: 7268
Current error: 0.0019169746354

Current iteration: 7269
Current error: 0.0018022436961

Current iteration: 7270
Current error: 0.00174223653556

Current iteration: 7271
Current error: 0.00168519609052

Current iteration: 7272
Current error: 0.00163074884453

Current iteration: 7273
Current error: 0.00158044282916

Current iteration: 7274
Current error: 0.00152944245809

Current iteration: 7275
Current error: 0.00148271772477

Current iteration: 7276
Current error: 0.00143729137334

Current iteration: 7277
Current error: 0.446030020377

Current iteration: 7278
Current error: 0.00236391170107

Current iteration: 7279
Current error: 0.00226533753149

Current iteration: 7280
Current error: 0.427162769312

Current iteration: 7281
Current error: 0.00355944625307

Current iteration: 7282
Current error: 0.0033978094966

Current iteration: 7283
Current error: 0.0032484918834

Current iteration: 7284
Current error: 0.0031059905727

Current iteration: 7285
Current error: 0.00297369426571

Current iteration: 7286
Current error: 0.00284929561766

Current iteration: 7287
Current error: 0.00273429961131

Current iteration: 7288
Current error: 0.00262262781445

Current iteration: 7289
Current error: 0.00251910739909

Current iteration: 7290
Current error: 0.00242189568392

Current iteration: 7291
Current error: 0.0023291606518

Current iteration: 7292
Current error: 0.00224875768825

Current iteration: 7293
Current error: 0.428628859669

Current iteration: 7294
Current error: 0.00355440660296

Current iteration: 7295
Current error: 0.00337608622275

Current iteration: 7296
Current error: 0.00322847117577

Current iteration: 7297
Current error: 0.00308718371376

Current iteration: 7298
Current error: 0.00295583794548

Current iteration: 7299
Current error: 0.00283272405621

Current iteration: 7300
Current error: 0.00271699566924

Current iteration: 7301
Current error: 0.00260793465565

Current iteration: 7302
Current error: 0.00250793956957

Current iteration: 7303
Current error: 0.00240912592784

Current iteration: 7304
Current error: 0.00232061233307

Current iteration: 7305
Current error: 0.00223027978626

Current iteration: 7306
Current error: 0.00214844223817

Current iteration: 7307
Current error: 0.00207096655657

Current iteration: 7308
Current error: 0.00199749127281

Current iteration: 7309
Current error: 0.00192780620361

Current iteration: 7310
Current error: 0.00186171270333

Current iteration: 7311
Current error: 0.00179912872061

Current iteration: 7312
Current error: 0.00173892124546

Current iteration: 7313
Current error: 0.00168197867253

Current iteration: 7314
Current error: 0.00162784045149

Current iteration: 7315
Current error: 0.00157613032118

Current iteration: 7316
Current error: 0.00153942431663

Current iteration: 7317
Current error: 0.00147966927735

Current iteration: 7318
Current error: 0.00143472124392

Current iteration: 7319
Current error: 0.0013917496639

Current iteration: 7320
Current error: 0.00135222521085

Current iteration: 7321
Current error: 0.00131141153999

Current iteration: 7322
Current error: 0.00127357738752

Current iteration: 7323
Current error: 0.00123746950284

Current iteration: 7324
Current error: 0.00120284976677

Current iteration: 7325
Current error: 0.00122798098533

Current iteration: 7326
Current error: 0.00113730393158

Current iteration: 7327
Current error: 0.00110674551871

Current iteration: 7328
Current error: 0.00107739309548

Current iteration: 7329
Current error: 0.00104913456225

Current iteration: 7330
Current error: 0.00102466418838

Current iteration: 7331
Current error: 0.000995949741144

Current iteration: 7332
Current error: 0.000970847623273

Current iteration: 7333
Current error: 0.000946490830674

Current iteration: 7334
Current error: 0.000932613003852

Current iteration: 7335
Current error: 0.000900639603756

Current iteration: 7336
Current error: 0.454511988629

Current iteration: 7337
Current error: 0.00149731598952

Current iteration: 7338
Current error: 0.00144482768277

Current iteration: 7339
Current error: 0.00140143997565

Current iteration: 7340
Current error: 0.001360114281

Current iteration: 7341
Current error: 0.00132020899187

Current iteration: 7342
Current error: 0.00128220123588

Current iteration: 7343
Current error: 0.00124722674098

Current iteration: 7344
Current error: 0.0012107136658

Current iteration: 7345
Current error: 0.00117722750861

Current iteration: 7346
Current error: 0.00114505323022

Current iteration: 7347
Current error: 0.00111423468002

Current iteration: 7348
Current error: 0.00108451275745

Current iteration: 7349
Current error: 0.00105654937808

Current iteration: 7350
Current error: 0.00102869074951

Current iteration: 7351
Current error: 0.00100228422834

Current iteration: 7352
Current error: 0.000977902797968

Current iteration: 7353
Current error: 0.000952415902101

Current iteration: 7354
Current error: 0.451603288087

Current iteration: 7355
Current error: 0.00156268088948

Current iteration: 7356
Current error: 0.00151402493768

Current iteration: 7357
Current error: 0.00146756827452

Current iteration: 7358
Current error: 0.00144244380788

Current iteration: 7359
Current error: 0.00138058188271

Current iteration: 7360
Current error: 0.00136697929127

Current iteration: 7361
Current error: 0.44733106833

Current iteration: 7362
Current error: 0.00219857247698

Current iteration: 7363
Current error: 0.00212736909761

Current iteration: 7364
Current error: 0.436244203362

Current iteration: 7365
Current error: 0.00341376424717

Current iteration: 7366
Current error: 0.00326216195397

Current iteration: 7367
Current error: 0.00311984460588

Current iteration: 7368
Current error: 0.424834151907

Current iteration: 7369
Current error: 0.00493193238777

Current iteration: 7370
Current error: 0.00467443957022

Current iteration: 7371
Current error: 0.00443845781397

Current iteration: 7372
Current error: 0.00421487942627

Current iteration: 7373
Current error: 0.00400939988858

Current iteration: 7374
Current error: 0.00381988008183

Current iteration: 7375
Current error: 0.00363982661624

Current iteration: 7376
Current error: 0.00347378163299

Current iteration: 7377
Current error: 0.00331798222458

Current iteration: 7378
Current error: 0.00318073608813

Current iteration: 7379
Current error: 0.00303581553125

Current iteration: 7380
Current error: 0.00290781205814

Current iteration: 7381
Current error: 0.00278770805652

Current iteration: 7382
Current error: 0.00270016744941

Current iteration: 7383
Current error: 0.00256778005711

Current iteration: 7384
Current error: 0.00246718084041

Current iteration: 7385
Current error: 0.0023724739342

Current iteration: 7386
Current error: 0.429625769473

Current iteration: 7387
Current error: 0.00376134081867

Current iteration: 7388
Current error: 0.00358685128348

Current iteration: 7389
Current error: 0.00342390379304

Current iteration: 7390
Current error: 0.421893846231

Current iteration: 7391
Current error: 0.00539682014263

Current iteration: 7392
Current error: 0.00509798625955

Current iteration: 7393
Current error: 0.00484256247701

Current iteration: 7394
Current error: 0.00457323787955

Current iteration: 7395
Current error: 0.00434268048212

Current iteration: 7396
Current error: 0.0041277422602

Current iteration: 7397
Current error: 0.00392828526029

Current iteration: 7398
Current error: 0.00377512313947

Current iteration: 7399
Current error: 0.0036615401672

Current iteration: 7400
Current error: 0.00340601039318

Current iteration: 7401
Current error: 0.00333027098055

Current iteration: 7402
Current error: 0.0031122880418

Current iteration: 7403
Current error: 0.00298297294405

Current iteration: 7404
Current error: 0.423444774343

Current iteration: 7405
Current error: 0.00468048857511

Current iteration: 7406
Current error: 0.0044523578514

Current iteration: 7407
Current error: 0.0042195569001

Current iteration: 7408
Current error: 0.00401362457281

Current iteration: 7409
Current error: 0.00382213036491

Current iteration: 7410
Current error: 0.00364364779147

Current iteration: 7411
Current error: 0.00347700074355

Current iteration: 7412
Current error: 0.00332154148527

Current iteration: 7413
Current error: 0.00318403454676

Current iteration: 7414
Current error: 0.00303941089254

Current iteration: 7415
Current error: 0.00291056472628

Current iteration: 7416
Current error: 0.00279016017366

Current iteration: 7417
Current error: 0.00267682230915

Current iteration: 7418
Current error: 0.00257158506496

Current iteration: 7419
Current error: 0.00247080512283

Current iteration: 7420
Current error: 0.00237468034585

Current iteration: 7421
Current error: 0.433041935727

Current iteration: 7422
Current error: 0.399579325402

Current iteration: 7423
Current error: 0.00596482372261

Current iteration: 7424
Current error: 0.00562696181892

Current iteration: 7425
Current error: 0.00531563445967

Current iteration: 7426
Current error: 0.00503386438037

Current iteration: 7427
Current error: 0.00476433568847

Current iteration: 7428
Current error: 0.395551920569

Current iteration: 7429
Current error: 0.00708863286404

Current iteration: 7430
Current error: 0.006656560668

Current iteration: 7431
Current error: 0.00626172732949

Current iteration: 7432
Current error: 0.00589909950759

Current iteration: 7433
Current error: 0.385320848882

Current iteration: 7434
Current error: 0.00861297142656

Current iteration: 7435
Current error: 0.00804424737011

Current iteration: 7436
Current error: 0.00752841362008

Current iteration: 7437
Current error: 0.00705791200103

Current iteration: 7438
Current error: 0.0066287035349

Current iteration: 7439
Current error: 0.00623615601214

Current iteration: 7440
Current error: 0.00587622403375

Current iteration: 7441
Current error: 0.00559346060205

Current iteration: 7442
Current error: 0.00524098599815

Current iteration: 7443
Current error: 0.00495978299538

Current iteration: 7444
Current error: 0.00470008878845

Current iteration: 7445
Current error: 0.00462893366068

Current iteration: 7446
Current error: 0.00423632193125

Current iteration: 7447
Current error: 0.00402797570726

Current iteration: 7448
Current error: 0.411509263107

Current iteration: 7449
Current error: 0.00619208147814

Current iteration: 7450
Current error: 0.0058356373854

Current iteration: 7451
Current error: 0.00550834014522

Current iteration: 7452
Current error: 0.0052217209487

Current iteration: 7453
Current error: 0.00492824097313

Current iteration: 7454
Current error: 0.00467114629654

Current iteration: 7455
Current error: 0.00443292468332

Current iteration: 7456
Current error: 0.00432778741651

Current iteration: 7457
Current error: 0.00401268739236

Current iteration: 7458
Current error: 0.00381389401379

Current iteration: 7459
Current error: 0.00363597134971

Current iteration: 7460
Current error: 0.0034700281669

Current iteration: 7461
Current error: 0.00331463684338

Current iteration: 7462
Current error: 0.00316920081399

Current iteration: 7463
Current error: 0.00303298174809

Current iteration: 7464
Current error: 0.00290678991698

Current iteration: 7465
Current error: 0.00278515517594

Current iteration: 7466
Current error: 0.00267212036241

Current iteration: 7467
Current error: 0.00268764200304

Current iteration: 7468
Current error: 0.00246386406372

Current iteration: 7469
Current error: 0.00236919879088

Current iteration: 7470
Current error: 0.00227999215219

Current iteration: 7471
Current error: 0.00219543685828

Current iteration: 7472
Current error: 0.429845300711

Current iteration: 7473
Current error: 0.00347586115474

Current iteration: 7474
Current error: 0.00332061948164

Current iteration: 7475
Current error: 0.00317467200794

Current iteration: 7476
Current error: 0.00303799078398

Current iteration: 7477
Current error: 0.00327483058088

Current iteration: 7478
Current error: 0.00278452732245

Current iteration: 7479
Current error: 0.00267164565966

Current iteration: 7480
Current error: 0.00256567890821

Current iteration: 7481
Current error: 0.00246515371965

Current iteration: 7482
Current error: 0.00237038007242

Current iteration: 7483
Current error: 0.00228223499947

Current iteration: 7484
Current error: 0.00219656401212

Current iteration: 7485
Current error: 0.00211639740271

Current iteration: 7486
Current error: 0.00204052796949

Current iteration: 7487
Current error: 0.00196871636312

Current iteration: 7488
Current error: 0.00190041259495

Current iteration: 7489
Current error: 0.00183940032416

Current iteration: 7490
Current error: 0.00177405877287

Current iteration: 7491
Current error: 0.00171544574114

Current iteration: 7492
Current error: 0.00165956214562

Current iteration: 7493
Current error: 0.00160654674081

Current iteration: 7494
Current error: 0.00155672565392

Current iteration: 7495
Current error: 0.00150746575446

Current iteration: 7496
Current error: 0.00146111116998

Current iteration: 7497
Current error: 0.00142647852698

Current iteration: 7498
Current error: 0.00137563247324

Current iteration: 7499
Current error: 0.0013343153551

Current iteration: 7500
Current error: 0.00135237091997

Current iteration: 7501
Current error: 0.00125812346244

Current iteration: 7502
Current error: 0.00122270520762

Current iteration: 7503
Current error: 0.00118864797289

Current iteration: 7504
Current error: 0.00115670143397

Current iteration: 7505
Current error: 0.00116119448798

Current iteration: 7506
Current error: 0.00109436973981

Current iteration: 7507
Current error: 0.00106572704155

Current iteration: 7508
Current error: 0.00103768081534

Current iteration: 7509
Current error: 0.00101107928133

Current iteration: 7510
Current error: 0.000985239094914

Current iteration: 7511
Current error: 0.000961830888943

Current iteration: 7512
Current error: 0.000936679058956

Current iteration: 7513
Current error: 0.000913656186529

Current iteration: 7514
Current error: 0.00089165975469

Current iteration: 7515
Current error: 0.000870125410135

Current iteration: 7516
Current error: 0.000849524686207

Current iteration: 7517
Current error: 0.000829618621311

Current iteration: 7518
Current error: 0.000810404908172

Current iteration: 7519
Current error: 0.000792212591884

Current iteration: 7520
Current error: 0.000773868543937

Current iteration: 7521
Current error: 0.00075654160728

Current iteration: 7522
Current error: 0.000739803261844

Current iteration: 7523
Current error: 0.000723525906751

Current iteration: 7524
Current error: 0.000708566694343

Current iteration: 7525
Current error: 0.000692596632265

Current iteration: 7526
Current error: 0.000677883743872

Current iteration: 7527
Current error: 0.000663631669961

Current iteration: 7528
Current error: 0.000649854488765

Current iteration: 7529
Current error: 0.000636388838431

Current iteration: 7530
Current error: 0.000623400147221

Current iteration: 7531
Current error: 0.000610765217173

Current iteration: 7532
Current error: 0.000598636379722

Current iteration: 7533
Current error: 0.000586638899896

Current iteration: 7534
Current error: 0.000575135658326

Current iteration: 7535
Current error: 0.00056393855804

Current iteration: 7536
Current error: 0.000553043557323

Current iteration: 7537
Current error: 0.00054251009629

Current iteration: 7538
Current error: 0.000532666369604

Current iteration: 7539
Current error: 0.000524100440081

Current iteration: 7540
Current error: 0.000522772010779

Current iteration: 7541
Current error: 0.000503004550267

Current iteration: 7542
Current error: 0.000493839675903

Current iteration: 7543
Current error: 0.00048488317671

Current iteration: 7544
Current error: 0.462438066543

Current iteration: 7545
Current error: 0.000807009874672

Current iteration: 7546
Current error: 0.000788587715584

Current iteration: 7547
Current error: 0.000770704024797

Current iteration: 7548
Current error: 0.000808455890226

Current iteration: 7549
Current error: 0.000736487838564

Current iteration: 7550
Current error: 0.000734633884556

Current iteration: 7551
Current error: 0.000704506759868

Current iteration: 7552
Current error: 0.000689363772719

Current iteration: 7553
Current error: 0.000675233431876

Current iteration: 7554
Current error: 0.000660547385782

Current iteration: 7555
Current error: 0.000650860074276

Current iteration: 7556
Current error: 0.000633754226142

Current iteration: 7557
Current error: 0.000620678677919

Current iteration: 7558
Current error: 0.000608103049454

Current iteration: 7559
Current error: 0.000595892980379

Current iteration: 7560
Current error: 0.000584172274506

Current iteration: 7561
Current error: 0.000624453836073

Current iteration: 7562
Current error: 0.00056116057248

Current iteration: 7563
Current error: 0.464039567422

Current iteration: 7564
Current error: 0.000953374644447

Current iteration: 7565
Current error: 0.000922911473742

Current iteration: 7566
Current error: 0.000900443848264

Current iteration: 7567
Current error: 0.000878820391136

Current iteration: 7568
Current error: 0.000858455914595

Current iteration: 7569
Current error: 0.457687827546

Current iteration: 7570
Current error: 0.00143566506897

Current iteration: 7571
Current error: 0.00139415985575

Current iteration: 7572
Current error: 0.00135579132721

Current iteration: 7573
Current error: 0.00131258790859

Current iteration: 7574
Current error: 0.00127445612187

Current iteration: 7575
Current error: 0.446645324427

Current iteration: 7576
Current error: 0.00208147174383

Current iteration: 7577
Current error: 0.00200747242794

Current iteration: 7578
Current error: 0.00193731937368

Current iteration: 7579
Current error: 0.00187065356388

Current iteration: 7580
Current error: 0.00180730272511

Current iteration: 7581
Current error: 0.00174738075969

Current iteration: 7582
Current error: 0.00168974113129

Current iteration: 7583
Current error: 0.00163516101072

Current iteration: 7584
Current error: 0.0016069996388

Current iteration: 7585
Current error: 0.00153326315508

Current iteration: 7586
Current error: 0.00148594994427

Current iteration: 7587
Current error: 0.433196647025

Current iteration: 7588
Current error: 0.00234710701845

Current iteration: 7589
Current error: 0.00225510603036

Current iteration: 7590
Current error: 0.00217141912139

Current iteration: 7591
Current error: 0.00209770475424

Current iteration: 7592
Current error: 0.00201804859892

Current iteration: 7593
Current error: 0.00194733772497

Current iteration: 7594
Current error: 0.00188015487524

Current iteration: 7595
Current error: 0.00181638321714

Current iteration: 7596
Current error: 0.00175993332911

Current iteration: 7597
Current error: 0.00169794081893

Current iteration: 7598
Current error: 0.00164355667197

Current iteration: 7599
Current error: 0.0016871135651

Current iteration: 7600
Current error: 0.001539557343

Current iteration: 7601
Current error: 0.00149247762689

Current iteration: 7602
Current error: 0.00144646566251

Current iteration: 7603
Current error: 0.00140290630393

Current iteration: 7604
Current error: 0.00136195667156

Current iteration: 7605
Current error: 0.00132153642875

Current iteration: 7606
Current error: 0.00128345430422

Current iteration: 7607
Current error: 0.00124700166296

Current iteration: 7608
Current error: 0.00121202997967

Current iteration: 7609
Current error: 0.00117846183457

Current iteration: 7610
Current error: 0.00114704990205

Current iteration: 7611
Current error: 0.00111527252256

Current iteration: 7612
Current error: 0.00108593830725

Current iteration: 7613
Current error: 0.00105714230597

Current iteration: 7614
Current error: 0.00102973506189

Current iteration: 7615
Current error: 0.00100455615218

Current iteration: 7616
Current error: 0.456415337744

Current iteration: 7617
Current error: 0.00168203718712

Current iteration: 7618
Current error: 0.00163914756852

Current iteration: 7619
Current error: 0.00157615693043

Current iteration: 7620
Current error: 0.00152680642565

Current iteration: 7621
Current error: 0.00147981395085

Current iteration: 7622
Current error: 0.00143473781293

Current iteration: 7623
Current error: 0.00139175580343

Current iteration: 7624
Current error: 0.00135070560934

Current iteration: 7625
Current error: 0.00131169823892

Current iteration: 7626
Current error: 0.0012736033529

Current iteration: 7627
Current error: 0.0012375123162

Current iteration: 7628
Current error: 0.00121138226567

Current iteration: 7629
Current error: 0.00116970698755

Current iteration: 7630
Current error: 0.00113782672704

Current iteration: 7631
Current error: 0.00110725578958

Current iteration: 7632
Current error: 0.00107811821474

Current iteration: 7633
Current error: 0.00104962375536

Current iteration: 7634
Current error: 0.00102267250079

Current iteration: 7635
Current error: 0.0010034922819

Current iteration: 7636
Current error: 0.00097106027566

Current iteration: 7637
Current error: 0.000946825687167

Current iteration: 7638
Current error: 0.000954584072554

Current iteration: 7639
Current error: 0.000900927501972

Current iteration: 7640
Current error: 0.000879017714704

Current iteration: 7641
Current error: 0.000858114503452

Current iteration: 7642
Current error: 0.000838082711658

Current iteration: 7643
Current error: 0.000818395424389

Current iteration: 7644
Current error: 0.000799578986583

Current iteration: 7645
Current error: 0.000781356166333

Current iteration: 7646
Current error: 0.456970647149

Current iteration: 7647
Current error: 0.00129818348703

Current iteration: 7648
Current error: 0.001261076612

Current iteration: 7649
Current error: 0.449082304122

Current iteration: 7650
Current error: 0.00207647466015

Current iteration: 7651
Current error: 0.428268921525

Current iteration: 7652
Current error: 0.00326706549552

Current iteration: 7653
Current error: 0.00312480961239

Current iteration: 7654
Current error: 0.00299128168629

Current iteration: 7655
Current error: 0.00286934705763

Current iteration: 7656
Current error: 0.426648355768

Current iteration: 7657
Current error: 0.0045389942139

Current iteration: 7658
Current error: 0.00431044677075

Current iteration: 7659
Current error: 0.00410398339018

Current iteration: 7660
Current error: 0.00390157659406

Current iteration: 7661
Current error: 0.00371695460612

Current iteration: 7662
Current error: 0.00354569040415

Current iteration: 7663
Current error: 0.00338536642345

Current iteration: 7664
Current error: 0.00323539173717

Current iteration: 7665
Current error: 0.00309511435486

Current iteration: 7666
Current error: 0.00296368624461

Current iteration: 7667
Current error: 0.00283981131891

Current iteration: 7668
Current error: 0.00272355018264

Current iteration: 7669
Current error: 0.42998252642

Current iteration: 7670
Current error: 0.00434883101502

Current iteration: 7671
Current error: 0.00413393893099

Current iteration: 7672
Current error: 0.00393423367828

Current iteration: 7673
Current error: 0.0037481118587

Current iteration: 7674
Current error: 0.00357439691728

Current iteration: 7675
Current error: 0.00341930389118

Current iteration: 7676
Current error: 0.00326069735398

Current iteration: 7677
Current error: 0.00311876495015

Current iteration: 7678
Current error: 0.00298576371339

Current iteration: 7679
Current error: 0.00286075482521

Current iteration: 7680
Current error: 0.00274319170148

Current iteration: 7681
Current error: 0.00263279146513

Current iteration: 7682
Current error: 0.00252850771051

Current iteration: 7683
Current error: 0.00243034740468

Current iteration: 7684
Current error: 0.00233761082822

Current iteration: 7685
Current error: 0.00224998364703

Current iteration: 7686
Current error: 0.00216780539941

Current iteration: 7687
Current error: 0.00208919682847

Current iteration: 7688
Current error: 0.00201440532473

Current iteration: 7689
Current error: 0.00194375608951

Current iteration: 7690
Current error: 0.00187678943925

Current iteration: 7691
Current error: 0.00181311284494

Current iteration: 7692
Current error: 0.00175260736071

Current iteration: 7693
Current error: 0.00169503106936

Current iteration: 7694
Current error: 0.00166435865293

Current iteration: 7695
Current error: 0.430623843663

Current iteration: 7696
Current error: 0.00258235295

Current iteration: 7697
Current error: 0.00248192226579

Current iteration: 7698
Current error: 0.00242115087814

Current iteration: 7699
Current error: 0.00229976155454

Current iteration: 7700
Current error: 0.00220920951567

Current iteration: 7701
Current error: 0.00212851470388

Current iteration: 7702
Current error: 0.00205217030418

Current iteration: 7703
Current error: 0.00197975700526

Current iteration: 7704
Current error: 0.00191080533176

Current iteration: 7705
Current error: 0.00184545919464

Current iteration: 7706
Current error: 0.00178344071478

Current iteration: 7707
Current error: 0.00172432225723

Current iteration: 7708
Current error: 0.00166817958771

Current iteration: 7709
Current error: 0.00162561533392

Current iteration: 7710
Current error: 0.00156331741119

Current iteration: 7711
Current error: 0.00151491172103

Current iteration: 7712
Current error: 0.00147124123191

Current iteration: 7713
Current error: 0.0014236381426

Current iteration: 7714
Current error: 0.00138111003401

Current iteration: 7715
Current error: 0.00134048272657

Current iteration: 7716
Current error: 0.00130160645814

Current iteration: 7717
Current error: 0.0012652737431

Current iteration: 7718
Current error: 0.00122860075477

Current iteration: 7719
Current error: 0.0011944161081

Current iteration: 7720
Current error: 0.00116151531152

Current iteration: 7721
Current error: 0.00113009291658

Current iteration: 7722
Current error: 0.00109988973395

Current iteration: 7723
Current error: 0.00107098026304

Current iteration: 7724
Current error: 0.00104273901308

Current iteration: 7725
Current error: 0.00101573762686

Current iteration: 7726
Current error: 0.000989888538581

Current iteration: 7727
Current error: 0.000964919052489

Current iteration: 7728
Current error: 0.000948104596238

Current iteration: 7729
Current error: 0.000917756459774

Current iteration: 7730
Current error: 0.000896183534092

Current iteration: 7731
Current error: 0.000873926066335

Current iteration: 7732
Current error: 0.000861225803852

Current iteration: 7733
Current error: 0.000833140719179

Current iteration: 7734
Current error: 0.000813791951167

Current iteration: 7735
Current error: 0.000795068064788

Current iteration: 7736
Current error: 0.000777036623942

Current iteration: 7737
Current error: 0.000759548153502

Current iteration: 7738
Current error: 0.000743287367563

Current iteration: 7739
Current error: 0.000726588988502

Current iteration: 7740
Current error: 0.00071437574487

Current iteration: 7741
Current error: 0.444663000252

Current iteration: 7742
Current error: 0.00113000553104

Current iteration: 7743
Current error: 0.0010999444113

Current iteration: 7744
Current error: 0.00107056979587

Current iteration: 7745
Current error: 0.00107852900913

Current iteration: 7746
Current error: 0.00101565571247

Current iteration: 7747
Current error: 0.453635776204

Current iteration: 7748
Current error: 0.43274636514

Current iteration: 7749
Current error: 0.0027734591641

Current iteration: 7750
Current error: 0.00265729654468

Current iteration: 7751
Current error: 0.00255237029492

Current iteration: 7752
Current error: 0.0024513369373

Current iteration: 7753
Current error: 0.00237013639944

Current iteration: 7754
Current error: 0.00226892561846

Current iteration: 7755
Current error: 0.00218660390469

Current iteration: 7756
Current error: 0.00210552540167

Current iteration: 7757
Current error: 0.0020301047322

Current iteration: 7758
Current error: 0.00195903911521

Current iteration: 7759
Current error: 0.00189114709583

Current iteration: 7760
Current error: 0.00182666003743

Current iteration: 7761
Current error: 0.00176895742167

Current iteration: 7762
Current error: 0.00170727017604

Current iteration: 7763
Current error: 0.0016518505372

Current iteration: 7764
Current error: 0.0015991307103

Current iteration: 7765
Current error: 0.00154866412568

Current iteration: 7766
Current error: 0.00168213714425

Current iteration: 7767
Current error: 0.00145280867989

Current iteration: 7768
Current error: 0.00140904194771

Current iteration: 7769
Current error: 0.440269216585

Current iteration: 7770
Current error: 0.00226594845259

Current iteration: 7771
Current error: 0.00222025080708

Current iteration: 7772
Current error: 0.00211651289583

Current iteration: 7773
Current error: 0.00202749706068

Current iteration: 7774
Current error: 0.00207186174267

Current iteration: 7775
Current error: 0.00188708842471

Current iteration: 7776
Current error: 0.00182291158426

Current iteration: 7777
Current error: 0.00176194932796

Current iteration: 7778
Current error: 0.0017039437896

Current iteration: 7779
Current error: 0.00164897601966

Current iteration: 7780
Current error: 0.00159598076175

Current iteration: 7781
Current error: 0.00154589251123

Current iteration: 7782
Current error: 0.00149998441255

Current iteration: 7783
Current error: 0.00145258184146

Current iteration: 7784
Current error: 0.00140832615625

Current iteration: 7785
Current error: 0.00136651734871

Current iteration: 7786
Current error: 0.00132647597105

Current iteration: 7787
Current error: 0.00128823787341

Current iteration: 7788
Current error: 0.00125148389541

Current iteration: 7789
Current error: 0.00121704192779

Current iteration: 7790
Current error: 0.00118260563036

Current iteration: 7791
Current error: 0.00115035907259

Current iteration: 7792
Current error: 0.001120735068

Current iteration: 7793
Current error: 0.00108925192754

Current iteration: 7794
Current error: 0.001060600303

Current iteration: 7795
Current error: 0.00103300045497

Current iteration: 7796
Current error: 0.00100647245871

Current iteration: 7797
Current error: 0.000980922938636

Current iteration: 7798
Current error: 0.000957102228585

Current iteration: 7799
Current error: 0.000943083967473

Current iteration: 7800
Current error: 0.00090973033347

Current iteration: 7801
Current error: 0.000888215028331

Current iteration: 7802
Current error: 0.000866491813196

Current iteration: 7803
Current error: 0.000845973859121

Current iteration: 7804
Current error: 0.000826383208894

Current iteration: 7805
Current error: 0.000807104543301

Current iteration: 7806
Current error: 0.00078862873938

Current iteration: 7807
Current error: 0.0007709872529

Current iteration: 7808
Current error: 0.000753607736641

Current iteration: 7809
Current error: 0.00073684675607

Current iteration: 7810
Current error: 0.000720738531605

Current iteration: 7811
Current error: 0.000705113383863

Current iteration: 7812
Current error: 0.000690081052746

Current iteration: 7813
Current error: 0.453541177412

Current iteration: 7814
Current error: 0.0011279523512

Current iteration: 7815
Current error: 0.00109768443424

Current iteration: 7816
Current error: 0.00106878362622

Current iteration: 7817
Current error: 0.00104516297022

Current iteration: 7818
Current error: 0.00101398241055

Current iteration: 7819
Current error: 0.000996476047548

Current iteration: 7820
Current error: 0.000963134746451

Current iteration: 7821
Current error: 0.000939331828044

Current iteration: 7822
Current error: 0.000916124460221

Current iteration: 7823
Current error: 0.000894845759354

Current iteration: 7824
Current error: 0.000872526385004

Current iteration: 7825
Current error: 0.000851732403514

Current iteration: 7826
Current error: 0.000831985138363

Current iteration: 7827
Current error: 0.000813174563347

Current iteration: 7828
Current error: 0.000793926518275

Current iteration: 7829
Current error: 0.000775919381619

Current iteration: 7830
Current error: 0.000770969243568

Current iteration: 7831
Current error: 0.000814762946295

Current iteration: 7832
Current error: 0.000725499722129

Current iteration: 7833
Current error: 0.000708833280185

Current iteration: 7834
Current error: 0.000693588215634

Current iteration: 7835
Current error: 0.00068261173707

Current iteration: 7836
Current error: 0.000707983115656

Current iteration: 7837
Current error: 0.000650405399873

Current iteration: 7838
Current error: 0.000640585879997

Current iteration: 7839
Current error: 0.000624092700942

Current iteration: 7840
Current error: 0.000611581962292

Current iteration: 7841
Current error: 0.000598977730872

Current iteration: 7842
Current error: 0.000598772986709

Current iteration: 7843
Current error: 0.000575562024241

Current iteration: 7844
Current error: 0.000564309061125

Current iteration: 7845
Current error: 0.000553756593603

Current iteration: 7846
Current error: 0.000542843358091

Current iteration: 7847
Current error: 0.000532527990484

Current iteration: 7848
Current error: 0.000522594381021

Current iteration: 7849
Current error: 0.000512811375816

Current iteration: 7850
Current error: 0.000503375627644

Current iteration: 7851
Current error: 0.000545555988915

Current iteration: 7852
Current error: 0.000484917556068

Current iteration: 7853
Current error: 0.00047618872

Current iteration: 7854
Current error: 0.46957516

Current iteration: 7855
Current error: 0.444269426458

Current iteration: 7856
Current error: 0.00134245676781

Current iteration: 7857
Current error: 0.00130349066636

Current iteration: 7858
Current error: 0.00126601092098

Current iteration: 7859
Current error: 0.0012302637601

Current iteration: 7860
Current error: 0.00119594062037

Current iteration: 7861
Current error: 0.00116297054819

Current iteration: 7862
Current error: 0.00114367817233

Current iteration: 7863
Current error: 0.438728077634

Current iteration: 7864
Current error: 0.00179846964229

Current iteration: 7865
Current error: 0.00173867425935

Current iteration: 7866
Current error: 0.00168822318389

Current iteration: 7867
Current error: 0.00162748055424

Current iteration: 7868
Current error: 0.00157616416137

Current iteration: 7869
Current error: 0.00152651095912

Current iteration: 7870
Current error: 0.00147948499508

Current iteration: 7871
Current error: 0.00143452638115

Current iteration: 7872
Current error: 0.00139167533804

Current iteration: 7873
Current error: 0.00136116672813

Current iteration: 7874
Current error: 0.00131264383458

Current iteration: 7875
Current error: 0.00127376300701

Current iteration: 7876
Current error: 0.00123724919931

Current iteration: 7877
Current error: 0.00121078363928

Current iteration: 7878
Current error: 0.444859133035

Current iteration: 7879
Current error: 0.0019512307591

Current iteration: 7880
Current error: 0.00188455304318

Current iteration: 7881
Current error: 0.00181980769149

Current iteration: 7882
Current error: 0.00175893567517

Current iteration: 7883
Current error: 0.0017058055372

Current iteration: 7884
Current error: 0.00164581442005

Current iteration: 7885
Current error: 0.00159349711751

Current iteration: 7886
Current error: 0.00154322393464

Current iteration: 7887
Current error: 0.00149542802264

Current iteration: 7888
Current error: 0.439193616032

Current iteration: 7889
Current error: 0.00240278638175

Current iteration: 7890
Current error: 0.00231212441311

Current iteration: 7891
Current error: 0.00222530538573

Current iteration: 7892
Current error: 0.00215782362583

Current iteration: 7893
Current error: 0.436326763139

Current iteration: 7894
Current error: 0.00345963154221

Current iteration: 7895
Current error: 0.00330503428652

Current iteration: 7896
Current error: 0.00316038557336

Current iteration: 7897
Current error: 0.00302454777951

Current iteration: 7898
Current error: 0.00289725508213

Current iteration: 7899
Current error: 0.00277761078993

Current iteration: 7900
Current error: 0.00266608907152

Current iteration: 7901
Current error: 0.00292067141626

Current iteration: 7902
Current error: 0.0024543644632

Current iteration: 7903
Current error: 0.432263907611

Current iteration: 7904
Current error: 0.0039312780922

Current iteration: 7905
Current error: 0.00374536433932

Current iteration: 7906
Current error: 0.003571984307

Current iteration: 7907
Current error: 0.00341007254757

Current iteration: 7908
Current error: 0.00325875306087

Current iteration: 7909
Current error: 0.423372612618

Current iteration: 7910
Current error: 0.00630259723277

Current iteration: 7911
Current error: 0.00484538127772

Current iteration: 7912
Current error: 0.00461815148071

Current iteration: 7913
Current error: 0.0044059761459

Current iteration: 7914
Current error: 0.0041448361202

Current iteration: 7915
Current error: 0.0039613328041

Current iteration: 7916
Current error: 0.00375707640666

Current iteration: 7917
Current error: 0.00358291189069

Current iteration: 7918
Current error: 0.00342043710203

Current iteration: 7919
Current error: 0.00326860919115

Current iteration: 7920
Current error: 0.00312586463026

Current iteration: 7921
Current error: 0.00299223777013

Current iteration: 7922
Current error: 0.00286688974435

Current iteration: 7923
Current error: 0.00274903052159

Current iteration: 7924
Current error: 0.00282374865395

Current iteration: 7925
Current error: 0.00253165338673

Current iteration: 7926
Current error: 0.00243285832821

Current iteration: 7927
Current error: 0.00234006514808

Current iteration: 7928
Current error: 0.00225293655001

Current iteration: 7929
Current error: 0.00216925727511

Current iteration: 7930
Current error: 0.00209069768106

Current iteration: 7931
Current error: 0.00208977626089

Current iteration: 7932
Current error: 0.00194688997944

Current iteration: 7933
Current error: 0.00187779080086

Current iteration: 7934
Current error: 0.435356673912

Current iteration: 7935
Current error: 0.405088523306

Current iteration: 7936
Current error: 0.00473707563325

Current iteration: 7937
Current error: 0.00449402711998

Current iteration: 7938
Current error: 0.410768972178

Current iteration: 7939
Current error: 0.00692428537255

Current iteration: 7940
Current error: 0.00650662670413

Current iteration: 7941
Current error: 0.00612433336065

Current iteration: 7942
Current error: 0.00577403030372

Current iteration: 7943
Current error: 0.00545112350029

Current iteration: 7944
Current error: 0.00515569212455

Current iteration: 7945
Current error: 0.00487971821284

Current iteration: 7946
Current error: 0.00462615090298

Current iteration: 7947
Current error: 0.00439259740017

Current iteration: 7948
Current error: 0.00417331302431

Current iteration: 7949
Current error: 0.00397122638657

Current iteration: 7950
Current error: 0.00392609477196

Current iteration: 7951
Current error: 0.00360920464997

Current iteration: 7952
Current error: 0.00344033477694

Current iteration: 7953
Current error: 0.00329377939177

Current iteration: 7954
Current error: 0.00314302860809

Current iteration: 7955
Current error: 0.00300838136667

Current iteration: 7956
Current error: 0.00291573578098

Current iteration: 7957
Current error: 0.00276285387012

Current iteration: 7958
Current error: 0.00265116196161

Current iteration: 7959
Current error: 0.00254600395829

Current iteration: 7960
Current error: 0.00244680831628

Current iteration: 7961
Current error: 0.00235327897629

Current iteration: 7962
Current error: 0.0022646860271

Current iteration: 7963
Current error: 0.00218102917684

Current iteration: 7964
Current error: 0.0021027717939

Current iteration: 7965
Current error: 0.00206331940253

Current iteration: 7966
Current error: 0.00195517379503

Current iteration: 7967
Current error: 0.00188760758624

Current iteration: 7968
Current error: 0.00182350183533

Current iteration: 7969
Current error: 0.00176240617627

Current iteration: 7970
Current error: 0.00170642783805

Current iteration: 7971
Current error: 0.00164906834538

Current iteration: 7972
Current error: 0.44150610444

Current iteration: 7973
Current error: 0.00268235106126

Current iteration: 7974
Current error: 0.00257015091106

Current iteration: 7975
Current error: 0.00264837138871

Current iteration: 7976
Current error: 0.00237240505062

Current iteration: 7977
Current error: 0.00228287155078

Current iteration: 7978
Current error: 0.00219832236439

Current iteration: 7979
Current error: 0.00211974360579

Current iteration: 7980
Current error: 0.00204216928622

Current iteration: 7981
Current error: 0.00197024228903

Current iteration: 7982
Current error: 0.00190203875247

Current iteration: 7983
Current error: 0.00183699579822

Current iteration: 7984
Current error: 0.00177534508044

Current iteration: 7985
Current error: 0.428330241187

Current iteration: 7986
Current error: 0.00278696621991

Current iteration: 7987
Current error: 0.00267378774035

Current iteration: 7988
Current error: 0.00256711981839

Current iteration: 7989
Current error: 0.0024667941191

Current iteration: 7990
Current error: 0.00237743428034

Current iteration: 7991
Current error: 0.00229549506871

Current iteration: 7992
Current error: 0.00219771428371

Current iteration: 7993
Current error: 0.00211769429254

Current iteration: 7994
Current error: 0.0020417105756

Current iteration: 7995
Current error: 0.00196983036041

Current iteration: 7996
Current error: 0.00190148469468

Current iteration: 7997
Current error: 0.00183663934245

Current iteration: 7998
Current error: 0.00177496162085

Current iteration: 7999
Current error: 0.0017162888858

Current iteration: 8000
Current error: 0.00166076189364

Current iteration: 8001
Current error: 0.00160722646832

Current iteration: 8002
Current error: 0.00155669890937

Current iteration: 8003
Current error: 0.446587608555

Current iteration: 8004
Current error: 0.00256460118836

Current iteration: 8005
Current error: 0.00247023974447

Current iteration: 8006
Current error: 0.00236987426227

Current iteration: 8007
Current error: 0.00228052554984

Current iteration: 8008
Current error: 0.00219590231895

Current iteration: 8009
Current error: 0.00212568231071

Current iteration: 8010
Current error: 0.00204037301814

Current iteration: 8011
Current error: 0.00196812334801

Current iteration: 8012
Current error: 0.0019000945023

Current iteration: 8013
Current error: 0.00183505500934

Current iteration: 8014
Current error: 0.00177349453541

Current iteration: 8015
Current error: 0.00171491192899

Current iteration: 8016
Current error: 0.00165911408689

Current iteration: 8017
Current error: 0.00160602153427

Current iteration: 8018
Current error: 0.00162172153766

Current iteration: 8019
Current error: 0.0015062125746

Current iteration: 8020
Current error: 0.00146008676618

Current iteration: 8021
Current error: 0.00141600256284

Current iteration: 8022
Current error: 0.00137385188131

Current iteration: 8023
Current error: 0.00133351361261

Current iteration: 8024
Current error: 0.00162499087363

Current iteration: 8025
Current error: 0.00125474520278

Current iteration: 8026
Current error: 0.00121939619625

Current iteration: 8027
Current error: 0.00118554264013

Current iteration: 8028
Current error: 0.00115306368321

Current iteration: 8029
Current error: 0.00112188017054

Current iteration: 8030
Current error: 0.00109190908847

Current iteration: 8031
Current error: 0.00106311515508

Current iteration: 8032
Current error: 0.00103541746037

Current iteration: 8033
Current error: 0.00101894664543

Current iteration: 8034
Current error: 0.000988316536592

Current iteration: 8035
Current error: 0.000959221830282

Current iteration: 8036
Current error: 0.00093629820078

Current iteration: 8037
Current error: 0.000911651131262

Current iteration: 8038
Current error: 0.000891466328727

Current iteration: 8039
Current error: 0.000868400675249

Current iteration: 8040
Current error: 0.000847768171612

Current iteration: 8041
Current error: 0.000828621715279

Current iteration: 8042
Current error: 0.000852931764452

Current iteration: 8043
Current error: 0.000789978772432

Current iteration: 8044
Current error: 0.000771957277336

Current iteration: 8045
Current error: 0.000754705496775

Current iteration: 8046
Current error: 0.00083092287304

Current iteration: 8047
Current error: 0.000721022040615

Current iteration: 8048
Current error: 0.000705398610465

Current iteration: 8049
Current error: 0.000690257747279

Current iteration: 8050
Current error: 0.000675602089997

Current iteration: 8051
Current error: 0.000661630600025

Current iteration: 8052
Current error: 0.000647913367924

Current iteration: 8053
Current error: 0.456276902201

Current iteration: 8054
Current error: 0.00107439011

Current iteration: 8055
Current error: 0.00103986203915

Current iteration: 8056
Current error: 0.00101303556551

Current iteration: 8057
Current error: 0.000987236084905

Current iteration: 8058
Current error: 0.00194684443132

Current iteration: 8059
Current error: 0.000931468092157

Current iteration: 8060
Current error: 0.000908477863087

Current iteration: 8061
Current error: 0.000886699485846

Current iteration: 8062
Current error: 0.000867261418888

Current iteration: 8063
Current error: 0.00171373065838

Current iteration: 8064
Current error: 0.000819055025371

Current iteration: 8065
Current error: 0.000800237959822

Current iteration: 8066
Current error: 0.000782070498229

Current iteration: 8067
Current error: 0.000764720206859

Current iteration: 8068
Current error: 0.456649336667

Current iteration: 8069
Current error: 0.00126920550135

Current iteration: 8070
Current error: 0.00125566339471

Current iteration: 8071
Current error: 0.00119924535209

Current iteration: 8072
Current error: 0.0011657586831

Current iteration: 8073
Current error: 0.00113385305669

Current iteration: 8074
Current error: 0.440322090384

Current iteration: 8075
Current error: 0.00181369511245

Current iteration: 8076
Current error: 0.00175309900016

Current iteration: 8077
Current error: 0.00169550597801

Current iteration: 8078
Current error: 0.439206433804

Current iteration: 8079
Current error: 0.0027366985645

Current iteration: 8080
Current error: 0.00262627009839

Current iteration: 8081
Current error: 0.00252260635196

Current iteration: 8082
Current error: 0.00242464964648

Current iteration: 8083
Current error: 0.00233307958437

Current iteration: 8084
Current error: 0.00224493324299

Current iteration: 8085
Current error: 0.00216239488778

Current iteration: 8086
Current error: 0.00208418213293

Current iteration: 8087
Current error: 0.00202629165032

Current iteration: 8088
Current error: 0.00193942669041

Current iteration: 8089
Current error: 0.0018726734031

Current iteration: 8090
Current error: 0.00180976623107

Current iteration: 8091
Current error: 0.00187631052759

Current iteration: 8092
Current error: 0.00169003316805

Current iteration: 8093
Current error: 0.00163544548327

Current iteration: 8094
Current error: 0.00158355724122

Current iteration: 8095
Current error: 0.00153374300275

Current iteration: 8096
Current error: 0.00148633745691

Current iteration: 8097
Current error: 0.00144111148539

Current iteration: 8098
Current error: 0.00139790959139

Current iteration: 8099
Current error: 0.00135648007757

Current iteration: 8100
Current error: 0.00136208107934

Current iteration: 8101
Current error: 0.00128222112225

Current iteration: 8102
Current error: 0.00124220882659

Current iteration: 8103
Current error: 0.00120740393006

Current iteration: 8104
Current error: 0.0011740407848

Current iteration: 8105
Current error: 0.00114201311073

Current iteration: 8106
Current error: 0.442238405679

Current iteration: 8107
Current error: 0.00183723632718

Current iteration: 8108
Current error: 0.0017758468798

Current iteration: 8109
Current error: 0.00171685666776

Current iteration: 8110
Current error: 0.00166093939677

Current iteration: 8111
Current error: 0.00160776806701

Current iteration: 8112
Current error: 0.00155714293139

Current iteration: 8113
Current error: 0.00150851972127

Current iteration: 8114
Current error: 0.00146226912811

Current iteration: 8115
Current error: 0.430297278702

Current iteration: 8116
Current error: 0.00229617935981

Current iteration: 8117
Current error: 0.00221073998957

Current iteration: 8118
Current error: 0.00212993683627

Current iteration: 8119
Current error: 0.00205345496542

Current iteration: 8120
Current error: 0.425647479399

Current iteration: 8121
Current error: 0.0032161540615

Current iteration: 8122
Current error: 0.00307706890476

Current iteration: 8123
Current error: 0.0029635839057

Current iteration: 8124
Current error: 0.00286170499682

Current iteration: 8125
Current error: 0.00271721297168

Current iteration: 8126
Current error: 0.00259929636056

Current iteration: 8127
Current error: 0.00249716372779

Current iteration: 8128
Current error: 0.0024006342619

Current iteration: 8129
Current error: 0.00230959501331

Current iteration: 8130
Current error: 0.00222526093529

Current iteration: 8131
Current error: 0.00214198562421

Current iteration: 8132
Current error: 0.431756619616

Current iteration: 8133
Current error: 0.00341150986455

Current iteration: 8134
Current error: 0.404750091185

Current iteration: 8135
Current error: 0.00527798306303

Current iteration: 8136
Current error: 0.00488107069297

Current iteration: 8137
Current error: 0.00462587529322

Current iteration: 8138
Current error: 0.00439004319017

Current iteration: 8139
Current error: 0.412217388318

Current iteration: 8140
Current error: 0.00678372155297

Current iteration: 8141
Current error: 0.00637808569515

Current iteration: 8142
Current error: 0.00600692094618

Current iteration: 8143
Current error: 0.00566528889646

Current iteration: 8144
Current error: 0.00535136258676

Current iteration: 8145
Current error: 0.00506346918863

Current iteration: 8146
Current error: 0.00479474222367

Current iteration: 8147
Current error: 0.00454756251089

Current iteration: 8148
Current error: 0.0043308464548

Current iteration: 8149
Current error: 0.391043142068

Current iteration: 8150
Current error: 0.00637757344766

Current iteration: 8151
Current error: 0.00644871506059

Current iteration: 8152
Current error: 0.00565691035472

Current iteration: 8153
Current error: 0.00534322387028

Current iteration: 8154
Current error: 0.00516525197239

Current iteration: 8155
Current error: 0.00478627836045

Current iteration: 8156
Current error: 0.00455476652419

Current iteration: 8157
Current error: 0.00431068247715

Current iteration: 8158
Current error: 0.398567707051

Current iteration: 8159
Current error: 0.00646016911736

Current iteration: 8160
Current error: 0.0060816878367

Current iteration: 8161
Current error: 0.397210811688

Current iteration: 8162
Current error: 0.00914168642723

Current iteration: 8163
Current error: 0.00852348860452

Current iteration: 8164
Current error: 0.00796337399187

Current iteration: 8165
Current error: 0.00745422001828

Current iteration: 8166
Current error: 0.00699077135833

Current iteration: 8167
Current error: 0.00656723863849

Current iteration: 8168
Current error: 0.00617996536136

Current iteration: 8169
Current error: 0.00582450669949

Current iteration: 8170
Current error: 0.00549863503298

Current iteration: 8171
Current error: 0.401006227152

Current iteration: 8172
Current error: 0.00831732726307

Current iteration: 8173
Current error: 0.0077751183195

Current iteration: 8174
Current error: 0.00728278153942

Current iteration: 8175
Current error: 0.00683421509677

Current iteration: 8176
Current error: 0.00643638160604

Current iteration: 8177
Current error: 0.00604858282525

Current iteration: 8178
Current error: 0.00570398927807

Current iteration: 8179
Current error: 0.00538748116902

Current iteration: 8180
Current error: 0.0059400747502

Current iteration: 8181
Current error: 0.00481083052146

Current iteration: 8182
Current error: 0.00456179577791

Current iteration: 8183
Current error: 0.00433160016188

Current iteration: 8184
Current error: 0.00411781985765

Current iteration: 8185
Current error: 0.00391904261404

Current iteration: 8186
Current error: 0.00373477945311

Current iteration: 8187
Current error: 0.00356190107841

Current iteration: 8188
Current error: 0.00340015480136

Current iteration: 8189
Current error: 0.00324936238138

Current iteration: 8190
Current error: 0.00314409990528

Current iteration: 8191
Current error: 0.00298804912511

Current iteration: 8192
Current error: 0.00285076319771

Current iteration: 8193
Current error: 0.00281655865225

Current iteration: 8194
Current error: 0.00262269245328

Current iteration: 8195
Current error: 0.0025191371153

Current iteration: 8196
Current error: 0.00242154343823

Current iteration: 8197
Current error: 0.00232928240552

Current iteration: 8198
Current error: 0.00308670352761

Current iteration: 8199
Current error: 0.00249886329795

Current iteration: 8200
Current error: 0.00206739664256

Current iteration: 8201
Current error: 0.00199412501272

Current iteration: 8202
Current error: 0.00192478627011

Current iteration: 8203
Current error: 0.00185859752732

Current iteration: 8204
Current error: 0.00179586724366

Current iteration: 8205
Current error: 0.00173620610056

Current iteration: 8206
Current error: 0.00167948820593

Current iteration: 8207
Current error: 0.00162529738171

Current iteration: 8208
Current error: 0.443332694466

Current iteration: 8209
Current error: 0.00265487873783

Current iteration: 8210
Current error: 0.00254946464943

Current iteration: 8211
Current error: 0.00245016870244

Current iteration: 8212
Current error: 0.0023582698949

Current iteration: 8213
Current error: 0.00226766661488

Current iteration: 8214
Current error: 0.00218379595364

Current iteration: 8215
Current error: 0.00210444784155

Current iteration: 8216
Current error: 0.00202930458102

Current iteration: 8217
Current error: 0.0019579316051

Current iteration: 8218
Current error: 0.00189029542161

Current iteration: 8219
Current error: 0.00182636075929

Current iteration: 8220
Current error: 0.00176539826292

Current iteration: 8221
Current error: 0.00171036262096

Current iteration: 8222
Current error: 0.0016512223299

Current iteration: 8223
Current error: 0.00159843432469

Current iteration: 8224
Current error: 0.00154823834391

Current iteration: 8225
Current error: 0.00152601748999

Current iteration: 8226
Current error: 0.00145391471647

Current iteration: 8227
Current error: 0.42230408263

Current iteration: 8228
Current error: 0.00224375526805

Current iteration: 8229
Current error: 0.00216282763016

Current iteration: 8230
Current error: 0.00208314048471

Current iteration: 8231
Current error: 0.00200893691376

Current iteration: 8232
Current error: 0.00256462752504

Current iteration: 8233
Current error: 0.00186474080924

Current iteration: 8234
Current error: 0.00180358777209

Current iteration: 8235
Current error: 0.00174167617113

Current iteration: 8236
Current error: 0.00168476970616

Current iteration: 8237
Current error: 0.00163039929856

Current iteration: 8238
Current error: 0.00157846665726

Current iteration: 8239
Current error: 0.00153134943787

Current iteration: 8240
Current error: 0.00148186744732

Current iteration: 8241
Current error: 0.00143680780267

Current iteration: 8242
Current error: 0.00139378143032

Current iteration: 8243
Current error: 0.00135256807003

Current iteration: 8244
Current error: 0.00131402240087

Current iteration: 8245
Current error: 0.00127552921611

Current iteration: 8246
Current error: 0.00123924306542

Current iteration: 8247
Current error: 0.00120454541293

Current iteration: 8248
Current error: 0.00117135770322

Current iteration: 8249
Current error: 0.00113939498315

Current iteration: 8250
Current error: 0.00110892300987

Current iteration: 8251
Current error: 0.00107940314664

Current iteration: 8252
Current error: 0.00105106808568

Current iteration: 8253
Current error: 0.00102377386651

Current iteration: 8254
Current error: 0.00099762994797

Current iteration: 8255
Current error: 0.000972379126978

Current iteration: 8256
Current error: 0.000948136293477

Current iteration: 8257
Current error: 0.000924731533432

Current iteration: 8258
Current error: 0.438323996791

Current iteration: 8259
Current error: 0.0014646047975

Current iteration: 8260
Current error: 0.435121442821

Current iteration: 8261
Current error: 0.00233596295524

Current iteration: 8262
Current error: 0.00224872278696

Current iteration: 8263
Current error: 0.392418540235

Current iteration: 8264
Current error: 0.0033026139294

Current iteration: 8265
Current error: 0.00316125446998

Current iteration: 8266
Current error: 0.0030278693316

Current iteration: 8267
Current error: 0.00289519482665

Current iteration: 8268
Current error: 0.00277567538569

Current iteration: 8269
Current error: 0.00266331061645

Current iteration: 8270
Current error: 0.00255779252058

Current iteration: 8271
Current error: 0.00245751741647

Current iteration: 8272
Current error: 0.00236330598705

Current iteration: 8273
Current error: 0.00227429656029

Current iteration: 8274
Current error: 0.00219012522076

Current iteration: 8275
Current error: 0.00211047402212

Current iteration: 8276
Current error: 0.00215343239488

Current iteration: 8277
Current error: 0.00196241116886

Current iteration: 8278
Current error: 0.00189394945546

Current iteration: 8279
Current error: 0.00182946738754

Current iteration: 8280
Current error: 0.00176886999225

Current iteration: 8281
Current error: 0.00170990053359

Current iteration: 8282
Current error: 0.00165430287456

Current iteration: 8283
Current error: 0.00160136539931

Current iteration: 8284
Current error: 0.0015508924487

Current iteration: 8285
Current error: 0.00165605047029

Current iteration: 8286
Current error: 0.00145502121618

Current iteration: 8287
Current error: 0.0014111695143

Current iteration: 8288
Current error: 0.00137010312683

Current iteration: 8289
Current error: 0.447730287006

Current iteration: 8290
Current error: 0.00226270813582

Current iteration: 8291
Current error: 0.00217102100787

Current iteration: 8292
Current error: 0.00212040783085

Current iteration: 8293
Current error: 0.0020175049064

Current iteration: 8294
Current error: 0.00194678900005

Current iteration: 8295
Current error: 0.0018874819367

Current iteration: 8296
Current error: 0.00181588638125

Current iteration: 8297
Current error: 0.0017728011503

Current iteration: 8298
Current error: 0.00169721206573

Current iteration: 8299
Current error: 0.00164228473519

Current iteration: 8300
Current error: 0.00159849093737

Current iteration: 8301
Current error: 0.00154355246806

Current iteration: 8302
Current error: 0.00149251999024

Current iteration: 8303
Current error: 0.00144667154725

Current iteration: 8304
Current error: 0.0014031550037

Current iteration: 8305
Current error: 0.00136156120102

Current iteration: 8306
Current error: 0.00132203629447

Current iteration: 8307
Current error: 0.00128373581402

Current iteration: 8308
Current error: 0.00124714041513

Current iteration: 8309
Current error: 0.00123625033349

Current iteration: 8310
Current error: 0.00117835251183

Current iteration: 8311
Current error: 0.00114639934142

Current iteration: 8312
Current error: 0.00111522165251

Current iteration: 8313
Current error: 0.00108636514886

Current iteration: 8314
Current error: 0.00105697011661

Current iteration: 8315
Current error: 0.00102952093966

Current iteration: 8316
Current error: 0.00100312318893

Current iteration: 8317
Current error: 0.000977906381278

Current iteration: 8318
Current error: 0.000953294496324

Current iteration: 8319
Current error: 0.429150291803

Current iteration: 8320
Current error: 0.00148126521057

Current iteration: 8321
Current error: 0.00143631891385

Current iteration: 8322
Current error: 0.0013931913821

Current iteration: 8323
Current error: 0.436484791455

Current iteration: 8324
Current error: 0.00256751952586

Current iteration: 8325
Current error: 0.00213828129493

Current iteration: 8326
Current error: 0.00206143419237

Current iteration: 8327
Current error: 0.0019909009613

Current iteration: 8328
Current error: 0.00192524347901

Current iteration: 8329
Current error: 0.00185339654167

Current iteration: 8330
Current error: 0.00179081855377

Current iteration: 8331
Current error: 0.00173144786112

Current iteration: 8332
Current error: 0.00167483131371

Current iteration: 8333
Current error: 0.0016336236432

Current iteration: 8334
Current error: 0.00159702340987

Current iteration: 8335
Current error: 0.440288107312

Current iteration: 8336
Current error: 0.00253694957378

Current iteration: 8337
Current error: 0.00243831119859

Current iteration: 8338
Current error: 0.00234509783058

Current iteration: 8339
Current error: 0.00236348675723

Current iteration: 8340
Current error: 0.00217254485588

Current iteration: 8341
Current error: 0.00210494036074

Current iteration: 8342
Current error: 0.00201897966446

Current iteration: 8343
Current error: 0.00195168331344

Current iteration: 8344
Current error: 0.00193733495701

Current iteration: 8345
Current error: 0.00181651475483

Current iteration: 8346
Current error: 0.00175581387289

Current iteration: 8347
Current error: 0.0016987029322

Current iteration: 8348
Current error: 0.00164666066459

Current iteration: 8349
Current error: 0.00159476706783

Current iteration: 8350
Current error: 0.00154124826826

Current iteration: 8351
Current error: 0.00149292744083

Current iteration: 8352
Current error: 0.00144758383584

Current iteration: 8353
Current error: 0.00140385771636

Current iteration: 8354
Current error: 0.00136223916266

Current iteration: 8355
Current error: 0.00132241977197

Current iteration: 8356
Current error: 0.00128426392992

Current iteration: 8357
Current error: 0.00124781075771

Current iteration: 8358
Current error: 0.00121271098453

Current iteration: 8359
Current error: 0.00117912513566

Current iteration: 8360
Current error: 0.00114691445999

Current iteration: 8361
Current error: 0.00111747164023

Current iteration: 8362
Current error: 0.00108639703743

Current iteration: 8363
Current error: 0.00105763486218

Current iteration: 8364
Current error: 0.00103015715666

Current iteration: 8365
Current error: 0.00100375883961

Current iteration: 8366
Current error: 0.000978385053799

Current iteration: 8367
Current error: 0.000953801156437

Current iteration: 8368
Current error: 0.00119723504914

Current iteration: 8369
Current error: 0.000905220172905

Current iteration: 8370
Current error: 0.000889718326664

Current iteration: 8371
Current error: 0.000862136280132

Current iteration: 8372
Current error: 0.000841883035872

Current iteration: 8373
Current error: 0.000822195868162

Current iteration: 8374
Current error: 0.000803203053268

Current iteration: 8375
Current error: 0.000798645532105

Current iteration: 8376
Current error: 0.000783276381764

Current iteration: 8377
Current error: 0.000749806430208

Current iteration: 8378
Current error: 0.00073323865202

Current iteration: 8379
Current error: 0.000717386620579

Current iteration: 8380
Current error: 0.00070168918983

Current iteration: 8381
Current error: 0.000686682298124

Current iteration: 8382
Current error: 0.000672129631609

Current iteration: 8383
Current error: 0.00065806790566

Current iteration: 8384
Current error: 0.464744618294

Current iteration: 8385
Current error: 0.402035590434

Current iteration: 8386
Current error: 0.00170931317801

Current iteration: 8387
Current error: 0.00171419211238

Current iteration: 8388
Current error: 0.00160022084615

Current iteration: 8389
Current error: 0.0015498271104

Current iteration: 8390
Current error: 0.00150171266505

Current iteration: 8391
Current error: 0.00145587313786

Current iteration: 8392
Current error: 0.00141189393313

Current iteration: 8393
Current error: 0.00136988745771

Current iteration: 8394
Current error: 0.00133560809814

Current iteration: 8395
Current error: 0.00129121792863

Current iteration: 8396
Current error: 0.00125447213713

Current iteration: 8397
Current error: 0.00121935969042

Current iteration: 8398
Current error: 0.00118525747918

Current iteration: 8399
Current error: 0.00115299838261

Current iteration: 8400
Current error: 0.00112167105811

Current iteration: 8401
Current error: 0.00109169899373

Current iteration: 8402
Current error: 0.0010628728372

Current iteration: 8403
Current error: 0.44405494584

Current iteration: 8404
Current error: 0.418836881508

Current iteration: 8405
Current error: 0.00274217824226

Current iteration: 8406
Current error: 0.00263170455188

Current iteration: 8407
Current error: 0.00257117159207

Current iteration: 8408
Current error: 0.00242908880236

Current iteration: 8409
Current error: 0.00268237373199

Current iteration: 8410
Current error: 0.00224412337001

Current iteration: 8411
Current error: 0.00216151111867

Current iteration: 8412
Current error: 0.00208340515693

Current iteration: 8413
Current error: 0.00200923326787

Current iteration: 8414
Current error: 0.00202721689913

Current iteration: 8415
Current error: 0.00187112531718

Current iteration: 8416
Current error: 0.00180777948586

Current iteration: 8417
Current error: 0.0017487766666

Current iteration: 8418
Current error: 0.0016902578409

Current iteration: 8419
Current error: 0.00164204532051

Current iteration: 8420
Current error: 0.00158348002634

Current iteration: 8421
Current error: 0.00153657735754

Current iteration: 8422
Current error: 0.00223443849893

Current iteration: 8423
Current error: 0.00146762012332

Current iteration: 8424
Current error: 0.00139007413132

Current iteration: 8425
Current error: 0.00135219772504

Current iteration: 8426
Current error: 0.00130974664358

Current iteration: 8427
Current error: 0.00244342002053

Current iteration: 8428
Current error: 0.00122864810993

Current iteration: 8429
Current error: 0.441431175336

Current iteration: 8430
Current error: 0.00197619677656

Current iteration: 8431
Current error: 0.00190748175557

Current iteration: 8432
Current error: 0.0018423253207

Current iteration: 8433
Current error: 0.432945303747

Current iteration: 8434
Current error: 0.0029434461002

Current iteration: 8435
Current error: 0.00282078079218

Current iteration: 8436
Current error: 0.00272844242761

Current iteration: 8437
Current error: 0.00260156406691

Current iteration: 8438
Current error: 0.00249460411909

Current iteration: 8439
Current error: 0.00239836083163

Current iteration: 8440
Current error: 0.00230740427013

Current iteration: 8441
Current error: 0.00222825439474

Current iteration: 8442
Current error: 0.00218238646148

Current iteration: 8443
Current error: 0.0020640358869

Current iteration: 8444
Current error: 0.00198935150293

Current iteration: 8445
Current error: 0.00192038293359

Current iteration: 8446
Current error: 0.00185433078962

Current iteration: 8447
Current error: 0.00182551128007

Current iteration: 8448
Current error: 0.00173189033324

Current iteration: 8449
Current error: 0.00167542957344

Current iteration: 8450
Current error: 0.00162150634503

Current iteration: 8451
Current error: 0.00157027797064

Current iteration: 8452
Current error: 0.00152101789788

Current iteration: 8453
Current error: 0.00147684162645

Current iteration: 8454
Current error: 0.00178704797231

Current iteration: 8455
Current error: 0.00138283339992

Current iteration: 8456
Current error: 0.00134392815496

Current iteration: 8457
Current error: 0.00130800205224

Current iteration: 8458
Current error: 0.00126690403436

Current iteration: 8459
Current error: 0.00130336285869

Current iteration: 8460
Current error: 0.00119500032211

Current iteration: 8461
Current error: 0.00116353825616

Current iteration: 8462
Current error: 0.00113047488402

Current iteration: 8463
Current error: 0.00110397248539

Current iteration: 8464
Current error: 0.00107121070729

Current iteration: 8465
Current error: 0.00104308508928

Current iteration: 8466
Current error: 0.0010161427502

Current iteration: 8467
Current error: 0.000990221732529

Current iteration: 8468
Current error: 0.410605254191

Current iteration: 8469
Current error: 0.410804035545

Current iteration: 8470
Current error: 0.00303927918833

Current iteration: 8471
Current error: 0.00232166962539

Current iteration: 8472
Current error: 0.00215774986075

Current iteration: 8473
Current error: 0.00241623779514

Current iteration: 8474
Current error: 0.00200383028496

Current iteration: 8475
Current error: 0.00193164803166

Current iteration: 8476
Current error: 0.00186544917714

Current iteration: 8477
Current error: 0.00180222077455

Current iteration: 8478
Current error: 0.0017476835354

Current iteration: 8479
Current error: 0.00181229754177

Current iteration: 8480
Current error: 0.0016658327879

Current iteration: 8481
Current error: 0.00157702061361

Current iteration: 8482
Current error: 0.00152798759545

Current iteration: 8483
Current error: 0.00152561111152

Current iteration: 8484
Current error: 0.00143552915319

Current iteration: 8485
Current error: 0.00139207855702

Current iteration: 8486
Current error: 0.00135094412796

Current iteration: 8487
Current error: 0.00131189379512

Current iteration: 8488
Current error: 0.00127395918003

Current iteration: 8489
Current error: 0.00129810198875

Current iteration: 8490
Current error: 0.00120259465555

Current iteration: 8491
Current error: 0.00116940601419

Current iteration: 8492
Current error: 0.00113759490027

Current iteration: 8493
Current error: 0.00110701751002

Current iteration: 8494
Current error: 0.00107762354611

Current iteration: 8495
Current error: 0.00105327110756

Current iteration: 8496
Current error: 0.0010221789837

Current iteration: 8497
Current error: 0.000996050878961

Current iteration: 8498
Current error: 0.000970910235232

Current iteration: 8499
Current error: 0.000946856836843

Current iteration: 8500
Current error: 0.000923596348274

Current iteration: 8501
Current error: 0.000901310536112

Current iteration: 8502
Current error: 0.000879130303131

Current iteration: 8503
Current error: 0.000858200850147

Current iteration: 8504
Current error: 0.000838455404582

Current iteration: 8505
Current error: 0.000818479367507

Current iteration: 8506
Current error: 0.000799635312798

Current iteration: 8507
Current error: 0.000781758034692

Current iteration: 8508
Current error: 0.000763842614641

Current iteration: 8509
Current error: 0.000746820800597

Current iteration: 8510
Current error: 0.000982067663213

Current iteration: 8511
Current error: 0.000712478648623

Current iteration: 8512
Current error: 0.000697072612654

Current iteration: 8513
Current error: 0.000682218993002

Current iteration: 8514
Current error: 0.000667799669607

Current iteration: 8515
Current error: 0.451832465415

Current iteration: 8516
Current error: 0.00110808510946

Current iteration: 8517
Current error: 0.00106655726183

Current iteration: 8518
Current error: 0.00103874365193

Current iteration: 8519
Current error: 0.00101198289996

Current iteration: 8520
Current error: 0.000986275388137

Current iteration: 8521
Current error: 0.00096144922333

Current iteration: 8522
Current error: 0.00093756939435

Current iteration: 8523
Current error: 0.000916559209913

Current iteration: 8524
Current error: 0.000892356430982

Current iteration: 8525
Current error: 0.000871140132325

Current iteration: 8526
Current error: 0.000850300390936

Current iteration: 8527
Current error: 0.000830456095654

Current iteration: 8528
Current error: 0.00081152810812

Current iteration: 8529
Current error: 0.000812171283234

Current iteration: 8530
Current error: 0.000775351195249

Current iteration: 8531
Current error: 0.000757044006573

Current iteration: 8532
Current error: 0.441400139948

Current iteration: 8533
Current error: 0.00121326448309

Current iteration: 8534
Current error: 0.00117356327386

Current iteration: 8535
Current error: 0.00114156897168

Current iteration: 8536
Current error: 0.00111084141637

Current iteration: 8537
Current error: 0.00108264162061

Current iteration: 8538
Current error: 0.00105292653754

Current iteration: 8539
Current error: 0.00102562696472

Current iteration: 8540
Current error: 0.000999381372588

Current iteration: 8541
Current error: 0.00097407111675

Current iteration: 8542
Current error: 0.000964959243226

Current iteration: 8543
Current error: 0.000926129316667

Current iteration: 8544
Current error: 0.000903542804717

Current iteration: 8545
Current error: 0.00142211624815

Current iteration: 8546
Current error: 0.000856316270428

Current iteration: 8547
Current error: 0.000840699453151

Current iteration: 8548
Current error: 0.000816680208075

Current iteration: 8549
Current error: 0.000797901964234

Current iteration: 8550
Current error: 0.442687679675

Current iteration: 8551
Current error: 0.00127873415881

Current iteration: 8552
Current error: 0.0012422171831

Current iteration: 8553
Current error: 0.00120741709312

Current iteration: 8554
Current error: 0.00117410131149

Current iteration: 8555
Current error: 0.00114203866943

Current iteration: 8556
Current error: 0.00111186672771

Current iteration: 8557
Current error: 0.0010817127473

Current iteration: 8558
Current error: 0.00105342456569

Current iteration: 8559
Current error: 0.00102606361662

Current iteration: 8560
Current error: 0.000999729961167

Current iteration: 8561
Current error: 0.000974618602025

Current iteration: 8562
Current error: 0.00095008015619

Current iteration: 8563
Current error: 0.00112258723478

Current iteration: 8564
Current error: 0.000902234350408

Current iteration: 8565
Current error: 0.000880488605203

Current iteration: 8566
Current error: 0.000860406942844

Current iteration: 8567
Current error: 0.00083923966738

Current iteration: 8568
Current error: 0.000819691128386

Current iteration: 8569
Current error: 0.000800809329203

Current iteration: 8570
Current error: 0.000784475650594

Current iteration: 8571
Current error: 0.000769993854525

Current iteration: 8572
Current error: 0.000747872394747

Current iteration: 8573
Current error: 0.000731325466688

Current iteration: 8574
Current error: 0.000715364296991

Current iteration: 8575
Current error: 0.000713308526861

Current iteration: 8576
Current error: 0.000685031070583

Current iteration: 8577
Current error: 0.000670743381208

Current iteration: 8578
Current error: 0.000656363943965

Current iteration: 8579
Current error: 0.000643452298721

Current iteration: 8580
Current error: 0.000629514773893

Current iteration: 8581
Current error: 0.000616811581381

Current iteration: 8582
Current error: 0.000604626685611

Current iteration: 8583
Current error: 0.000592349019499

Current iteration: 8584
Current error: 0.000580582809364

Current iteration: 8585
Current error: 0.000569231644961

Current iteration: 8586
Current error: 0.00055833913495

Current iteration: 8587
Current error: 0.000551415444903

Current iteration: 8588
Current error: 0.00053704669884

Current iteration: 8589
Current error: 0.000526941159839

Current iteration: 8590
Current error: 0.000517095269985

Current iteration: 8591
Current error: 0.000507555963108

Current iteration: 8592
Current error: 0.000525465185137

Current iteration: 8593
Current error: 0.000489018090638

Current iteration: 8594
Current error: 0.45689490005

Current iteration: 8595
Current error: 0.000804768283779

Current iteration: 8596
Current error: 0.000786364404705

Current iteration: 8597
Current error: 0.000771862901978

Current iteration: 8598
Current error: 0.000751396381569

Current iteration: 8599
Current error: 0.000734784538687

Current iteration: 8600
Current error: 0.000737420107051

Current iteration: 8601
Current error: 0.000703013014591

Current iteration: 8602
Current error: 0.000687972301284

Current iteration: 8603
Current error: 0.000673371166208

Current iteration: 8604
Current error: 0.00118034237068

Current iteration: 8605
Current error: 0.000643647933137

Current iteration: 8606
Current error: 0.000628923374533

Current iteration: 8607
Current error: 0.000620189631756

Current iteration: 8608
Current error: 0.000603541747622

Current iteration: 8609
Current error: 0.000600715242498

Current iteration: 8610
Current error: 0.00057976588389

Current iteration: 8611
Current error: 0.000575497986217

Current iteration: 8612
Current error: 0.000558838984071

Current iteration: 8613
Current error: 0.000546661515872

Current iteration: 8614
Current error: 0.000536293409311

Current iteration: 8615
Current error: 0.000596069309274

Current iteration: 8616
Current error: 0.000515874886347

Current iteration: 8617
Current error: 0.00050633786801

Current iteration: 8618
Current error: 0.000501883718589

Current iteration: 8619
Current error: 0.00048800535848

Current iteration: 8620
Current error: 0.000479229251695

Current iteration: 8621
Current error: 0.000470680871961

Current iteration: 8622
Current error: 0.00046302557545

Current iteration: 8623
Current error: 0.000454449432553

Current iteration: 8624
Current error: 0.456360275398

Current iteration: 8625
Current error: 0.000745944355964

Current iteration: 8626
Current error: 0.000729428895294

Current iteration: 8627
Current error: 0.000713526796785

Current iteration: 8628
Current error: 0.000698154860691

Current iteration: 8629
Current error: 0.397057501702

Current iteration: 8630
Current error: 0.455737407615

Current iteration: 8631
Current error: 0.00176444489804

Current iteration: 8632
Current error: 0.00170630716158

Current iteration: 8633
Current error: 0.00165102233672

Current iteration: 8634
Current error: 0.00159839011745

Current iteration: 8635
Current error: 0.00154785790179

Current iteration: 8636
Current error: 0.00150023618713

Current iteration: 8637
Current error: 0.00145395436389

Current iteration: 8638
Current error: 0.00145916359899

Current iteration: 8639
Current error: 0.00136766488588

Current iteration: 8640
Current error: 0.00132760362356

Current iteration: 8641
Current error: 0.00128924408396

Current iteration: 8642
Current error: 0.00125252776496

Current iteration: 8643
Current error: 0.00121728839513

Current iteration: 8644
Current error: 0.00126570561133

Current iteration: 8645
Current error: 0.00115026724413

Current iteration: 8646
Current error: 0.00111920765302

Current iteration: 8647
Current error: 0.00137817443398

Current iteration: 8648
Current error: 0.00128082062694

Current iteration: 8649
Current error: 0.00102813517625

Current iteration: 8650
Current error: 0.00100176646817

Current iteration: 8651
Current error: 0.000976429606177

Current iteration: 8652
Current error: 0.000991978558465

Current iteration: 8653
Current error: 0.000928053449004

Current iteration: 8654
Current error: 0.000905444507642

Current iteration: 8655
Current error: 0.000897818437925

Current iteration: 8656
Current error: 0.000862303217032

Current iteration: 8657
Current error: 0.000850115409227

Current iteration: 8658
Current error: 0.000822261791044

Current iteration: 8659
Current error: 0.000804533102368

Current iteration: 8660
Current error: 0.000784994997158

Current iteration: 8661
Current error: 0.000772270095417

Current iteration: 8662
Current error: 0.000750086694571

Current iteration: 8663
Current error: 0.000733489744608

Current iteration: 8664
Current error: 0.000717497849022

Current iteration: 8665
Current error: 0.000701938166512

Current iteration: 8666
Current error: 0.000686925920224

Current iteration: 8667
Current error: 0.000674241722586

Current iteration: 8668
Current error: 0.000722577569853

Current iteration: 8669
Current error: 0.000650601794735

Current iteration: 8670
Current error: 0.000630778992383

Current iteration: 8671
Current error: 0.000617955366545

Current iteration: 8672
Current error: 0.000605506346628

Current iteration: 8673
Current error: 0.000593420893265

Current iteration: 8674
Current error: 0.000581812284723

Current iteration: 8675
Current error: 0.000575173668048

Current iteration: 8676
Current error: 0.000559427477993

Current iteration: 8677
Current error: 0.00054848218969

Current iteration: 8678
Current error: 0.000538054183751

Current iteration: 8679
Current error: 0.000527902635241

Current iteration: 8680
Current error: 0.000518042574162

Current iteration: 8681
Current error: 0.000508444018065

Current iteration: 8682
Current error: 0.000499115952525

Current iteration: 8683
Current error: 0.456739858946

Current iteration: 8684
Current error: 0.000820986183572

Current iteration: 8685
Current error: 0.000802065406536

Current iteration: 8686
Current error: 0.000783932429326

Current iteration: 8687
Current error: 0.000766087154576

Current iteration: 8688
Current error: 0.000749055636085

Current iteration: 8689
Current error: 0.427657371397

Current iteration: 8690
Current error: 0.00116372491368

Current iteration: 8691
Current error: 0.00113185291636

Current iteration: 8692
Current error: 0.00110149817705

Current iteration: 8693
Current error: 0.00107232426303

Current iteration: 8694
Current error: 0.00104449393416

Current iteration: 8695
Current error: 0.00101757903678

Current iteration: 8696
Current error: 0.000991420193659

Current iteration: 8697
Current error: 0.00096640486834

Current iteration: 8698
Current error: 0.000945908831039

Current iteration: 8699
Current error: 0.000919130293376

Current iteration: 8700
Current error: 0.000922927149207

Current iteration: 8701
Current error: 0.000874976489124

Current iteration: 8702
Current error: 0.000854358436142

Current iteration: 8703
Current error: 0.000834485411229

Current iteration: 8704
Current error: 0.000814744901225

Current iteration: 8705
Current error: 0.000796210319804

Current iteration: 8706
Current error: 0.00077795147629

Current iteration: 8707
Current error: 0.000760766947733

Current iteration: 8708
Current error: 0.000743638309813

Current iteration: 8709
Current error: 0.000727197903773

Current iteration: 8710
Current error: 0.000717052157813

Current iteration: 8711
Current error: 0.000845518749313

Current iteration: 8712
Current error: 0.000692360425454

Current iteration: 8713
Current error: 0.00066611862842

Current iteration: 8714
Current error: 0.000651657690946

Current iteration: 8715
Current error: 0.000638307934862

Current iteration: 8716
Current error: 0.000625123434721

Current iteration: 8717
Current error: 0.000612444843301

Current iteration: 8718
Current error: 0.446246108048

Current iteration: 8719
Current error: 0.000992914734049

Current iteration: 8720
Current error: 0.000964756127125

Current iteration: 8721
Current error: 0.455966930618

Current iteration: 8722
Current error: 0.00161394424381

Current iteration: 8723
Current error: 0.00156289682724

Current iteration: 8724
Current error: 0.00151414612772

Current iteration: 8725
Current error: 0.00147484769894

Current iteration: 8726
Current error: 0.00142331021205

Current iteration: 8727
Current error: 0.00138065288491

Current iteration: 8728
Current error: 0.00134004523955

Current iteration: 8729
Current error: 0.00130121480492

Current iteration: 8730
Current error: 0.00126393962644

Current iteration: 8731
Current error: 0.00122835758944

Current iteration: 8732
Current error: 0.00119404287405

Current iteration: 8733
Current error: 0.00116119664131

Current iteration: 8734
Current error: 0.0011297249072

Current iteration: 8735
Current error: 0.00109940999895

Current iteration: 8736
Current error: 0.00107032499242

Current iteration: 8737
Current error: 0.00104308762094

Current iteration: 8738
Current error: 0.00102891774647

Current iteration: 8739
Current error: 0.00099170101457

Current iteration: 8740
Current error: 0.000964541457302

Current iteration: 8741
Current error: 0.000941346199673

Current iteration: 8742
Current error: 0.000920680507532

Current iteration: 8743
Current error: 0.000895089922229

Current iteration: 8744
Current error: 0.000873591638858

Current iteration: 8745
Current error: 0.000852998887385

Current iteration: 8746
Current error: 0.000832858544587

Current iteration: 8747
Current error: 0.000825827905835

Current iteration: 8748
Current error: 0.000818503479554

Current iteration: 8749
Current error: 0.00077651865708

Current iteration: 8750
Current error: 0.000767804102498

Current iteration: 8751
Current error: 0.000742135452948

Current iteration: 8752
Current error: 0.000725806591073

Current iteration: 8753
Current error: 0.000714936232593

Current iteration: 8754
Current error: 0.000694688604173

Current iteration: 8755
Current error: 0.000679895126125

Current iteration: 8756
Current error: 0.000665560623066

Current iteration: 8757
Current error: 0.446167929407

Current iteration: 8758
Current error: 0.00107389138844

Current iteration: 8759
Current error: 0.00104569262888

Current iteration: 8760
Current error: 0.00101873411865

Current iteration: 8761
Current error: 0.000992673285058

Current iteration: 8762
Current error: 0.45555573954

Current iteration: 8763
Current error: 0.00165983192042

Current iteration: 8764
Current error: 0.00160656861205

Current iteration: 8765
Current error: 0.00155744991568

Current iteration: 8766
Current error: 0.00150791960856

Current iteration: 8767
Current error: 0.00146412483271

Current iteration: 8768
Current error: 0.00144229321883

Current iteration: 8769
Current error: 0.425191965431

Current iteration: 8770
Current error: 0.00221420627038

Current iteration: 8771
Current error: 0.00213309830538

Current iteration: 8772
Current error: 0.00205644373952

Current iteration: 8773
Current error: 0.00198744655604

Current iteration: 8774
Current error: 0.00191813242291

Current iteration: 8775
Current error: 0.00184912028018

Current iteration: 8776
Current error: 0.00178877753681

Current iteration: 8777
Current error: 0.00172764109041

Current iteration: 8778
Current error: 0.0016712933164

Current iteration: 8779
Current error: 0.00162652077061

Current iteration: 8780
Current error: 0.00156618096457

Current iteration: 8781
Current error: 0.00151731644639

Current iteration: 8782
Current error: 0.00147068211212

Current iteration: 8783
Current error: 0.00142619627447

Current iteration: 8784
Current error: 0.00146713476704

Current iteration: 8785
Current error: 0.00134187980183

Current iteration: 8786
Current error: 0.00130303078674

Current iteration: 8787
Current error: 0.0012655998088

Current iteration: 8788
Current error: 0.00123057151965

Current iteration: 8789
Current error: 0.00119559381799

Current iteration: 8790
Current error: 0.00116268084403

Current iteration: 8791
Current error: 0.00113110659275

Current iteration: 8792
Current error: 0.00110173170598

Current iteration: 8793
Current error: 0.00107169554603

Current iteration: 8794
Current error: 0.00104363264942

Current iteration: 8795
Current error: 0.00101674649622

Current iteration: 8796
Current error: 0.000990746045567

Current iteration: 8797
Current error: 0.000965790188423

Current iteration: 8798
Current error: 0.000941810932048

Current iteration: 8799
Current error: 0.436374201497

Current iteration: 8800
Current error: 0.00149592917787

Current iteration: 8801
Current error: 0.00145025282068

Current iteration: 8802
Current error: 0.00307396609176

Current iteration: 8803
Current error: 0.0013493659528

Current iteration: 8804
Current error: 0.00131013091281

Current iteration: 8805
Current error: 0.0012724956064

Current iteration: 8806
Current error: 0.00123661125203

Current iteration: 8807
Current error: 0.00120189530643

Current iteration: 8808
Current error: 0.00116874730081

Current iteration: 8809
Current error: 0.00113692985267

Current iteration: 8810
Current error: 0.00166826013385

Current iteration: 8811
Current error: 0.0010717672661

Current iteration: 8812
Current error: 0.00104376649119

Current iteration: 8813
Current error: 0.001057116958

Current iteration: 8814
Current error: 0.00102167512432

Current iteration: 8815
Current error: 0.000965261446508

Current iteration: 8816
Current error: 0.000941254627473

Current iteration: 8817
Current error: 0.000918083154673

Current iteration: 8818
Current error: 0.000895773330972

Current iteration: 8819
Current error: 0.00087425355316

Current iteration: 8820
Current error: 0.000853507222043

Current iteration: 8821
Current error: 0.000934610244686

Current iteration: 8822
Current error: 0.000814168743496

Current iteration: 8823
Current error: 0.000794546203657

Current iteration: 8824
Current error: 0.000776484746061

Current iteration: 8825
Current error: 0.000759042884468

Current iteration: 8826
Current error: 0.00074218473503

Current iteration: 8827
Current error: 0.000725880043613

Current iteration: 8828
Current error: 0.000710182070478

Current iteration: 8829
Current error: 0.000694823900027

Current iteration: 8830
Current error: 0.000680089525931

Current iteration: 8831
Current error: 0.000665703749576

Current iteration: 8832
Current error: 0.000651778631704

Current iteration: 8833
Current error: 0.000639486507891

Current iteration: 8834
Current error: 0.000625250406642

Current iteration: 8835
Current error: 0.455704752687

Current iteration: 8836
Current error: 0.00103676388751

Current iteration: 8837
Current error: 0.00101030936996

Current iteration: 8838
Current error: 0.00103676583411

Current iteration: 8839
Current error: 0.00164503884292

Current iteration: 8840
Current error: 0.000929557811116

Current iteration: 8841
Current error: 0.000906841722751

Current iteration: 8842
Current error: 0.000884924291287

Current iteration: 8843
Current error: 0.000863784765012

Current iteration: 8844
Current error: 0.000843387475455

Current iteration: 8845
Current error: 0.000823763163172

Current iteration: 8846
Current error: 0.000804696869403

Current iteration: 8847
Current error: 0.000787675076053

Current iteration: 8848
Current error: 0.000768583038567

Current iteration: 8849
Current error: 0.000754907439851

Current iteration: 8850
Current error: 0.000734719916693

Current iteration: 8851
Current error: 0.000743027574739

Current iteration: 8852
Current error: 0.000702890639166

Current iteration: 8853
Current error: 0.000687838488934

Current iteration: 8854
Current error: 0.00067378848423

Current iteration: 8855
Current error: 0.000659124816572

Current iteration: 8856
Current error: 0.000645435516791

Current iteration: 8857
Current error: 0.000632215633836

Current iteration: 8858
Current error: 0.00258076669321

Current iteration: 8859
Current error: 0.000596937237224

Current iteration: 8860
Current error: 0.000585139518271

Current iteration: 8861
Current error: 0.000589498585258

Current iteration: 8862
Current error: 0.000562340069738

Current iteration: 8863
Current error: 0.000551517935813

Current iteration: 8864
Current error: 0.000541026932876

Current iteration: 8865
Current error: 0.000530790837154

Current iteration: 8866
Current error: 0.000520815558542

Current iteration: 8867
Current error: 0.000514733530735

Current iteration: 8868
Current error: 0.000502343175753

Current iteration: 8869
Current error: 0.00049258547066

Current iteration: 8870
Current error: 0.000483664154345

Current iteration: 8871
Current error: 0.000475002011563

Current iteration: 8872
Current error: 0.000476139491634

Current iteration: 8873
Current error: 0.00045942580284

Current iteration: 8874
Current error: 0.000450292929848

Current iteration: 8875
Current error: 0.000442631202542

Current iteration: 8876
Current error: 0.000434909509898

Current iteration: 8877
Current error: 0.000427475369616

Current iteration: 8878
Current error: 0.000420263362187

Current iteration: 8879
Current error: 0.446797331452

Current iteration: 8880
Current error: 0.000711717553837

Current iteration: 8881
Current error: 0.000658281705509

Current iteration: 8882
Current error: 0.000644617761819

Current iteration: 8883
Current error: 0.000631372430481

Current iteration: 8884
Current error: 0.000618731174072

Current iteration: 8885
Current error: 0.000606314004251

Current iteration: 8886
Current error: 0.000673097250731

Current iteration: 8887
Current error: 0.000581626592744

Current iteration: 8888
Current error: 0.000570215127454

Current iteration: 8889
Current error: 0.000559161787606

Current iteration: 8890
Current error: 0.000548423271281

Current iteration: 8891
Current error: 0.000538232596948

Current iteration: 8892
Current error: 0.000529468167245

Current iteration: 8893
Current error: 0.000519579426659

Current iteration: 8894
Current error: 0.000508633320337

Current iteration: 8895
Current error: 0.000499057987413

Current iteration: 8896
Current error: 0.000490040351891

Current iteration: 8897
Current error: 0.000481164260604

Current iteration: 8898
Current error: 0.000472549240297

Current iteration: 8899
Current error: 0.000591470823467

Current iteration: 8900
Current error: 0.000455150360442

Current iteration: 8901
Current error: 0.000447222565635

Current iteration: 8902
Current error: 0.000439505099466

Current iteration: 8903
Current error: 0.000432010564574

Current iteration: 8904
Current error: 0.000424681594739

Current iteration: 8905
Current error: 0.000417507093691

Current iteration: 8906
Current error: 0.000410540822569

Current iteration: 8907
Current error: 0.000403740179294

Current iteration: 8908
Current error: 0.00040680946333

Current iteration: 8909
Current error: 0.000390577422255

Current iteration: 8910
Current error: 0.000384257075183

Current iteration: 8911
Current error: 0.0003780924827

Current iteration: 8912
Current error: 0.000374223393613

Current iteration: 8913
Current error: 0.00036620465927

Current iteration: 8914
Current error: 0.000360810778709

Current iteration: 8915
Current error: 0.000354838242448

Current iteration: 8916
Current error: 0.000349373611082

Current iteration: 8917
Current error: 0.000344054019625

Current iteration: 8918
Current error: 0.000338781009386

Current iteration: 8919
Current error: 0.00033556338299

Current iteration: 8920
Current error: 0.000328668617891

Current iteration: 8921
Current error: 0.000323767440036

Current iteration: 8922
Current error: 0.000318993844425

Current iteration: 8923
Current error: 0.000314866706477

Current iteration: 8924
Current error: 0.00030973152253

Current iteration: 8925
Current error: 0.000305264421994

Current iteration: 8926
Current error: 0.00030095169711

Current iteration: 8927
Current error: 0.000296618823931

Current iteration: 8928
Current error: 0.00029241175748

Current iteration: 8929
Current error: 0.000288269600047

Current iteration: 8930
Current error: 0.000284429657757

Current iteration: 8931
Current error: 0.000280767387042

Current iteration: 8932
Current error: 0.00133488681148

Current iteration: 8933
Current error: 0.470586894744

Current iteration: 8934
Current error: 0.000462775386892

Current iteration: 8935
Current error: 0.000454653981499

Current iteration: 8936
Current error: 0.000446751292802

Current iteration: 8937
Current error: 0.000439043645436

Current iteration: 8938
Current error: 0.000431537775772

Current iteration: 8939
Current error: 0.000770637355313

Current iteration: 8940
Current error: 0.000415080177004

Current iteration: 8941
Current error: 0.000408181764895

Current iteration: 8942
Current error: 0.0004014210512

Current iteration: 8943
Current error: 0.000394847153742

Current iteration: 8944
Current error: 0.000553356141127

Current iteration: 8945
Current error: 0.000381183060212

Current iteration: 8946
Current error: 0.000375094680435

Current iteration: 8947
Current error: 0.000369617904507

Current iteration: 8948
Current error: 0.000363346097982

Current iteration: 8949
Current error: 0.000357665845749

Current iteration: 8950
Current error: 0.000352476775046

Current iteration: 8951
Current error: 0.000346843237641

Current iteration: 8952
Current error: 0.000341582043799

Current iteration: 8953
Current error: 0.000336257789663

Current iteration: 8954
Current error: 0.385284147406

Current iteration: 8955
Current error: 0.000482414164034

Current iteration: 8956
Current error: 0.000473694676076

Current iteration: 8957
Current error: 0.000465278845154

Current iteration: 8958
Current error: 0.000457091024734

Current iteration: 8959
Current error: 0.375037647683

Current iteration: 8960
Current error: 0.000651648864016

Current iteration: 8961
Current error: 0.000638188158096

Current iteration: 8962
Current error: 0.44634961746

Current iteration: 8963
Current error: 0.00103152072632

Current iteration: 8964
Current error: 0.00100504784105

Current iteration: 8965
Current error: 0.000979521703491

Current iteration: 8966
Current error: 0.000955027934303

Current iteration: 8967
Current error: 0.000941455474976

Current iteration: 8968
Current error: 0.000908658131707

Current iteration: 8969
Current error: 0.000904131453676

Current iteration: 8970
Current error: 0.000865111728754

Current iteration: 8971
Current error: 0.000844926582082

Current iteration: 8972
Current error: 0.000825844927189

Current iteration: 8973
Current error: 0.000806137217468

Current iteration: 8974
Current error: 0.000787558916751

Current iteration: 8975
Current error: 0.00076965434505

Current iteration: 8976
Current error: 0.439469097164

Current iteration: 8977
Current error: 0.00123022095816

Current iteration: 8978
Current error: 0.00119540300546

Current iteration: 8979
Current error: 0.00116489983523

Current iteration: 8980
Current error: 0.00113091960349

Current iteration: 8981
Current error: 0.00110526813178

Current iteration: 8982
Current error: 0.00107158798678

Current iteration: 8983
Current error: 0.00107367495205

Current iteration: 8984
Current error: 0.00101618080479

Current iteration: 8985
Current error: 0.00103063574155

Current iteration: 8986
Current error: 0.000964974798545

Current iteration: 8987
Current error: 0.000940969200606

Current iteration: 8988
Current error: 0.000917797399187

Current iteration: 8989
Current error: 0.00089548390651

Current iteration: 8990
Current error: 0.000873998892227

Current iteration: 8991
Current error: 0.000853232330175

Current iteration: 8992
Current error: 0.000834050526743

Current iteration: 8993
Current error: 0.000813864180941

Current iteration: 8994
Current error: 0.000795256475213

Current iteration: 8995
Current error: 0.000777112154567

Current iteration: 8996
Current error: 0.453333543295

Current iteration: 8997
Current error: 0.00132215098447

Current iteration: 8998
Current error: 0.00124706328809

Current iteration: 8999
Current error: 0.00128503160577

Current iteration: 9000
Current error: 0.00117770342451

Current iteration: 9001
Current error: 0.00114766231896

Current iteration: 9002
Current error: 0.00111480398384

Current iteration: 9003
Current error: 0.00108670247544

Current iteration: 9004
Current error: 0.00105638900358

Current iteration: 9005
Current error: 0.00103320369189

Current iteration: 9006
Current error: 0.00100252568286

Current iteration: 9007
Current error: 0.000978260458128

Current iteration: 9008
Current error: 0.00388018869956

Current iteration: 9009
Current error: 0.000911058808097

Current iteration: 9010
Current error: 0.000889062023237

Current iteration: 9011
Current error: 0.000868665418095

Current iteration: 9012
Current error: 0.000847286800963

Current iteration: 9013
Current error: 0.435897459893

Current iteration: 9014
Current error: 0.00134756571544

Current iteration: 9015
Current error: 0.00190303535842

Current iteration: 9016
Current error: 0.0012645525619

Current iteration: 9017
Current error: 0.379266920359

Current iteration: 9018
Current error: 0.00184324519249

Current iteration: 9019
Current error: 0.00178129975217

Current iteration: 9020
Current error: 0.00172229790565

Current iteration: 9021
Current error: 0.00176808668856

Current iteration: 9022
Current error: 0.0016114573011

Current iteration: 9023
Current error: 0.00167197856597

Current iteration: 9024
Current error: 0.00151059794478

Current iteration: 9025
Current error: 0.00146595381449

Current iteration: 9026
Current error: 0.00141992952987

Current iteration: 9027
Current error: 0.00137756377344

Current iteration: 9028
Current error: 0.00133716776702

Current iteration: 9029
Current error: 0.00129859376394

Current iteration: 9030
Current error: 0.434447473236

Current iteration: 9031
Current error: 0.295758114865

Current iteration: 9032
Current error: 0.331321134392

Current iteration: 9033
Current error: 0.0041039363112

Current iteration: 9034
Current error: 0.00607558228336

Current iteration: 9035
Current error: 0.237788526435

Current iteration: 9036
Current error: 0.00481153954741

Current iteration: 9037
Current error: 0.0045629790257

Current iteration: 9038
Current error: 0.00433263314156

Current iteration: 9039
Current error: 0.00411899812106

Current iteration: 9040
Current error: 0.00392011370107

Current iteration: 9041
Current error: 0.00373498453542

Current iteration: 9042
Current error: 0.00356212721295

Current iteration: 9043
Current error: 0.262850514122

Current iteration: 9044
Current error: 0.00455581284252

Current iteration: 9045
Current error: 0.00432469643085

Current iteration: 9046
Current error: 0.00411172653297

Current iteration: 9047
Current error: 0.00391309439771

Current iteration: 9048
Current error: 0.00373054537226

Current iteration: 9049
Current error: 0.364669937081

Current iteration: 9050
Current error: 0.00550983773762

Current iteration: 9051
Current error: 0.00510427500348

Current iteration: 9052
Current error: 0.00484574858922

Current iteration: 9053
Current error: 0.020537079274

Current iteration: 9054
Current error: 0.00417104362263

Current iteration: 9055
Current error: 0.00396876424544

Current iteration: 9056
Current error: 0.00440255154113

Current iteration: 9057
Current error: 0.00363862407554

Current iteration: 9058
Current error: 0.00343228104367

Current iteration: 9059
Current error: 0.00327671322038

Current iteration: 9060
Current error: 0.0031395823725

Current iteration: 9061
Current error: 0.00303084774417

Current iteration: 9062
Current error: 0.00293145581099

Current iteration: 9063
Current error: 0.00275417212856

Current iteration: 9064
Current error: 0.269157047489

Current iteration: 9065
Current error: 0.00355837415098

Current iteration: 9066
Current error: 0.00339731734373

Current iteration: 9067
Current error: 0.00324665444293

Current iteration: 9068
Current error: 0.00310559259232

Current iteration: 9069
Current error: 0.00297399276649

Current iteration: 9070
Current error: 0.00285192361478

Current iteration: 9071
Current error: 0.00273221742165

Current iteration: 9072
Current error: 0.00262245462802

Current iteration: 9073
Current error: 0.00251961863398

Current iteration: 9074
Current error: 0.270935475888

Current iteration: 9075
Current error: 0.00341480994099

Current iteration: 9076
Current error: 0.00312171560812

Current iteration: 9077
Current error: 0.0129971024423

Current iteration: 9078
Current error: 0.00276550855611

Current iteration: 9079
Current error: 0.0027057138504

Current iteration: 9080
Current error: 0.00254646345382

Current iteration: 9081
Current error: 0.00244780403602

Current iteration: 9082
Current error: 0.00235430300587

Current iteration: 9083
Current error: 0.00234259519403

Current iteration: 9084
Current error: 0.00218045503993

Current iteration: 9085
Current error: 0.00210119757091

Current iteration: 9086
Current error: 0.0020261645147

Current iteration: 9087
Current error: 0.00195524182616

Current iteration: 9088
Current error: 0.0018876380859

Current iteration: 9089
Current error: 0.00182331964453

Current iteration: 9090
Current error: 0.00176232071553

Current iteration: 9091
Current error: 0.00170425061279

Current iteration: 9092
Current error: 0.00164909251531

Current iteration: 9093
Current error: 0.00159633499744

Current iteration: 9094
Current error: 0.00155314392204

Current iteration: 9095
Current error: 0.00149797865104

Current iteration: 9096
Current error: 0.298535988379

Current iteration: 9097
Current error: 0.00200656606665

Current iteration: 9098
Current error: 0.00193615661664

Current iteration: 9099
Current error: 0.00187133226954

Current iteration: 9100
Current error: 0.00180610548747

Current iteration: 9101
Current error: 0.271964236332

Current iteration: 9102
Current error: 0.00235434607102

Current iteration: 9103
Current error: 0.00226802546931

Current iteration: 9104
Current error: 0.00218200974065

Current iteration: 9105
Current error: 0.00210296285243

Current iteration: 9106
Current error: 0.00202762585043

Current iteration: 9107
Current error: 0.00195660434486

Current iteration: 9108
Current error: 0.00188882692027

Current iteration: 9109
Current error: 0.00182463184593

Current iteration: 9110
Current error: 0.00176351478237

Current iteration: 9111
Current error: 0.0017154861313

Current iteration: 9112
Current error: 0.00165000535647

Current iteration: 9113
Current error: 0.00159725078513

Current iteration: 9114
Current error: 0.00155027296403

Current iteration: 9115
Current error: 0.00149896107104

Current iteration: 9116
Current error: 0.344941046789

Current iteration: 9117
Current error: 0.00212404560661

Current iteration: 9118
Current error: 0.00204283302267

Current iteration: 9119
Current error: 0.00197057200682

Current iteration: 9120
Current error: 0.00190300708259

Current iteration: 9121
Current error: 0.00183798642912

Current iteration: 9122
Current error: 0.00177914150235

Current iteration: 9123
Current error: 0.00171700499205

Current iteration: 9124
Current error: 0.00169486156594

Current iteration: 9125
Current error: 0.00160746441087

Current iteration: 9126
Current error: 0.00155675189448

Current iteration: 9127
Current error: 0.286410362513

Current iteration: 9128
Current error: 0.00206784570415

Current iteration: 9129
Current error: 0.00199433745194

Current iteration: 9130
Current error: 0.00192486171244

Current iteration: 9131
Current error: 0.001858882321

Current iteration: 9132
Current error: 0.00181388499887

Current iteration: 9133
Current error: 0.00173630368013

Current iteration: 9134
Current error: 0.00168171448256

Current iteration: 9135
Current error: 0.00615156645721

Current iteration: 9136
Current error: 0.001538707627

Current iteration: 9137
Current error: 0.00148875552856

Current iteration: 9138
Current error: 0.00144342282863

Current iteration: 9139
Current error: 0.001400093416

Current iteration: 9140
Current error: 0.00135861910655

Current iteration: 9141
Current error: 0.00131884796171

Current iteration: 9142
Current error: 0.00128090769857

Current iteration: 9143
Current error: 0.254046390742

Current iteration: 9144
Current error: 0.00200313007292

Current iteration: 9145
Current error: 0.00159079545185

Current iteration: 9146
Current error: 0.00154732740147

Current iteration: 9147
Current error: 0.0015682105422

Current iteration: 9148
Current error: 0.00224467949215

Current iteration: 9149
Current error: 0.00143323654

Current iteration: 9150
Current error: 0.00135103528709

Current iteration: 9151
Current error: 0.00131156432267

Current iteration: 9152
Current error: 0.00127395030563

Current iteration: 9153
Current error: 0.00133435832276

Current iteration: 9154
Current error: 0.00120199638646

Current iteration: 9155
Current error: 0.00116894316027

Current iteration: 9156
Current error: 0.00113711700536

Current iteration: 9157
Current error: 0.00436015575341

Current iteration: 9158
Current error: 0.00105467313778

Current iteration: 9159
Current error: 0.00102708086295

Current iteration: 9160
Current error: 0.00100076914033

Current iteration: 9161
Current error: 0.00711039686486

Current iteration: 9162
Current error: 0.000919712916592

Current iteration: 9163
Current error: 0.325581449805

Current iteration: 9164
Current error: 0.00127424646364

Current iteration: 9165
Current error: 0.00124665221631

Current iteration: 9166
Current error: 0.425060750906

Current iteration: 9167
Current error: 0.00196611204442

Current iteration: 9168
Current error: 0.00387911009369

Current iteration: 9169
Current error: 0.00180924535823

Current iteration: 9170
Current error: 0.00176583038518

Current iteration: 9171
Current error: 0.0016909757652

Current iteration: 9172
Current error: 0.00276117310149

Current iteration: 9173
Current error: 0.00157168605432

Current iteration: 9174
Current error: 0.00152266198041

Current iteration: 9175
Current error: 0.00148056996593

Current iteration: 9176
Current error: 0.00143089380618

Current iteration: 9177
Current error: 0.00138799112358

Current iteration: 9178
Current error: 0.00134747229031

Current iteration: 9179
Current error: 0.00131399930093

Current iteration: 9180
Current error: 0.00127048091922

Current iteration: 9181
Current error: 0.0012343069605

Current iteration: 9182
Current error: 0.392140858153

Current iteration: 9183
Current error: 0.00187138478957

Current iteration: 9184
Current error: 0.00180739963888

Current iteration: 9185
Current error: 0.001747157094

Current iteration: 9186
Current error: 0.00169033891333

Current iteration: 9187
Current error: 0.00164513476992

Current iteration: 9188
Current error: 0.00158309327445

Current iteration: 9189
Current error: 0.00155038417212

Current iteration: 9190
Current error: 0.00148590833877

Current iteration: 9191
Current error: 0.00152679473789

Current iteration: 9192
Current error: 0.00139632336122

Current iteration: 9193
Current error: 0.00135514503903

Current iteration: 9194
Current error: 0.00131553001463

Current iteration: 9195
Current error: 0.00135328582257

Current iteration: 9196
Current error: 0.00124652522886

Current iteration: 9197
Current error: 0.00125251033326

Current iteration: 9198
Current error: 0.00117692979218

Current iteration: 9199
Current error: 0.00113994411697

Current iteration: 9200
Current error: 0.00110919205768

Current iteration: 9201
Current error: 0.00107981533734

Current iteration: 9202
Current error: 0.0010514994923

Current iteration: 9203
Current error: 0.282311239846

Current iteration: 9204
Current error: 0.00150062749547

Current iteration: 9205
Current error: 0.218297944914

Current iteration: 9206
Current error: 0.00175573499376

Current iteration: 9207
Current error: 0.0236517929643

Current iteration: 9208
Current error: 0.00152886054906

Current iteration: 9209
Current error: 0.00148177044036

Current iteration: 9210
Current error: 0.00143688233532

Current iteration: 9211
Current error: 0.00139431305453

Current iteration: 9212
Current error: 0.00135307601143

Current iteration: 9213
Current error: 0.00131475203013

Current iteration: 9214
Current error: 0.00127519681518

Current iteration: 9215
Current error: 0.00123917172622

Current iteration: 9216
Current error: 0.00120442218222

Current iteration: 9217
Current error: 0.00133402444398

Current iteration: 9218
Current error: 0.00113756932412

Current iteration: 9219
Current error: 0.00110824500753

Current iteration: 9220
Current error: 0.00107749692022

Current iteration: 9221
Current error: 0.00104926983513

Current iteration: 9222
Current error: 0.00350033212767

Current iteration: 9223
Current error: 0.000981181683196

Current iteration: 9224
Current error: 0.000958762432071

Current iteration: 9225
Current error: 0.000938031503579

Current iteration: 9226
Current error: 0.000907815161195

Current iteration: 9227
Current error: 0.000885293920879

Current iteration: 9228
Current error: 0.000864170602976

Current iteration: 9229
Current error: 0.000843740223934

Current iteration: 9230
Current error: 0.0008239877265

Current iteration: 9231
Current error: 0.000805198595766

Current iteration: 9232
Current error: 0.000786536369832

Current iteration: 9233
Current error: 0.000768823617248

Current iteration: 9234
Current error: 0.000751575485633

Current iteration: 9235
Current error: 0.000734937117099

Current iteration: 9236
Current error: 0.00071894062332

Current iteration: 9237
Current error: 0.000704290539041

Current iteration: 9238
Current error: 0.000688276053064

Current iteration: 9239
Current error: 0.000673668212424

Current iteration: 9240
Current error: 0.000659535705306

Current iteration: 9241
Current error: 0.000645869492882

Current iteration: 9242
Current error: 0.0159803850221

Current iteration: 9243
Current error: 0.000619593593997

Current iteration: 9244
Current error: 0.000572784970195

Current iteration: 9245
Current error: 0.00120367170649

Current iteration: 9246
Current error: 0.000545636475151

Current iteration: 9247
Current error: 0.000535454442574

Current iteration: 9248
Current error: 0.000525426668674

Current iteration: 9249
Current error: 0.00051542474577

Current iteration: 9250
Current error: 0.000506005188734

Current iteration: 9251
Current error: 0.000496860052324

Current iteration: 9252
Current error: 0.000490301462588

Current iteration: 9253
Current error: 0.000478833954254

Current iteration: 9254
Current error: 0.000470303620112

Current iteration: 9255
Current error: 0.000461981723887

Current iteration: 9256
Current error: 0.450609263979

Current iteration: 9257
Current error: 0.266688877809

Current iteration: 9258
Current error: 0.0010129538164

Current iteration: 9259
Current error: 0.000987290265695

Current iteration: 9260
Current error: 0.000962361967946

Current iteration: 9261
Current error: 0.0009384327212

Current iteration: 9262
Current error: 0.000915391615164

Current iteration: 9263
Current error: 0.000894152368481

Current iteration: 9264
Current error: 0.000871728308976

Current iteration: 9265
Current error: 0.290382087216

Current iteration: 9266
Current error: 0.0011745106096

Current iteration: 9267
Current error: 0.00113909624402

Current iteration: 9268
Current error: 0.0011083755624

Current iteration: 9269
Current error: 0.00107897903035

Current iteration: 9270
Current error: 0.00105208532679

Current iteration: 9271
Current error: 0.00102344514885

Current iteration: 9272
Current error: 0.000997310463964

Current iteration: 9273
Current error: 0.000974859196699

Current iteration: 9274
Current error: 0.000947807709944

Current iteration: 9275
Current error: 0.000924401733474

Current iteration: 9276
Current error: 0.000903394695592

Current iteration: 9277
Current error: 0.000880116980752

Current iteration: 9278
Current error: 0.000860908735878

Current iteration: 9279
Current error: 0.00083890981879

Current iteration: 9280
Current error: 0.00089179014866

Current iteration: 9281
Current error: 0.0140616210444

Current iteration: 9282
Current error: 0.000740059618865

Current iteration: 9283
Current error: 0.000723812114589

Current iteration: 9284
Current error: 0.000708799189992

Current iteration: 9285
Current error: 0.000694390141242

Current iteration: 9286
Current error: 0.000678062131104

Current iteration: 9287
Current error: 0.0013144498463

Current iteration: 9288
Current error: 0.000644917910505

Current iteration: 9289
Current error: 0.000631723077437

Current iteration: 9290
Current error: 0.000639145243113

Current iteration: 9291
Current error: 0.0006061774676

Current iteration: 9292
Current error: 0.00224003368669

Current iteration: 9293
Current error: 0.000575520370619

Current iteration: 9294
Current error: 0.000562102937724

Current iteration: 9295
Current error: 0.000551284215625

Current iteration: 9296
Current error: 0.000541332152492

Current iteration: 9297
Current error: 0.000530529187127

Current iteration: 9298
Current error: 0.000520916360064

Current iteration: 9299
Current error: 0.000510949841194

Current iteration: 9300
Current error: 0.000503173259427

Current iteration: 9301
Current error: 0.00049237567325

Current iteration: 9302
Current error: 0.000483522700625

Current iteration: 9303
Current error: 0.000529394293524

Current iteration: 9304
Current error: 0.000465983178805

Current iteration: 9305
Current error: 0.0104176526434

Current iteration: 9306
Current error: 0.345199182149

Current iteration: 9307
Current error: 0.318611795442

Current iteration: 9308
Current error: 0.458980804246

Current iteration: 9309
Current error: 0.188778448239

Current iteration: 9310
Current error: 0.00191649678581

Current iteration: 9311
Current error: 0.00184664435483

Current iteration: 9312
Current error: 0.00178378181378

Current iteration: 9313
Current error: 0.00172546051192

Current iteration: 9314
Current error: 0.00166865917095

Current iteration: 9315
Current error: 0.00161455078421

Current iteration: 9316
Current error: 0.00156388952097

Current iteration: 9317
Current error: 0.00151542794934

Current iteration: 9318
Current error: 0.00146822737998

Current iteration: 9319
Current error: 0.00142372662154

Current iteration: 9320
Current error: 0.00143755130233

Current iteration: 9321
Current error: 0.0013398846312

Current iteration: 9322
Current error: 0.00130107148455

Current iteration: 9323
Current error: 0.00136532306913

Current iteration: 9324
Current error: 0.00122777206033

Current iteration: 9325
Current error: 0.00119433938208

Current iteration: 9326
Current error: 0.00580330925146

Current iteration: 9327
Current error: 0.00109731698863

Current iteration: 9328
Current error: 0.00106831566348

Current iteration: 9329
Current error: 0.00104044574741

Current iteration: 9330
Current error: 0.0010135882933

Current iteration: 9331
Current error: 0.00100784804479

Current iteration: 9332
Current error: 0.00111561934746

Current iteration: 9333
Current error: 0.000960921541227

Current iteration: 9334
Current error: 0.0271586597532

Current iteration: 9335
Current error: 0.000825143384524

Current iteration: 9336
Current error: 0.000809909278982

Current iteration: 9337
Current error: 0.000787710105792

Current iteration: 9338
Current error: 0.000769793408575

Current iteration: 9339
Current error: 0.000752658301589

Current iteration: 9340
Current error: 0.000736320116783

Current iteration: 9341
Current error: 0.00072024512795

Current iteration: 9342
Current error: 0.000704234389538

Current iteration: 9343
Current error: 0.000689173341799

Current iteration: 9344
Current error: 0.000674575844618

Current iteration: 9345
Current error: 0.000660344165741

Current iteration: 9346
Current error: 0.000691970040375

Current iteration: 9347
Current error: 0.000637732015351

Current iteration: 9348
Current error: 0.00230536373888

Current iteration: 9349
Current error: 0.000907409069348

Current iteration: 9350
Current error: 0.000583799439404

Current iteration: 9351
Current error: 0.000572270096946

Current iteration: 9352
Current error: 0.000561163453617

Current iteration: 9353
Current error: 0.000550916753037

Current iteration: 9354
Current error: 0.000539893786493

Current iteration: 9355
Current error: 0.0154126760265

Current iteration: 9356
Current error: 0.000488990113776

Current iteration: 9357
Current error: 0.000480263729431

Current iteration: 9358
Current error: 0.000480849737389

Current iteration: 9359
Current error: 0.000465384327634

Current iteration: 9360
Current error: 0.318159649132

Current iteration: 9361
Current error: 0.000641065939343

Current iteration: 9362
Current error: 0.000636854693217

Current iteration: 9363
Current error: 0.000615099817785

Current iteration: 9364
Current error: 0.460757352061

Current iteration: 9365
Current error: 0.00105364011756

Current iteration: 9366
Current error: 0.197170604023

Current iteration: 9367
Current error: 0.00128278974365

Current iteration: 9368
Current error: 0.00124633851322

Current iteration: 9369
Current error: 0.18794695091

Current iteration: 9370
Current error: 0.00152481156552

Current iteration: 9371
Current error: 0.00150895277961

Current iteration: 9372
Current error: 0.00143259737373

Current iteration: 9373
Current error: 0.00138966229192

Current iteration: 9374
Current error: 0.0202924092493

Current iteration: 9375
Current error: 0.00948703893131

Current iteration: 9376
Current error: 0.00114642909015

Current iteration: 9377
Current error: 0.00112044971911

Current iteration: 9378
Current error: 0.00108569573228

Current iteration: 9379
Current error: 0.00105720647472

Current iteration: 9380
Current error: 0.00102975103373

Current iteration: 9381
Current error: 0.00100373673645

Current iteration: 9382
Current error: 0.00137002945335

Current iteration: 9383
Current error: 0.00095211910602

Current iteration: 9384
Current error: 0.000926048546385

Current iteration: 9385
Current error: 0.000904659056469

Current iteration: 9386
Current error: 0.000881694570396

Current iteration: 9387
Current error: 0.000860714511628

Current iteration: 9388
Current error: 0.000840395901291

Current iteration: 9389
Current error: 0.0257847092032

Current iteration: 9390
Current error: 0.000741635022183

Current iteration: 9391
Current error: 0.000725352749972

Current iteration: 9392
Current error: 0.000709558470459

Current iteration: 9393
Current error: 0.000694348625331

Current iteration: 9394
Current error: 0.000679994160912

Current iteration: 9395
Current error: 0.00072687737796

Current iteration: 9396
Current error: 0.000650776503772

Current iteration: 9397
Current error: 0.000637346022032

Current iteration: 9398
Current error: 0.000649151519474

Current iteration: 9399
Current error: 0.000613094466551

Current iteration: 9400
Current error: 0.000599183221143

Current iteration: 9401
Current error: 0.000587301132123

Current iteration: 9402
Current error: 0.000575757674413

Current iteration: 9403
Current error: 0.0167003805473

Current iteration: 9404
Current error: 0.000518964529616

Current iteration: 9405
Current error: 0.000509358553229

Current iteration: 9406
Current error: 0.000501481767809

Current iteration: 9407
Current error: 0.000490856551024

Current iteration: 9408
Current error: 0.000544066323296

Current iteration: 9409
Current error: 0.000472885940042

Current iteration: 9410
Current error: 0.000464564194144

Current iteration: 9411
Current error: 0.000456544590256

Current iteration: 9412
Current error: 0.000448429987462

Current iteration: 9413
Current error: 0.000440689160366

Current iteration: 9414
Current error: 0.000433119726539

Current iteration: 9415
Current error: 0.000467074539719

Current iteration: 9416
Current error: 0.000418290500601

Current iteration: 9417
Current error: 0.000411368057282

Current iteration: 9418
Current error: 0.000794957717592

Current iteration: 9419
Current error: 0.000395789155623

Current iteration: 9420
Current error: 0.000392213550636

Current iteration: 9421
Current error: 0.000382813949107

Current iteration: 9422
Current error: 0.000376839756362

Current iteration: 9423
Current error: 0.00037069338985

Current iteration: 9424
Current error: 0.000366801078801

Current iteration: 9425
Current error: 0.000359179305105

Current iteration: 9426
Current error: 0.000353545533923

Current iteration: 9427
Current error: 0.000348100679831

Current iteration: 9428
Current error: 0.000343112145745

Current iteration: 9429
Current error: 0.000343683488667

Current iteration: 9430
Current error: 0.000332472579698

Current iteration: 9431
Current error: 0.000327492581513

Current iteration: 9432
Current error: 0.000323078007141

Current iteration: 9433
Current error: 0.00031789824086

Current iteration: 9434
Current error: 0.000313958992573

Current iteration: 9435
Current error: 0.000308625823032

Current iteration: 9436
Current error: 0.000304184973899

Current iteration: 9437
Current error: 0.0002998722289

Current iteration: 9438
Current error: 0.000295573301807

Current iteration: 9439
Current error: 0.000291406979788

Current iteration: 9440
Current error: 0.00028730873007

Current iteration: 9441
Current error: 0.00028336673662

Current iteration: 9442
Current error: 0.000279418146431

Current iteration: 9443
Current error: 0.000355974481941

Current iteration: 9444
Current error: 0.000271680824725

Current iteration: 9445
Current error: 0.407353976904

Current iteration: 9446
Current error: 0.000424393782254

Current iteration: 9447
Current error: 0.000407152671619

Current iteration: 9448
Current error: 0.000402651759176

Current iteration: 9449
Current error: 0.000393397309404

Current iteration: 9450
Current error: 0.0120538318697

Current iteration: 9451
Current error: 0.000360002828981

Current iteration: 9452
Current error: 0.000354448005436

Current iteration: 9453
Current error: 0.00095305045849

Current iteration: 9454
Current error: 0.000340622645708

Current iteration: 9455
Current error: 0.000335481007276

Current iteration: 9456
Current error: 0.000330496935987

Current iteration: 9457
Current error: 0.000325513086779

Current iteration: 9458
Current error: 0.000320762728068

Current iteration: 9459
Current error: 0.000352011163516

Current iteration: 9460
Current error: 0.000311154489962

Current iteration: 9461
Current error: 0.000306625057956

Current iteration: 9462
Current error: 0.000302228576439

Current iteration: 9463
Current error: 0.00030295319223

Current iteration: 9464
Current error: 0.000293647654189

Current iteration: 9465
Current error: 0.000309467736283

Current iteration: 9466
Current error: 0.000285344845236

Current iteration: 9467
Current error: 0.000281421777485

Current iteration: 9468
Current error: 0.000277490606383

Current iteration: 9469
Current error: 0.000273690283297

Current iteration: 9470
Current error: 0.00027001468029

Current iteration: 9471
Current error: 0.000266324052664

Current iteration: 9472
Current error: 0.000262746553519

Current iteration: 9473
Current error: 0.000259229824057

Current iteration: 9474
Current error: 0.000255791724702

Current iteration: 9475
Current error: 0.359619040545

Current iteration: 9476
Current error: 0.000369307994406

Current iteration: 9477
Current error: 0.000363488242245

Current iteration: 9478
Current error: 0.000365539087136

Current iteration: 9479
Current error: 0.000352205210515

Current iteration: 9480
Current error: 0.00034683986837

Current iteration: 9481
Current error: 0.00688510434115

Current iteration: 9482
Current error: 0.305234055579

Current iteration: 9483
Current error: 0.000448160912102

Current iteration: 9484
Current error: 0.00044039684702

Current iteration: 9485
Current error: 0.000432811790406

Current iteration: 9486
Current error: 0.000425523941491

Current iteration: 9487
Current error: 0.000418297350165

Current iteration: 9488
Current error: 0.000411299255971

Current iteration: 9489
Current error: 0.00040453655911

Current iteration: 9490
Current error: 0.000397825165279

Current iteration: 9491
Current error: 0.000391491912459

Current iteration: 9492
Current error: 0.000385016176951

Current iteration: 9493
Current error: 0.00037889677249

Current iteration: 9494
Current error: 0.000373300467332

Current iteration: 9495
Current error: 0.000386235555829

Current iteration: 9496
Current error: 0.000361188056252

Current iteration: 9497
Current error: 0.000355381226673

Current iteration: 9498
Current error: 0.000349895399742

Current iteration: 9499
Current error: 0.000344565706324

Current iteration: 9500
Current error: 0.000339315629019

Current iteration: 9501
Current error: 0.000334216955527

Current iteration: 9502
Current error: 0.000329161692325

Current iteration: 9503
Current error: 0.33561770307

Current iteration: 9504
Current error: 0.000469503740882

Current iteration: 9505
Current error: 0.000461289634482

Current iteration: 9506
Current error: 0.000453123173108

Current iteration: 9507
Current error: 0.000445234383113

Current iteration: 9508
Current error: 0.000440607308767

Current iteration: 9509
Current error: 0.000430359250354

Current iteration: 9510
Current error: 0.000446794706467

Current iteration: 9511
Current error: 0.000422058187906

Current iteration: 9512
Current error: 0.000408527013582

Current iteration: 9513
Current error: 0.00040422163474

Current iteration: 9514
Current error: 0.000395212313004

Current iteration: 9515
Current error: 0.000409362212563

Current iteration: 9516
Current error: 0.000382622363732

Current iteration: 9517
Current error: 0.000376739392191

Current iteration: 9518
Current error: 0.000370302639041

Current iteration: 9519
Current error: 0.214155501986

Current iteration: 9520
Current error: 0.000683911976596

Current iteration: 9521
Current error: 0.000457833159863

Current iteration: 9522
Current error: 0.000449809662267

Current iteration: 9523
Current error: 0.000517003299017

Current iteration: 9524
Current error: 0.000433903047455

Current iteration: 9525
Current error: 0.000426519876033

Current iteration: 9526
Current error: 0.000419353427985

Current iteration: 9527
Current error: 0.000412341628788

Current iteration: 9528
Current error: 0.233006330392

Current iteration: 9529
Current error: 0.241160249992

Current iteration: 9530
Current error: 0.162236448251

Current iteration: 9531
Current error: 0.000871829193649

Current iteration: 9532
Current error: 0.000851083048375

Current iteration: 9533
Current error: 0.000831099634778

Current iteration: 9534
Current error: 0.00081196329588

Current iteration: 9535
Current error: 0.000793231841469

Current iteration: 9536
Current error: 0.000775363039668

Current iteration: 9537
Current error: 0.000757854881745

Current iteration: 9538
Current error: 0.000740976586058

Current iteration: 9539
Current error: 0.000724739073862

Current iteration: 9540
Current error: 0.000709007784296

Current iteration: 9541
Current error: 0.000693754445569

Current iteration: 9542
Current error: 0.153020549122

Current iteration: 9543
Current error: 0.000830944857499

Current iteration: 9544
Current error: 0.000904477981332

Current iteration: 9545
Current error: 0.000793591937372

Current iteration: 9546
Current error: 0.000779844902053

Current iteration: 9547
Current error: 0.000907442125506

Current iteration: 9548
Current error: 0.36284999348

Current iteration: 9549
Current error: 0.00111215972382

Current iteration: 9550
Current error: 0.00109109128649

Current iteration: 9551
Current error: 0.00107698162161

Current iteration: 9552
Current error: 0.00102645927385

Current iteration: 9553
Current error: 0.296193064809

Current iteration: 9554
Current error: 0.00143051248841

Current iteration: 9555
Current error: 0.00138326924202

Current iteration: 9556
Current error: 0.00143643606751

Current iteration: 9557
Current error: 0.00130203215028

Current iteration: 9558
Current error: 0.00126595406065

Current iteration: 9559
Current error: 0.00122933329225

Current iteration: 9560
Current error: 0.00119497792191

Current iteration: 9561
Current error: 0.0011617583406

Current iteration: 9562
Current error: 0.00113206455001

Current iteration: 9563
Current error: 0.0206222912897

Current iteration: 9564
Current error: 0.00100186541902

Current iteration: 9565
Current error: 0.000974206095813

Current iteration: 9566
Current error: 0.00172580881542

Current iteration: 9567
Current error: 0.000925306406911

Current iteration: 9568
Current error: 0.000896927132694

Current iteration: 9569
Current error: 0.000887419440941

Current iteration: 9570
Current error: 0.00226188452552

Current iteration: 9571
Current error: 0.000825383113422

Current iteration: 9572
Current error: 0.460685151966

Current iteration: 9573
Current error: 0.0013931989316

Current iteration: 9574
Current error: 0.00135804336467

Current iteration: 9575
Current error: 0.00131360279804

Current iteration: 9576
Current error: 0.0802620857111

Current iteration: 9577
Current error: 0.00108523528059

Current iteration: 9578
Current error: 0.00105684413812

Current iteration: 9579
Current error: 0.0366833756758

Current iteration: 9580
Current error: 0.000912484356475

Current iteration: 9581
Current error: 0.327923928776

Current iteration: 9582
Current error: 0.00129538920639

Current iteration: 9583
Current error: 0.00125738385471

Current iteration: 9584
Current error: 0.00137254604475

Current iteration: 9585
Current error: 0.00118627141322

Current iteration: 9586
Current error: 0.00115377495169

Current iteration: 9587
Current error: 0.0011224149884

Current iteration: 9588
Current error: 0.00109240589841

Current iteration: 9589
Current error: 0.00106361932407

Current iteration: 9590
Current error: 0.0242482428473

Current iteration: 9591
Current error: 0.000935035242312

Current iteration: 9592
Current error: 0.000911870684558

Current iteration: 9593
Current error: 0.000889793589618

Current iteration: 9594
Current error: 0.000868462790882

Current iteration: 9595
Current error: 0.000848020069324

Current iteration: 9596
Current error: 0.000828043075632

Current iteration: 9597
Current error: 0.000808838250512

Current iteration: 9598
Current error: 0.000790971820807

Current iteration: 9599
Current error: 0.14075759164

Current iteration: 9600
Current error: 0.00543411479222

Current iteration: 9601
Current error: 0.00117242644379

Current iteration: 9602
Current error: 0.000863099975195

Current iteration: 9603
Current error: 0.00084269612276

Current iteration: 9604
Current error: 0.000823065840423

Current iteration: 9605
Current error: 0.299051828078

Current iteration: 9606
Current error: 0.00114684368144

Current iteration: 9607
Current error: 0.00111670423539

Current iteration: 9608
Current error: 0.00120348224799

Current iteration: 9609
Current error: 0.00105718950283

Current iteration: 9610
Current error: 0.00102886625899

Current iteration: 9611
Current error: 0.0010024964407

Current iteration: 9612
Current error: 0.000977082591516

Current iteration: 9613
Current error: 0.000965478095834

Current iteration: 9614
Current error: 0.000929085180661

Current iteration: 9615
Current error: 0.137773793232

Current iteration: 9616
Current error: 0.00109541514589

Current iteration: 9617
Current error: 0.00106714423617

Current iteration: 9618
Current error: 0.00103831375416

Current iteration: 9619
Current error: 0.00101161104975

Current iteration: 9620
Current error: 0.119857878677

Current iteration: 9621
Current error: 0.0011742725111

Current iteration: 9622
Current error: 0.00114227850658

Current iteration: 9623
Current error: 0.00111153361758

Current iteration: 9624
Current error: 0.00119261068892

Current iteration: 9625
Current error: 0.00105223722208

Current iteration: 9626
Current error: 0.00102501178995

Current iteration: 9627
Current error: 0.000998787561239

Current iteration: 9628
Current error: 0.000973565131296

Current iteration: 9629
Current error: 0.000949234041006

Current iteration: 9630
Current error: 0.000925966961758

Current iteration: 9631
Current error: 0.000905055811805

Current iteration: 9632
Current error: 0.000881363472367

Current iteration: 9633
Current error: 0.000860350868092

Current iteration: 9634
Current error: 0.000840019152502

Current iteration: 9635
Current error: 0.000820744748643

Current iteration: 9636
Current error: 0.000801643202052

Current iteration: 9637
Current error: 0.000783376026925

Current iteration: 9638
Current error: 0.000765668958218

Current iteration: 9639
Current error: 0.00168633715614

Current iteration: 9640
Current error: 0.000724938124449

Current iteration: 9641
Current error: 0.000709131630691

Current iteration: 9642
Current error: 0.122439393697

Current iteration: 9643
Current error: 0.000841321058312

Current iteration: 9644
Current error: 0.000807983001727

Current iteration: 9645
Current error: 0.000790952540589

Current iteration: 9646
Current error: 0.000771604651277

Current iteration: 9647
Current error: 0.000754329123898

Current iteration: 9648
Current error: 0.000737629413311

Current iteration: 9649
Current error: 0.000728223539862

Current iteration: 9650
Current error: 0.0544574075734

Current iteration: 9651
Current error: 0.000613503742749

Current iteration: 9652
Current error: 0.000602287229887

Current iteration: 9653
Current error: 0.000593193229291

Current iteration: 9654
Current error: 0.000577534177961

Current iteration: 9655
Current error: 0.000570337650892

Current iteration: 9656
Current error: 0.000555375406181

Current iteration: 9657
Current error: 0.000544701308964

Current iteration: 9658
Current error: 0.000535228922108

Current iteration: 9659
Current error: 0.000526807528127

Current iteration: 9660
Current error: 0.000515353399652

Current iteration: 9661
Current error: 0.000567778395995

Current iteration: 9662
Current error: 0.000495707680824

Current iteration: 9663
Current error: 0.000486740040193

Current iteration: 9664
Current error: 0.00047866207273

Current iteration: 9665
Current error: 0.00046908278154

Current iteration: 9666
Current error: 0.000460787893574

Current iteration: 9667
Current error: 0.000452712650329

Current iteration: 9668
Current error: 0.000840513459518

Current iteration: 9669
Current error: 0.000435023064766

Current iteration: 9670
Current error: 0.000427286536221

Current iteration: 9671
Current error: 0.0142987722991

Current iteration: 9672
Current error: 0.00039105040048

Current iteration: 9673
Current error: 0.000381369584815

Current iteration: 9674
Current error: 0.000497669126119

Current iteration: 9675
Current error: 0.000368460440102

Current iteration: 9676
Current error: 0.000362667053491

Current iteration: 9677
Current error: 0.000356988016219

Current iteration: 9678
Current error: 0.000352068764179

Current iteration: 9679
Current error: 0.000452662537729

Current iteration: 9680
Current error: 0.000345105069324

Current iteration: 9681
Current error: 0.000335360363301

Current iteration: 9682
Current error: 0.000329942528138

Current iteration: 9683
Current error: 0.00032698337031

Current iteration: 9684
Current error: 0.000320228928538

Current iteration: 9685
Current error: 0.000315487121067

Current iteration: 9686
Current error: 0.170579597324

Current iteration: 9687
Current error: 0.000386035452138

Current iteration: 9688
Current error: 0.000395037740773

Current iteration: 9689
Current error: 0.000373386698256

Current iteration: 9690
Current error: 0.00036751766372

Current iteration: 9691
Current error: 0.00036178152462

Current iteration: 9692
Current error: 0.000356082278884

Current iteration: 9693
Current error: 0.000416045451096

Current iteration: 9694
Current error: 0.000344762476789

Current iteration: 9695
Current error: 0.0003395252496

Current iteration: 9696
Current error: 0.000335093032063

Current iteration: 9697
Current error: 0.000329358620886

Current iteration: 9698
Current error: 0.000324462303584

Current iteration: 9699
Current error: 0.000319668318524

Current iteration: 9700
Current error: 0.000314978728614

Current iteration: 9701
Current error: 0.214618503096

Current iteration: 9702
Current error: 0.000408979258474

Current iteration: 9703
Current error: 0.000396350962585

Current iteration: 9704
Current error: 0.000389892585559

Current iteration: 9705
Current error: 0.000383636927676

Current iteration: 9706
Current error: 0.000377460981481

Current iteration: 9707
Current error: 0.000371443332435

Current iteration: 9708
Current error: 0.000365595384726

Current iteration: 9709
Current error: 0.000359839433824

Current iteration: 9710
Current error: 0.000355381400824

Current iteration: 9711
Current error: 0.000348790379988

Current iteration: 9712
Current error: 0.000343452822649

Current iteration: 9713
Current error: 0.000338238254796

Current iteration: 9714
Current error: 0.000333392295211

Current iteration: 9715
Current error: 0.000328153137733

Current iteration: 9716
Current error: 0.00032328030505

Current iteration: 9717
Current error: 0.000319238316902

Current iteration: 9718
Current error: 0.185722062537

Current iteration: 9719
Current error: 0.156431937324

Current iteration: 9720
Current error: 0.000529440298816

Current iteration: 9721
Current error: 0.000480467893469

Current iteration: 9722
Current error: 0.00047193425894

Current iteration: 9723
Current error: 0.000948171916846

Current iteration: 9724
Current error: 0.000608426846624

Current iteration: 9725
Current error: 0.000443921402554

Current iteration: 9726
Current error: 0.000435748499414

Current iteration: 9727
Current error: 0.0145298839618

Current iteration: 9728
Current error: 0.000395167179871

Current iteration: 9729
Current error: 0.000394142894531

Current iteration: 9730
Current error: 0.000384516703396

Current iteration: 9731
Current error: 0.133013589876

Current iteration: 9732
Current error: 0.000451931299733

Current iteration: 9733
Current error: 0.000443484306903

Current iteration: 9734
Current error: 0.000435891273917

Current iteration: 9735
Current error: 0.000428450970915

Current iteration: 9736
Current error: 0.000421180667491

Current iteration: 9737
Current error: 0.000421795119865

Current iteration: 9738
Current error: 0.000408409997648

Current iteration: 9739
Current error: 0.000400465762219

Current iteration: 9740
Current error: 0.000394395923646

Current iteration: 9741
Current error: 0.0003895280182

Current iteration: 9742
Current error: 0.000381318534294

Current iteration: 9743
Current error: 0.000375161239632

Current iteration: 9744
Current error: 0.000369214258924

Current iteration: 9745
Current error: 0.000371850068367

Current iteration: 9746
Current error: 0.000357683925614

Current iteration: 9747
Current error: 0.000352125696103

Current iteration: 9748
Current error: 0.000346760073946

Current iteration: 9749
Current error: 0.0400743817938

Current iteration: 9750
Current error: 0.000301658663258

Current iteration: 9751
Current error: 0.000297529667454

Current iteration: 9752
Current error: 0.000294014012072

Current iteration: 9753
Current error: 0.000288999596428

Current iteration: 9754
Current error: 0.000284959017202

Current iteration: 9755
Current error: 0.000281195460378

Current iteration: 9756
Current error: 0.000277131647171

Current iteration: 9757
Current error: 0.000292242315234

Current iteration: 9758
Current error: 0.00026951194941

Current iteration: 9759
Current error: 0.0616083146692

Current iteration: 9760
Current error: 0.000230492757013

Current iteration: 9761
Current error: 0.000227588975087

Current iteration: 9762
Current error: 0.000224719281783

Current iteration: 9763
Current error: 0.00407931761768

Current iteration: 9764
Current error: 0.000243445217836

Current iteration: 9765
Current error: 0.000209226662605

Current iteration: 9766
Current error: 0.00020780445135

Current iteration: 9767
Current error: 0.00020426915113

Current iteration: 9768
Current error: 0.000201848597955

Current iteration: 9769
Current error: 0.000199481571081

Current iteration: 9770
Current error: 0.167114623547

Current iteration: 9771
Current error: 0.000244442216191

Current iteration: 9772
Current error: 0.000241360772601

Current iteration: 9773
Current error: 0.000241753561993

Current iteration: 9774
Current error: 0.000235222888645

Current iteration: 9775
Current error: 0.000232191563645

Current iteration: 9776
Current error: 0.000232927734241

Current iteration: 9777
Current error: 0.000226970299353

Current iteration: 9778
Current error: 0.000223639053523

Current iteration: 9779
Current error: 0.000220822523811

Current iteration: 9780
Current error: 0.000222143858399

Current iteration: 9781
Current error: 0.000215430629067

Current iteration: 9782
Current error: 0.000223148000194

Current iteration: 9783
Current error: 0.000210191981847

Current iteration: 9784
Current error: 0.0002076775604

Current iteration: 9785
Current error: 0.000205211971584

Current iteration: 9786
Current error: 0.0303802781008

Current iteration: 9787
Current error: 0.000182068225223

Current iteration: 9788
Current error: 0.000180036670893

Current iteration: 9789
Current error: 0.000179286410149

Current iteration: 9790
Current error: 0.000237768333304

Current iteration: 9791
Current error: 0.000173843042775

Current iteration: 9792
Current error: 0.000171968485838

Current iteration: 9793
Current error: 0.000170142832515

Current iteration: 9794
Current error: 0.000168236732549

Current iteration: 9795
Current error: 0.000166431991379

Current iteration: 9796
Current error: 0.0176056879482

Current iteration: 9797
Current error: 0.000151215018025

Current iteration: 9798
Current error: 0.000151623137292

Current iteration: 9799
Current error: 0.000150458303293

Current iteration: 9800
Current error: 0.000146639199516

Current iteration: 9801
Current error: 0.00014528155887

Current iteration: 9802
Current error: 0.000144382583895

Current iteration: 9803
Current error: 0.000143021823392

Current iteration: 9804
Current error: 0.000142150075356

Current iteration: 9805
Current error: 0.0331838926654

Current iteration: 9806
Current error: 0.000125115300351

Current iteration: 9807
Current error: 0.000123781393829

Current iteration: 9808
Current error: 0.000163502936667

Current iteration: 9809
Current error: 0.000121346326057

Current iteration: 9810
Current error: 0.000120230306262

Current iteration: 9811
Current error: 0.000119128107321

Current iteration: 9812
Current error: 0.000118056940974

Current iteration: 9813
Current error: 0.000116986690842

Current iteration: 9814
Current error: 0.000127151170941

Current iteration: 9815
Current error: 0.349695820515

Current iteration: 9816
Current error: 0.0132555129656

Current iteration: 9817
Current error: 0.000156238298042

Current iteration: 9818
Current error: 0.000154653628908

Current iteration: 9819
Current error: 0.000153024029983

Current iteration: 9820
Current error: 0.265718001719

Current iteration: 9821
Current error: 0.000206447779922

Current iteration: 9822
Current error: 0.000204463955376

Current iteration: 9823
Current error: 0.000201602300443

Current iteration: 9824
Current error: 0.235297720178

Current iteration: 9825
Current error: 0.000264523832809

Current iteration: 9826
Current error: 0.000260866546881

Current iteration: 9827
Current error: 0.000257410530306

Current iteration: 9828
Current error: 0.000254038109073

Current iteration: 9829
Current error: 0.000250687934832

Current iteration: 9830
Current error: 0.000247393380096

Current iteration: 9831
Current error: 0.000244274226653

Current iteration: 9832
Current error: 0.000241063935896

Current iteration: 9833
Current error: 0.000237978087609

Current iteration: 9834
Current error: 0.000234941329642

Current iteration: 9835
Current error: 0.000231980821576

Current iteration: 9836
Current error: 0.000229057215148

Current iteration: 9837
Current error: 0.000226322001672

Current iteration: 9838
Current error: 0.000322868853003

Current iteration: 9839
Current error: 0.0288291779081

Current iteration: 9840
Current error: 0.000197916472314

Current iteration: 9841
Current error: 0.00382605413358

Current iteration: 9842
Current error: 0.000187027999098

Current iteration: 9843
Current error: 0.00018488991365

Current iteration: 9844
Current error: 0.170106491821

Current iteration: 9845
Current error: 0.000227360337645

Current iteration: 9846
Current error: 0.000225684467614

Current iteration: 9847
Current error: 0.000221743186343

Current iteration: 9848
Current error: 0.00023238095404

Current iteration: 9849
Current error: 0.000216274123322

Current iteration: 9850
Current error: 0.000213648134661

Current iteration: 9851
Current error: 0.262740080314

Current iteration: 9852
Current error: 0.000289195535668

Current iteration: 9853
Current error: 0.000285158220675

Current iteration: 9854
Current error: 0.000282871809356

Current iteration: 9855
Current error: 0.000277296043097

Current iteration: 9856
Current error: 0.000273508853394

Current iteration: 9857
Current error: 0.000270047293567

Current iteration: 9858
Current error: 0.000266113504767

Current iteration: 9859
Current error: 0.000568399343369

Current iteration: 9860
Current error: 0.144439262596

Current iteration: 9861
Current error: 0.000314336479613

Current iteration: 9862
Current error: 0.000309759009475

Current iteration: 9863
Current error: 0.000305306264868

Current iteration: 9864
Current error: 0.000300920179801

Current iteration: 9865
Current error: 0.000296632373991

Current iteration: 9866
Current error: 0.000292399608884

Current iteration: 9867
Current error: 0.000288310590832

Current iteration: 9868
Current error: 0.00727888500013

Current iteration: 9869
Current error: 0.000267963592538

Current iteration: 9870
Current error: 0.000264150375185

Current iteration: 9871
Current error: 0.000279259853744

Current iteration: 9872
Current error: 0.000257040960973

Current iteration: 9873
Current error: 0.000253768598814

Current iteration: 9874
Current error: 0.000250293281205

Current iteration: 9875
Current error: 0.000247141167144

Current iteration: 9876
Current error: 0.00026140154025

Current iteration: 9877
Current error: 0.000240597570132

Current iteration: 9878
Current error: 0.000237510313382

Current iteration: 9879
Current error: 0.000256586397453

Current iteration: 9880
Current error: 0.140628641259

Current iteration: 9881
Current error: 0.000281319056562

Current iteration: 9882
Current error: 0.000285250149482

Current iteration: 9883
Current error: 0.000273508211434

Current iteration: 9884
Current error: 0.000269783358158

Current iteration: 9885
Current error: 0.000266138955806

Current iteration: 9886
Current error: 0.132350958953

Current iteration: 9887
Current error: 0.000317103115072

Current iteration: 9888
Current error: 0.0770664153562

Current iteration: 9889
Current error: 0.000311908624365

Current iteration: 9890
Current error: 0.000262471036384

Current iteration: 9891
Current error: 0.00025899306312

Current iteration: 9892
Current error: 0.000255540560819

Current iteration: 9893
Current error: 0.000252166462786

Current iteration: 9894
Current error: 0.00631614337058

Current iteration: 9895
Current error: 0.000235696138676

Current iteration: 9896
Current error: 0.000232081722193

Current iteration: 9897
Current error: 0.000241502669732

Current iteration: 9898
Current error: 0.000226209751822

Current iteration: 9899
Current error: 0.000223426475433

Current iteration: 9900
Current error: 0.000220693112391

Current iteration: 9901
Current error: 0.00030105002352

Current iteration: 9902
Current error: 0.000215309781301

Current iteration: 9903
Current error: 0.000212281351568

Current iteration: 9904
Current error: 0.00021002449987

Current iteration: 9905
Current error: 0.000207210413826

Current iteration: 9906
Current error: 0.000205393263336

Current iteration: 9907
Current error: 0.000202332513502

Current iteration: 9908
Current error: 0.000199932511516

Current iteration: 9909
Current error: 0.000198246998498

Current iteration: 9910
Current error: 0.000195325992867

Current iteration: 9911
Current error: 0.000193044682171

Current iteration: 9912
Current error: 0.00019081683059

Current iteration: 9913
Current error: 0.000193594880305

Current iteration: 9914
Current error: 0.000186480102349

Current iteration: 9915
Current error: 0.000184369523986

Current iteration: 9916
Current error: 0.000182309929116

Current iteration: 9917
Current error: 0.000180280817098

Current iteration: 9918
Current error: 0.000178267310439

Current iteration: 9919
Current error: 0.000176328106368

Current iteration: 9920
Current error: 0.000174359435002

Current iteration: 9921
Current error: 0.000172655744797

Current iteration: 9922
Current error: 0.000171614791664

Current iteration: 9923
Current error: 0.00016872921953

Current iteration: 9924
Current error: 0.000166913701439

Current iteration: 9925
Current error: 0.00016571350636

Current iteration: 9926
Current error: 0.000163362131851

Current iteration: 9927
Current error: 0.000161636904087

Current iteration: 9928
Current error: 0.000159937800221

Current iteration: 9929
Current error: 0.000158252724766

Current iteration: 9930
Current error: 0.000156603525808

Current iteration: 9931
Current error: 0.000159429054515

Current iteration: 9932
Current error: 0.00015335385944

Current iteration: 9933
Current error: 0.000151818417227

Current iteration: 9934
Current error: 0.000150278235266

Current iteration: 9935
Current error: 0.000149309553096

Current iteration: 9936
Current error: 0.000147725356672

Current iteration: 9937
Current error: 0.00014570455311

Current iteration: 9938
Current error: 0.000144255519003

Current iteration: 9939
Current error: 0.000143044682173

Current iteration: 9940
Current error: 0.000142124089056

Current iteration: 9941
Current error: 0.000139997889326

Current iteration: 9942
Current error: 0.000280796852965

Current iteration: 9943
Current error: 0.000136742578502

Current iteration: 9944
Current error: 0.000135427961862

Current iteration: 9945
Current error: 0.167664102051

Current iteration: 9946
Current error: 0.000166855702804

Current iteration: 9947
Current error: 0.000165068620991

Current iteration: 9948
Current error: 0.000163311654108

Current iteration: 9949
Current error: 0.000161595530848

Current iteration: 9950
Current error: 0.000160142725772

Current iteration: 9951
Current error: 0.000158202970898

Current iteration: 9952
Current error: 0.000157838826115

Current iteration: 9953
Current error: 0.000154942427297

Current iteration: 9954
Current error: 0.000153329420006

Current iteration: 9955
Current error: 0.137530162686

Current iteration: 9956
Current error: 0.000185633393894

Current iteration: 9957
Current error: 0.000181940242139

Current iteration: 9958
Current error: 0.000179636533405

Current iteration: 9959
Current error: 0.00018272425034

Current iteration: 9960
Current error: 0.000178565844057

Current iteration: 9961
Current error: 0.00017367403221

Current iteration: 9962
Current error: 0.000171778424355

Current iteration: 9963
Current error: 0.0226545334508

Current iteration: 9964
Current error: 0.000154223191147

Current iteration: 9965
Current error: 0.000152698911729

Current iteration: 9966
Current error: 0.481125646234

Current iteration: 9967
Current error: 0.000269771979247

Current iteration: 9968
Current error: 0.000264160683856

Current iteration: 9969
Current error: 0.000261704422809

Current iteration: 9970
Current error: 0.000257127854188

Current iteration: 9971
Current error: 0.000253760304452

Current iteration: 9972
Current error: 0.21128238053

Current iteration: 9973
Current error: 0.000328494111771

Current iteration: 9974
Current error: 0.000323638563218

Current iteration: 9975
Current error: 0.000318974402198

Current iteration: 9976
Current error: 0.000349422479279

Current iteration: 9977
Current error: 0.000309393994487

Current iteration: 9978
Current error: 0.106627894289

Current iteration: 9979
Current error: 0.000359112413552

Current iteration: 9980
Current error: 0.000353558844782

Current iteration: 9981
Current error: 0.000348112484234

Current iteration: 9982
Current error: 0.00063727601502

Current iteration: 9983
Current error: 0.000335960729248

Current iteration: 9984
Current error: 0.000330858631965

Current iteration: 9985
Current error: 0.000327785126317

Current iteration: 9986
Current error: 0.000321173115914

Current iteration: 9987
Current error: 0.10195356639

Current iteration: 9988
Current error: 0.000264807145071

Current iteration: 9989
Current error: 0.000261282734093

Current iteration: 9990
Current error: 0.000259162023595

Current iteration: 9991
Current error: 0.000254388974403

Current iteration: 9992
Current error: 0.000251160952872

Current iteration: 9993
Current error: 0.000247752426498

Current iteration: 9994
Current error: 0.000554166382573

Current iteration: 9995
Current error: 0.000240010850483

Current iteration: 9996
Current error: 0.000236890485096

Current iteration: 9997
Current error: 0.000233896044194

Current iteration: 9998
Current error: 0.000230969718627

Current iteration: 9999
Current error: 0.000230681207839

Current iteration: 10000
Current error: 0.000226802774441

Current iteration: 10001
Current error: 0.000222399283694

Current iteration: 10002
Current error: 0.000249358739907

Current iteration: 10003
Current error: 0.000216809772211

Current iteration: 10004
Current error: 0.000214663824349

Current iteration: 10005
Current error: 0.000211577535174

Current iteration: 10006
Current error: 0.000209095911227

Current iteration: 10007
Current error: 0.000256183620566

Current iteration: 10008
Current error: 0.000203845480656

Current iteration: 10009
Current error: 0.000201432784429

Current iteration: 10010
Current error: 0.000199071632195

Current iteration: 10011
Current error: 0.000196741196809

Current iteration: 10012
Current error: 0.259017099203

Current iteration: 10013
Current error: 0.000266559444352

Current iteration: 10014
Current error: 0.000266198809436

Current iteration: 10015
Current error: 0.000277496965569

Current iteration: 10016
Current error: 0.000255865230119

Current iteration: 10017
Current error: 0.0879517001102

Current iteration: 10018
Current error: 0.0125187349292

Current iteration: 10019
Current error: 0.000198392703351

Current iteration: 10020
Current error: 0.000195362801589

Current iteration: 10021
Current error: 0.000193135948452

Current iteration: 10022
Current error: 0.000194028016348

Current iteration: 10023
Current error: 0.000188831000031

Current iteration: 10024
Current error: 0.00020555407537

Current iteration: 10025
Current error: 0.000184396698807

Current iteration: 10026
Current error: 0.000182266396372

Current iteration: 10027
Current error: 0.000180238536926

Current iteration: 10028
Current error: 0.000178309820173

Current iteration: 10029
Current error: 0.000176265211485

Current iteration: 10030
Current error: 0.000180352061675

Current iteration: 10031
Current error: 0.000172392419723

Current iteration: 10032
Current error: 0.000170554913112

Current iteration: 10033
Current error: 0.0862837064768

Current iteration: 10034
Current error: 0.00014316561785

Current iteration: 10035
Current error: 0.000141734218189

Current iteration: 10036
Current error: 0.000142798252921

Current iteration: 10037
Current error: 0.000319565860935

Current iteration: 10038
Current error: 0.000204825119473

Current iteration: 10039
Current error: 0.000135695100332

Current iteration: 10040
Current error: 0.000140248558256

Current iteration: 10041
Current error: 0.050423034

Current iteration: 10042
Current error: 0.000116128476348

Current iteration: 10043
Current error: 0.000115093327641

Current iteration: 10044
Current error: 0.00011406650911

Current iteration: 10045
Current error: 0.000113815119666

Current iteration: 10046
Current error: 0.0626267807056

Current iteration: 10047
Current error: 0.000716442730471

Current iteration: 10048
Current error: 9.66354303054e-05

Current iteration: 10049
Current error: 9.59003612325e-05

Current iteration: 10050
Current error: 9.35736625234e-05

Current iteration: 10051
Current error: 9.28277765189e-05

Current iteration: 10052
Current error: 0.179667438299

Current iteration: 10053
Current error: 0.000115551638564

Current iteration: 10054
Current error: 0.000114077846406

Current iteration: 10055
Current error: 0.000113240074869

Current iteration: 10056
Current error: 0.000196015877755

Current iteration: 10057
Current error: 0.000110824372306

Current iteration: 10058
Current error: 0.19453320391

Current iteration: 10059
Current error: 0.000140093737847

Current iteration: 10060
Current error: 0.000151812739439

Current iteration: 10061
Current error: 0.0306968444812

Current iteration: 10062
Current error: 0.000122928697434

Current iteration: 10063
Current error: 0.000122177148804

Current iteration: 10064
Current error: 0.000120676604737

Current iteration: 10065
Current error: 0.000119582518858

Current iteration: 10066
Current error: 0.000118494436001

Current iteration: 10067
Current error: 0.000133926713896

Current iteration: 10068
Current error: 0.00461252413553

Current iteration: 10069
Current error: 0.000110903187908

Current iteration: 10070
Current error: 0.000110006016356

Current iteration: 10071
Current error: 0.0573464679581

Current iteration: 10072
Current error: 9.75321251169e-05

Current iteration: 10073
Current error: 0.0242299309739

Current iteration: 10074
Current error: 0.0119783729005

Current iteration: 10075
Current error: 0.198650340099

Current iteration: 10076
Current error: 0.000115137320985

Current iteration: 10077
Current error: 0.000100075797477

Current iteration: 10078
Current error: 9.92457666507e-05

Current iteration: 10079
Current error: 9.84504374222e-05

Current iteration: 10080
Current error: 9.76302978624e-05

Current iteration: 10081
Current error: 0.00955628087216

Current iteration: 10082
Current error: 9.06706529602e-05

Current iteration: 10083
Current error: 8.99013617154e-05

Current iteration: 10084
Current error: 8.92172799686e-05

Current iteration: 10085
Current error: 0.000665288389179

Current iteration: 10086
Current error: 0.158207283307

Current iteration: 10087
Current error: 0.00011227697032

Current iteration: 10088
Current error: 0.00174815566129

Current iteration: 10089
Current error: 0.000102662388166

Current iteration: 10090
Current error: 0.000102024354891

Current iteration: 10091
Current error: 0.000101093589213

Current iteration: 10092
Current error: 0.000100111187908

Current iteration: 10093
Current error: 9.92868610286e-05

Current iteration: 10094
Current error: 9.84397949593e-05

Current iteration: 10095
Current error: 9.76373811644e-05

Current iteration: 10096
Current error: 9.68256133265e-05

Current iteration: 10097
Current error: 9.6032687807e-05

Current iteration: 10098
Current error: 9.52869583141e-05

Current iteration: 10099
Current error: 9.44722671711e-05

Current iteration: 10100
Current error: 9.37031412672e-05

Current iteration: 10101
Current error: 0.000101522258075

Current iteration: 10102
Current error: 9.23024548973e-05

Current iteration: 10103
Current error: 9.15869187131e-05

Current iteration: 10104
Current error: 0.000100485010627

Current iteration: 10105
Current error: 8.9985898756e-05

Current iteration: 10106
Current error: 8.92533550768e-05

Current iteration: 10107
Current error: 0.000356988105113

Current iteration: 10108
Current error: 8.7438535792e-05

Current iteration: 10109
Current error: 8.65329195367e-05

Current iteration: 10110
Current error: 8.58750138651e-05

Current iteration: 10111
Current error: 8.52081009319e-05

Current iteration: 10112
Current error: 0.14878721149

Current iteration: 10113
Current error: 0.000102946254759

Current iteration: 10114
Current error: 0.0567073897554

Current iteration: 10115
Current error: 8.88634889799e-05

Current iteration: 10116
Current error: 0.0484302656128

Current iteration: 10117
Current error: 7.81553437043e-05

Current iteration: 10118
Current error: 7.68706541034e-05

Current iteration: 10119
Current error: 7.65189479711e-05

Current iteration: 10120
Current error: 7.57642341112e-05

Current iteration: 10121
Current error: 7.51946713889e-05

Current iteration: 10122
Current error: 0.000118558331107

Current iteration: 10123
Current error: 7.39824147289e-05

Current iteration: 10124
Current error: 0.20505005126

Current iteration: 10125
Current error: 9.41859396792e-05

Current iteration: 10126
Current error: 9.3427401193e-05

Current iteration: 10127
Current error: 0.207886878198

Current iteration: 10128
Current error: 0.000121737619416

Current iteration: 10129
Current error: 0.000119154190261

Current iteration: 10130
Current error: 0.00015468924608

Current iteration: 10131
Current error: 0.138597446173

Current iteration: 10132
Current error: 0.000141097538277

Current iteration: 10133
Current error: 0.000139705383799

Current iteration: 10134
Current error: 0.000141166534307

Current iteration: 10135
Current error: 0.000137633908842

Current iteration: 10136
Current error: 0.000135714547429

Current iteration: 10137
Current error: 0.000254084397307

Current iteration: 10138
Current error: 0.000166882844004

Current iteration: 10139
Current error: 0.000195106658912

Current iteration: 10140
Current error: 0.000129682363898

Current iteration: 10141
Current error: 0.000128512772225

Current iteration: 10142
Current error: 0.000127257059325

Current iteration: 10143
Current error: 0.000126051856146

Current iteration: 10144
Current error: 0.000124885194101

Current iteration: 10145
Current error: 0.000123717141773

Current iteration: 10146
Current error: 0.000122569139432

Current iteration: 10147
Current error: 0.000122738863573

Current iteration: 10148
Current error: 0.000120332854011

Current iteration: 10149
Current error: 0.014595262596

Current iteration: 10150
Current error: 0.000109989293834

Current iteration: 10151
Current error: 0.000109034523192

Current iteration: 10152
Current error: 0.000108142368329

Current iteration: 10153
Current error: 0.000107146722065

Current iteration: 10154
Current error: 0.000106227737257

Current iteration: 10155
Current error: 0.204766298398

Current iteration: 10156
Current error: 0.000136697376764

Current iteration: 10157
Current error: 0.000135466341028

Current iteration: 10158
Current error: 0.0701557730667

Current iteration: 10159
Current error: 0.000127134070293

Current iteration: 10160
Current error: 0.000113906811593

Current iteration: 10161
Current error: 0.000161275885341

Current iteration: 10162
Current error: 0.000111784289944

Current iteration: 10163
Current error: 0.000110748942753

Current iteration: 10164
Current error: 0.000110125325016

Current iteration: 10165
Current error: 0.000108822390663

Current iteration: 10166
Current error: 0.000107875085456

Current iteration: 10167
Current error: 0.000111553808228

Current iteration: 10168
Current error: 0.000105998916553

Current iteration: 10169
Current error: 0.0384746212865

Current iteration: 10170
Current error: 0.074256275567

Current iteration: 10171
Current error: 9.94993195966e-05

Current iteration: 10172
Current error: 7.92517558041e-05

Current iteration: 10173
Current error: 7.87056667082e-05

Current iteration: 10174
Current error: 7.80639820718e-05

Current iteration: 10175
Current error: 7.75584966142e-05

Current iteration: 10176
Current error: 7.69310551958e-05

Current iteration: 10177
Current error: 7.6366089103e-05

Current iteration: 10178
Current error: 7.58056891973e-05

Current iteration: 10179
Current error: 7.79374432707e-05

Current iteration: 10180
Current error: 7.46969977506e-05

Current iteration: 10181
Current error: 7.41644756264e-05

Current iteration: 10182
Current error: 7.36252875287e-05

Current iteration: 10183
Current error: 7.31049965006e-05

Current iteration: 10184
Current error: 7.25846029441e-05

Current iteration: 10185
Current error: 7.20680186964e-05

Current iteration: 10186
Current error: 7.1553083459e-05

Current iteration: 10187
Current error: 7.1382177463e-05

Current iteration: 10188
Current error: 7.05452679883e-05

Current iteration: 10189
Current error: 7.09863534826e-05

Current iteration: 10190
Current error: 6.95569287883e-05

Current iteration: 10191
Current error: 6.90726770106e-05

Current iteration: 10192
Current error: 6.86047998955e-05

Current iteration: 10193
Current error: 6.811932948e-05

Current iteration: 10194
Current error: 6.77244975834e-05

Current iteration: 10195
Current error: 6.71830552242e-05

Current iteration: 10196
Current error: 6.67064034987e-05

Current iteration: 10197
Current error: 6.62724577133e-05

Current iteration: 10198
Current error: 7.14836799713e-05

Current iteration: 10199
Current error: 6.5351737703e-05

Current iteration: 10200
Current error: 6.4909467738e-05

Current iteration: 10201
Current error: 6.44737754388e-05

Current iteration: 10202
Current error: 6.40552291735e-05

Current iteration: 10203
Current error: 6.36284712185e-05

Current iteration: 10204
Current error: 8.18765015897e-05

Current iteration: 10205
Current error: 6.2862507673e-05

Current iteration: 10206
Current error: 6.25896150666e-05

Current iteration: 10207
Current error: 6.18854285373e-05

Current iteration: 10208
Current error: 6.14950359658e-05

Current iteration: 10209
Current error: 6.11417748191e-05

Current iteration: 10210
Current error: 6.0674899952e-05

Current iteration: 10211
Current error: 6.02867185943e-05

Current iteration: 10212
Current error: 6.02973285748e-05

Current iteration: 10213
Current error: 5.95039931337e-05

Current iteration: 10214
Current error: 5.91235757429e-05

Current iteration: 10215
Current error: 5.87402218202e-05

Current iteration: 10216
Current error: 5.84311281087e-05

Current iteration: 10217
Current error: 5.79838961943e-05

Current iteration: 10218
Current error: 5.76186369407e-05

Current iteration: 10219
Current error: 5.72529653599e-05

Current iteration: 10220
Current error: 5.69004244186e-05

Current iteration: 10221
Current error: 5.65237412142e-05

Current iteration: 10222
Current error: 5.61760775853e-05

Current iteration: 10223
Current error: 7.07095571827e-05

Current iteration: 10224
Current error: 7.44621555613e-05

Current iteration: 10225
Current error: 5.5037082938e-05

Current iteration: 10226
Current error: 5.46977394046e-05

Current iteration: 10227
Current error: 5.64686169947e-05

Current iteration: 10228
Current error: 5.41048753477e-05

Current iteration: 10229
Current error: 5.36810416007e-05

Current iteration: 10230
Current error: 5.33568170524e-05

Current iteration: 10231
Current error: 5.31193615547e-05

Current iteration: 10232
Current error: 0.00356100113613

Current iteration: 10233
Current error: 5.05337570079e-05

Current iteration: 10234
Current error: 9.79699819824e-05

Current iteration: 10235
Current error: 4.98292233845e-05

Current iteration: 10236
Current error: 4.95584225579e-05

Current iteration: 10237
Current error: 4.92441928062e-05

Current iteration: 10238
Current error: 4.89538143968e-05

Current iteration: 10239
Current error: 4.86663033637e-05

Current iteration: 10240
Current error: 4.939031068e-05

Current iteration: 10241
Current error: 4.81084321842e-05

Current iteration: 10242
Current error: 4.78193408465e-05

Current iteration: 10243
Current error: 5.22652867218e-05

Current iteration: 10244
Current error: 4.72754908129e-05

Current iteration: 10245
Current error: 4.69958057191e-05

Current iteration: 10246
Current error: 4.67123504198e-05

Current iteration: 10247
Current error: 0.472382510166

Current iteration: 10248
Current error: 7.89410244775e-05

Current iteration: 10249
Current error: 7.83643949937e-05

Current iteration: 10250
Current error: 7.81396022013e-05

Current iteration: 10251
Current error: 7.79215489414e-05

Current iteration: 10252
Current error: 7.66338837054e-05

Current iteration: 10253
Current error: 7.60697325099e-05

Current iteration: 10254
Current error: 0.24012587309

Current iteration: 10255
Current error: 0.000100898875775

Current iteration: 10256
Current error: 0.176148396618

Current iteration: 10257
Current error: 0.000126072688598

Current iteration: 10258
Current error: 0.000124931856596

Current iteration: 10259
Current error: 0.000144797114214

Current iteration: 10260
Current error: 0.000122499136134

Current iteration: 10261
Current error: 0.000121675253772

Current iteration: 10262
Current error: 0.00012026985091

Current iteration: 10263
Current error: 0.120557575598

Current iteration: 10264
Current error: 0.00014252668662

Current iteration: 10265
Current error: 0.000141154361798

Current iteration: 10266
Current error: 0.000139824040041

Current iteration: 10267
Current error: 0.000143122747853

Current iteration: 10268
Current error: 0.00013696501147

Current iteration: 10269
Current error: 0.000135627401743

Current iteration: 10270
Current error: 0.000134311617534

Current iteration: 10271
Current error: 0.000133014208036

Current iteration: 10272
Current error: 0.000131733148347

Current iteration: 10273
Current error: 0.0001304861266

Current iteration: 10274
Current error: 0.000129247604886

Current iteration: 10275
Current error: 0.000128021653577

Current iteration: 10276
Current error: 0.00355957516991

Current iteration: 10277
Current error: 0.000887235874036

Current iteration: 10278
Current error: 0.000118694983382

Current iteration: 10279
Current error: 0.125221468487

Current iteration: 10280
Current error: 0.000141211166192

Current iteration: 10281
Current error: 0.000139826292739

Current iteration: 10282
Current error: 0.000138447979486

Current iteration: 10283
Current error: 0.0693701999655

Current iteration: 10284
Current error: 0.000117546756614

Current iteration: 10285
Current error: 0.00011648051087

Current iteration: 10286
Current error: 0.000115757209215

Current iteration: 10287
Current error: 0.000114812905226

Current iteration: 10288
Current error: 0.000113394958683

Current iteration: 10289
Current error: 0.000318067177143

Current iteration: 10290
Current error: 0.0677551050906

Current iteration: 10291
Current error: 0.008348436684

Current iteration: 10292
Current error: 8.93400144893e-05

Current iteration: 10293
Current error: 8.86358719376e-05

Current iteration: 10294
Current error: 8.79397472329e-05

Current iteration: 10295
Current error: 8.74513161663e-05

Current iteration: 10296
Current error: 8.94814593772e-05

Current iteration: 10297
Current error: 8.58731766899e-05

Current iteration: 10298
Current error: 8.55471840849e-05

Current iteration: 10299
Current error: 8.47008740408e-05

Current iteration: 10300
Current error: 9.17018561229e-05

Current iteration: 10301
Current error: 8.32405026734e-05

Current iteration: 10302
Current error: 8.33082206769e-05

Current iteration: 10303
Current error: 9.3614433037e-05

Current iteration: 10304
Current error: 8.13281879826e-05

Current iteration: 10305
Current error: 8.30985670837e-05

Current iteration: 10306
Current error: 8.01005487519e-05

Current iteration: 10307
Current error: 8.09361036237e-05

Current iteration: 10308
Current error: 7.89051501196e-05

Current iteration: 10309
Current error: 7.83253579984e-05

Current iteration: 10310
Current error: 0.152098797268

Current iteration: 10311
Current error: 0.00014317940766

Current iteration: 10312
Current error: 9.4715154709e-05

Current iteration: 10313
Current error: 9.54558276788e-05

Current iteration: 10314
Current error: 9.32209720065e-05

Current iteration: 10315
Current error: 9.24380622919e-05

Current iteration: 10316
Current error: 9.16901302123e-05

Current iteration: 10317
Current error: 9.09546410222e-05

Current iteration: 10318
Current error: 9.02660024037e-05

Current iteration: 10319
Current error: 8.95342444678e-05

Current iteration: 10320
Current error: 8.8864417098e-05

Current iteration: 10321
Current error: 8.81192656081e-05

Current iteration: 10322
Current error: 8.74312086778e-05

Current iteration: 10323
Current error: 9.25527952628e-05

Current iteration: 10324
Current error: 0.208307352773

Current iteration: 10325
Current error: 0.000111690639354

Current iteration: 10326
Current error: 0.000110692505896

Current iteration: 10327
Current error: 0.00010990198005

Current iteration: 10328
Current error: 0.000108737868791

Current iteration: 10329
Current error: 0.000170151051831

Current iteration: 10330
Current error: 0.000106645534009

Current iteration: 10331
Current error: 0.000105720874658

Current iteration: 10332
Current error: 0.000105070782266

Current iteration: 10333
Current error: 0.000103919343483

Current iteration: 10334
Current error: 0.000103284351982

Current iteration: 10335
Current error: 0.0483946398747

Current iteration: 10336
Current error: 8.94408563824e-05

Current iteration: 10337
Current error: 8.87503960912e-05

Current iteration: 10338
Current error: 8.80367081082e-05

Current iteration: 10339
Current error: 8.73461408166e-05

Current iteration: 10340
Current error: 8.66605068298e-05

Current iteration: 10341
Current error: 8.59843697287e-05

Current iteration: 10342
Current error: 8.53161786204e-05

Current iteration: 10343
Current error: 0.0849638414095

Current iteration: 10344
Current error: 7.19685332578e-05

Current iteration: 10345
Current error: 0.0250997320443

Current iteration: 10346
Current error: 0.000147131221336

Current iteration: 10347
Current error: 6.39126675579e-05

Current iteration: 10348
Current error: 6.38004674652e-05

Current iteration: 10349
Current error: 6.30793190738e-05

Current iteration: 10350
Current error: 6.26416929436e-05

Current iteration: 10351
Current error: 0.473706652291

Current iteration: 10352
Current error: 0.000106869777468

Current iteration: 10353
Current error: 0.00010589482874

Current iteration: 10354
Current error: 0.0523492003815

Current iteration: 10355
Current error: 9.15848411671e-05

Current iteration: 10356
Current error: 9.08492512202e-05

Current iteration: 10357
Current error: 9.01310880384e-05

Current iteration: 10358
Current error: 8.94173255591e-05

Current iteration: 10359
Current error: 8.87316317816e-05

Current iteration: 10360
Current error: 8.80168745771e-05

Current iteration: 10361
Current error: 8.73071510112e-05

Current iteration: 10362
Current error: 8.66532711644e-05

Current iteration: 10363
Current error: 0.0470708056526

Current iteration: 10364
Current error: 8.04519039972e-05

Current iteration: 10365
Current error: 7.49262665291e-05

Current iteration: 10366
Current error: 0.0167343718855

Current iteration: 10367
Current error: 6.84023683576e-05

Current iteration: 10368
Current error: 6.79295102774e-05

Current iteration: 10369
Current error: 6.74925774907e-05

Current iteration: 10370
Current error: 6.71017513563e-05

Current iteration: 10371
Current error: 6.65397119614e-05

Current iteration: 10372
Current error: 6.6085622263e-05

Current iteration: 10373
Current error: 6.56356350248e-05

Current iteration: 10374
Current error: 7.7427194065e-05

Current iteration: 10375
Current error: 6.47211823179e-05

Current iteration: 10376
Current error: 6.42789290259e-05

Current iteration: 10377
Current error: 6.38577538339e-05

Current iteration: 10378
Current error: 6.36653926357e-05

Current iteration: 10379
Current error: 6.29978326212e-05

Current iteration: 10380
Current error: 6.25822255633e-05

Current iteration: 10381
Current error: 6.23969070869e-05

Current iteration: 10382
Current error: 6.17527294611e-05

Current iteration: 10383
Current error: 6.13469989633e-05

Current iteration: 10384
Current error: 6.09498601992e-05

Current iteration: 10385
Current error: 6.13043716164e-05

Current iteration: 10386
Current error: 7.09809498929e-05

Current iteration: 10387
Current error: 5.97289106921e-05

Current iteration: 10388
Current error: 5.93479978136e-05

Current iteration: 10389
Current error: 0.0192207508247

Current iteration: 10390
Current error: 0.0277890472644

Current iteration: 10391
Current error: 5.00644066391e-05

Current iteration: 10392
Current error: 4.8395300794e-05

Current iteration: 10393
Current error: 4.81184756908e-05

Current iteration: 10394
Current error: 4.78496922352e-05

Current iteration: 10395
Current error: 5.27519114747e-05

Current iteration: 10396
Current error: 0.0221602094214

Current iteration: 10397
Current error: 4.30579173418e-05

Current iteration: 10398
Current error: 4.28232416338e-05

Current iteration: 10399
Current error: 4.3049202536e-05

Current iteration: 10400
Current error: 4.23549609972e-05

Current iteration: 10401
Current error: 4.21617037979e-05

Current iteration: 10402
Current error: 4.19045614986e-05

Current iteration: 10403
Current error: 4.16735459155e-05

Current iteration: 10404
Current error: 4.14429029483e-05

Current iteration: 10405
Current error: 4.12155262792e-05

Current iteration: 10406
Current error: 5.47316059333e-05

Current iteration: 10407
Current error: 4.08322501776e-05

Current iteration: 10408
Current error: 4.05243585639e-05

Current iteration: 10409
Current error: 4.03085645666e-05

Current iteration: 10410
Current error: 8.10719697068e-05

Current iteration: 10411
Current error: 3.98982600604e-05

Current iteration: 10412
Current error: 3.96057843151e-05

Current iteration: 10413
Current error: 3.93848294084e-05

Current iteration: 10414
Current error: 3.91727115832e-05

Current iteration: 10415
Current error: 3.89992038218e-05

Current iteration: 10416
Current error: 5.71841945133e-05

Current iteration: 10417
Current error: 3.85189542799e-05

Current iteration: 10418
Current error: 3.83207569129e-05

Current iteration: 10419
Current error: 3.81182944325e-05

Current iteration: 10420
Current error: 3.79214622208e-05

Current iteration: 10421
Current error: 3.77312615097e-05

Current iteration: 10422
Current error: 3.75393332047e-05

Current iteration: 10423
Current error: 0.0102852556817

Current iteration: 10424
Current error: 0.0166615484229

Current iteration: 10425
Current error: 3.23709169353e-05

Current iteration: 10426
Current error: 3.203338563e-05

Current iteration: 10427
Current error: 7.38797384916e-05

Current iteration: 10428
Current error: 3.16838927129e-05

Current iteration: 10429
Current error: 3.15111132286e-05

Current iteration: 10430
Current error: 3.1386638377e-05

Current iteration: 10431
Current error: 3.12304408695e-05

Current iteration: 10432
Current error: 3.10762780451e-05

Current iteration: 10433
Current error: 3.09322892303e-05

Current iteration: 10434
Current error: 3.07822866144e-05

Current iteration: 10435
Current error: 3.06354931246e-05

Current iteration: 10436
Current error: 3.04918162348e-05

Current iteration: 10437
Current error: 0.461023398252

Current iteration: 10438
Current error: 5.02497056223e-05

Current iteration: 10439
Current error: 4.99543847178e-05

Current iteration: 10440
Current error: 4.96736401152e-05

Current iteration: 10441
Current error: 4.93646377321e-05

Current iteration: 10442
Current error: 4.90791305325e-05

Current iteration: 10443
Current error: 4.879827817e-05

Current iteration: 10444
Current error: 4.8676321878e-05

Current iteration: 10445
Current error: 4.82221712043e-05

Current iteration: 10446
Current error: 4.79385904786e-05

Current iteration: 10447
Current error: 4.76604096923e-05

Current iteration: 10448
Current error: 4.73830157507e-05

Current iteration: 10449
Current error: 4.71056917999e-05

Current iteration: 10450
Current error: 4.68445188212e-05

Current iteration: 10451
Current error: 4.65719476789e-05

Current iteration: 10452
Current error: 4.63131497093e-05

Current iteration: 10453
Current error: 4.60364322556e-05

Current iteration: 10454
Current error: 4.57798170379e-05

Current iteration: 10455
Current error: 0.380970792877

Current iteration: 10456
Current error: 6.89864445185e-05

Current iteration: 10457
Current error: 6.85689319063e-05

Current iteration: 10458
Current error: 0.138203716478

Current iteration: 10459
Current error: 0.126448580242

Current iteration: 10460
Current error: 9.83687999154e-05

Current iteration: 10461
Current error: 9.75584592674e-05

Current iteration: 10462
Current error: 9.69954591809e-05

Current iteration: 10463
Current error: 9.59988042099e-05

Current iteration: 10464
Current error: 0.098591156387

Current iteration: 10465
Current error: 8.22070179915e-05

Current iteration: 10466
Current error: 0.000138845342816

Current iteration: 10467
Current error: 7.91801534452e-05

Current iteration: 10468
Current error: 0.000176336797956

Current iteration: 10469
Current error: 7.72718512278e-05

Current iteration: 10470
Current error: 7.6704188532e-05

Current iteration: 10471
Current error: 7.61748232805e-05

Current iteration: 10472
Current error: 7.56135633519e-05

Current iteration: 10473
Current error: 7.50357645415e-05

Current iteration: 10474
Current error: 7.4595871124e-05

Current iteration: 10475
Current error: 7.39595570446e-05

Current iteration: 10476
Current error: 9.05474114875e-05

Current iteration: 10477
Current error: 0.00118576203899

Current iteration: 10478
Current error: 7.09838812926e-05

Current iteration: 10479
Current error: 7.04906701682e-05

Current iteration: 10480
Current error: 0.0468056982229

Current iteration: 10481
Current error: 0.161449378725

Current iteration: 10482
Current error: 7.60315746341e-05

Current iteration: 10483
Current error: 7.54800002655e-05

Current iteration: 10484
Current error: 7.49258624783e-05

Current iteration: 10485
Current error: 7.43868716752e-05

Current iteration: 10486
Current error: 0.000105114423225

Current iteration: 10487
Current error: 0.035463783623

Current iteration: 10488
Current error: 8.3122955777e-05

Current iteration: 10489
Current error: 0.0691304254005

Current iteration: 10490
Current error: 5.58533198599e-05

Current iteration: 10491
Current error: 5.54969503036e-05

Current iteration: 10492
Current error: 5.71691515019e-05

Current iteration: 10493
Current error: 5.48114504699e-05

Current iteration: 10494
Current error: 0.000387870534983

Current iteration: 10495
Current error: 5.36386350739e-05

Current iteration: 10496
Current error: 0.0507021070473

Current iteration: 10497
Current error: 4.67257498018e-05

Current iteration: 10498
Current error: 4.64495839466e-05

Current iteration: 10499
Current error: 4.62006313162e-05

Current iteration: 10500
Current error: 4.59331295022e-05

Current iteration: 10501
Current error: 4.56678898904e-05

Current iteration: 10502
Current error: 4.54093276396e-05

Current iteration: 10503
Current error: 4.51520753555e-05

Current iteration: 10504
Current error: 5.9268220333e-05

Current iteration: 10505
Current error: 0.160397324046

Current iteration: 10506
Current error: 5.48522519159e-05

Current iteration: 10507
Current error: 5.45126764305e-05

Current iteration: 10508
Current error: 5.41735495854e-05

Current iteration: 10509
Current error: 5.38422119656e-05

Current iteration: 10510
Current error: 5.35181139299e-05

Current iteration: 10511
Current error: 5.3179429811e-05

Current iteration: 10512
Current error: 5.29169052187e-05

Current iteration: 10513
Current error: 5.25312733446e-05

Current iteration: 10514
Current error: 5.2302509645e-05

Current iteration: 10515
Current error: 5.18929743702e-05

Current iteration: 10516
Current error: 5.15907634442e-05

Current iteration: 10517
Current error: 5.13755534972e-05

Current iteration: 10518
Current error: 5.10213416725e-05

Current iteration: 10519
Current error: 0.000508006428793

Current iteration: 10520
Current error: 4.9814108896e-05

Current iteration: 10521
Current error: 4.95021085548e-05

Current iteration: 10522
Current error: 4.92055769153e-05

Current iteration: 10523
Current error: 9.65109738718e-05

Current iteration: 10524
Current error: 4.85382032061e-05

Current iteration: 10525
Current error: 4.82543832612e-05

Current iteration: 10526
Current error: 4.79793290937e-05

Current iteration: 10527
Current error: 4.76800445483e-05

Current iteration: 10528
Current error: 4.74177081519e-05

Current iteration: 10529
Current error: 4.7133379078e-05

Current iteration: 10530
Current error: 4.68620462624e-05

Current iteration: 10531
Current error: 4.65946048519e-05

Current iteration: 10532
Current error: 4.63281272393e-05

Current iteration: 10533
Current error: 4.60626941596e-05

Current iteration: 10534
Current error: 4.58609523406e-05

Current iteration: 10535
Current error: 4.5539844957e-05

Current iteration: 10536
Current error: 4.57524993498e-05

Current iteration: 10537
Current error: 4.50233637864e-05

Current iteration: 10538
Current error: 4.47741941239e-05

Current iteration: 10539
Current error: 4.55559321905e-05

Current iteration: 10540
Current error: 4.42883328991e-05

Current iteration: 10541
Current error: 4.40363981484e-05

Current iteration: 10542
Current error: 4.37798090445e-05

Current iteration: 10543
Current error: 4.35357757849e-05

Current iteration: 10544
Current error: 4.32940362684e-05

Current iteration: 10545
Current error: 4.39277204064e-05

Current iteration: 10546
Current error: 4.28177316957e-05

Current iteration: 10547
Current error: 0.0432467914153

Current iteration: 10548
Current error: 0.000144858766508

Current iteration: 10549
Current error: 3.72945136309e-05

Current iteration: 10550
Current error: 3.71050376276e-05

Current iteration: 10551
Current error: 3.69131809684e-05

Current iteration: 10552
Current error: 4.30296401758e-05

Current iteration: 10553
Current error: 3.72307571817e-05

Current iteration: 10554
Current error: 0.00438199908116

Current iteration: 10555
Current error: 3.47387218338e-05

Current iteration: 10556
Current error: 3.45344830944e-05

Current iteration: 10557
Current error: 3.4357931244e-05

Current iteration: 10558
Current error: 3.41959879434e-05

Current iteration: 10559
Current error: 0.000455199980502

Current iteration: 10560
Current error: 3.44021103608e-05

Current iteration: 10561
Current error: 3.35897052669e-05

Current iteration: 10562
Current error: 3.3148125286e-05

Current iteration: 10563
Current error: 3.36550958266e-05

Current iteration: 10564
Current error: 3.28234708646e-05

Current iteration: 10565
Current error: 0.00592932893274

Current iteration: 10566
Current error: 3.09992984063e-05

Current iteration: 10567
Current error: 0.037015422124

Current iteration: 10568
Current error: 0.181335916926

Current iteration: 10569
Current error: 3.45022817278e-05

Current iteration: 10570
Current error: 3.44281075624e-05

Current iteration: 10571
Current error: 7.79382659294e-05

Current iteration: 10572
Current error: 3.38978165752e-05

Current iteration: 10573
Current error: 3.44043796583e-05

Current iteration: 10574
Current error: 3.40134704068e-05

Current iteration: 10575
Current error: 3.33997536674e-05

Current iteration: 10576
Current error: 3.32390973111e-05

Current iteration: 10577
Current error: 3.30904539039e-05

Current iteration: 10578
Current error: 0.00427023920825

Current iteration: 10579
Current error: 3.14905929543e-05

Current iteration: 10580
Current error: 0.196102229574

Current iteration: 10581
Current error: 3.97039034807e-05

Current iteration: 10582
Current error: 3.97665284646e-05

Current iteration: 10583
Current error: 0.490620716523

Current iteration: 10584
Current error: 7.05615682147e-05

Current iteration: 10585
Current error: 7.00578053715e-05

Current iteration: 10586
Current error: 6.95777949839e-05

Current iteration: 10587
Current error: 6.91252602476e-05

Current iteration: 10588
Current error: 6.86164298921e-05

Current iteration: 10589
Current error: 0.0660960132673

Current iteration: 10590
Current error: 5.87971931297e-05

Current iteration: 10591
Current error: 5.84549103179e-05

Current iteration: 10592
Current error: 5.93729222315e-05

Current iteration: 10593
Current error: 5.76667544464e-05

Current iteration: 10594
Current error: 5.73046844686e-05

Current iteration: 10595
Current error: 5.69424752896e-05

Current iteration: 10596
Current error: 5.6582024777e-05

Current iteration: 10597
Current error: 5.62355959392e-05

Current iteration: 10598
Current error: 0.0478290039532

Current iteration: 10599
Current error: 4.90986911657e-05

Current iteration: 10600
Current error: 4.88767376565e-05

Current iteration: 10601
Current error: 4.85337311895e-05

Current iteration: 10602
Current error: 5.63066742099e-05

Current iteration: 10603
Current error: 4.79411641008e-05

Current iteration: 10604
Current error: 4.76601711781e-05

Current iteration: 10605
Current error: 0.0255390436894

Current iteration: 10606
Current error: 4.29274701646e-05

Current iteration: 10607
Current error: 4.2645207469e-05

Current iteration: 10608
Current error: 4.24103479696e-05

Current iteration: 10609
Current error: 4.25825174476e-05

Current iteration: 10610
Current error: 4.1957818704e-05

Current iteration: 10611
Current error: 4.17242020782e-05

Current iteration: 10612
Current error: 4.14947544989e-05

Current iteration: 10613
Current error: 0.0254976892708

Current iteration: 10614
Current error: 3.73936324171e-05

Current iteration: 10615
Current error: 3.72127845296e-05

Current iteration: 10616
Current error: 3.70085884914e-05

Current iteration: 10617
Current error: 3.83238063354e-05

Current iteration: 10618
Current error: 3.66330332291e-05

Current iteration: 10619
Current error: 0.216503145197

Current iteration: 10620
Current error: 4.72455386237e-05

Current iteration: 10621
Current error: 4.69738000575e-05

Current iteration: 10622
Current error: 4.67470039113e-05

Current iteration: 10623
Current error: 0.153273893668

Current iteration: 10624
Current error: 5.84773498966e-05

Current iteration: 10625
Current error: 0.183129228392

Current iteration: 10626
Current error: 7.17277971555e-05

Current iteration: 10627
Current error: 7.10628232037e-05

Current iteration: 10628
Current error: 7.06270747792e-05

Current iteration: 10629
Current error: 7.00872502048e-05

Current iteration: 10630
Current error: 6.96901107096e-05

Current iteration: 10631
Current error: 6.90931776369e-05

Current iteration: 10632
Current error: 7.75515403813e-05

Current iteration: 10633
Current error: 9.29576081142e-05

Current iteration: 10634
Current error: 7.10612955324e-05

Current iteration: 10635
Current error: 6.71248137488e-05

Current iteration: 10636
Current error: 6.6634977079e-05

Current iteration: 10637
Current error: 6.61751599941e-05

Current iteration: 10638
Current error: 6.57273407669e-05

Current iteration: 10639
Current error: 6.53000012653e-05

Current iteration: 10640
Current error: 0.00661676649847

Current iteration: 10641
Current error: 0.00016522517467

Current iteration: 10642
Current error: 6.06376881429e-05

Current iteration: 10643
Current error: 6.02577479675e-05

Current iteration: 10644
Current error: 6.1340551306e-05

Current iteration: 10645
Current error: 5.94585641246e-05

Current iteration: 10646
Current error: 5.90863956278e-05

Current iteration: 10647
Current error: 5.87085713217e-05

Current iteration: 10648
Current error: 5.83309797701e-05

Current iteration: 10649
Current error: 0.489291589041

Current iteration: 10650
Current error: 0.106904652748

Current iteration: 10651
Current error: 0.000122893616349

Current iteration: 10652
Current error: 0.000367223821222

Current iteration: 10653
Current error: 0.00011989311071

Current iteration: 10654
Current error: 0.000118854183827

Current iteration: 10655
Current error: 0.000117785670153

Current iteration: 10656
Current error: 0.000116666487385

Current iteration: 10657
Current error: 0.000115906519428

Current iteration: 10658
Current error: 0.000115750905646

Current iteration: 10659
Current error: 0.000113612695074

Current iteration: 10660
Current error: 0.000112618132371

Current iteration: 10661
Current error: 0.000111556362758

Current iteration: 10662
Current error: 0.10233153823

Current iteration: 10663
Current error: 0.000130043178608

Current iteration: 10664
Current error: 0.0876412469083

Current iteration: 10665
Current error: 0.000157836470391

Current iteration: 10666
Current error: 0.00014776134475

Current iteration: 10667
Current error: 0.000145618993882

Current iteration: 10668
Current error: 0.000261489657196

Current iteration: 10669
Current error: 0.000142272458171

Current iteration: 10670
Current error: 0.000140855211642

Current iteration: 10671
Current error: 0.000139471310435

Current iteration: 10672
Current error: 0.000139212538549

Current iteration: 10673
Current error: 0.0911549492845

Current iteration: 10674
Current error: 0.000159099683194

Current iteration: 10675
Current error: 0.000162354176503

Current iteration: 10676
Current error: 0.000157018057248

Current iteration: 10677
Current error: 0.000154227704815

Current iteration: 10678
Current error: 0.000152545650262

Current iteration: 10679
Current error: 0.000150986272666

Current iteration: 10680
Current error: 0.000149453203761

Current iteration: 10681
Current error: 0.000148839495648

Current iteration: 10682
Current error: 0.000146437894295

Current iteration: 10683
Current error: 0.000144951072315

Current iteration: 10684
Current error: 0.000143515773742

Current iteration: 10685
Current error: 0.000142079410198

Current iteration: 10686
Current error: 0.000140733387231

Current iteration: 10687
Current error: 0.000139306064298

Current iteration: 10688
Current error: 0.000137946146352

Current iteration: 10689
Current error: 0.000136907020406

Current iteration: 10690
Current error: 0.000135270216188

Current iteration: 10691
Current error: 0.000136080442766

Current iteration: 10692
Current error: 0.000132742279823

Current iteration: 10693
Current error: 0.00013146342744

Current iteration: 10694
Current error: 0.000188741921737

Current iteration: 10695
Current error: 0.0814331701754

Current iteration: 10696
Current error: 0.000109060849105

Current iteration: 10697
Current error: 0.000110690566248

Current iteration: 10698
Current error: 0.000108599900091

Current iteration: 10699
Current error: 0.000106243922352

Current iteration: 10700
Current error: 0.000105324124665

Current iteration: 10701
Current error: 0.000104505001316

Current iteration: 10702
Current error: 0.000103548282597

Current iteration: 10703
Current error: 0.000102694153054

Current iteration: 10704
Current error: 0.0986776084388

Current iteration: 10705
Current error: 0.000119269840578

Current iteration: 10706
Current error: 0.000118190359299

Current iteration: 10707
Current error: 0.000117120267924

Current iteration: 10708
Current error: 0.000128030808842

Current iteration: 10709
Current error: 0.0933743278779

Current iteration: 10710
Current error: 0.000134228169951

Current iteration: 10711
Current error: 0.000132926886184

Current iteration: 10712
Current error: 0.000131667496188

Current iteration: 10713
Current error: 0.00013668326871

Current iteration: 10714
Current error: 0.0441400749848

Current iteration: 10715
Current error: 0.000113190740628

Current iteration: 10716
Current error: 0.000112312652564

Current iteration: 10717
Current error: 0.000111673266459

Current iteration: 10718
Current error: 0.000111402020638

Current iteration: 10719
Current error: 0.000110534890869

Current iteration: 10720
Current error: 0.000108302790176

Current iteration: 10721
Current error: 0.000107399819834

Current iteration: 10722
Current error: 0.00010644112222

Current iteration: 10723
Current error: 0.0903840201538

Current iteration: 10724
Current error: 0.0852697532531

Current iteration: 10725
Current error: 0.000292163472421

Current iteration: 10726
Current error: 0.000139876106238

Current iteration: 10727
Current error: 0.000138473049203

Current iteration: 10728
Current error: 0.000137960686055

Current iteration: 10729
Current error: 0.00013590461027

Current iteration: 10730
Current error: 0.000145014099807

Current iteration: 10731
Current error: 0.355436678021

Current iteration: 10732
Current error: 0.000200577663208

Current iteration: 10733
Current error: 0.0650436661787

Current iteration: 10734
Current error: 0.135404901836

Current iteration: 10735
Current error: 0.000185375109394

Current iteration: 10736
Current error: 0.000181306704897

Current iteration: 10737
Current error: 0.000240449293984

Current iteration: 10738
Current error: 0.000178678251447

Current iteration: 10739
Current error: 0.000175210772747

Current iteration: 10740
Current error: 0.000173083506392

Current iteration: 10741
Current error: 0.422574048353

Current iteration: 10742
Current error: 0.00028242821497

Current iteration: 10743
Current error: 0.203207795023

Current iteration: 10744
Current error: 0.00389500818982

Current iteration: 10745
Current error: 0.000211715597193

Current iteration: 10746
Current error: 0.000205429617204

Current iteration: 10747
Current error: 0.000243598885943

Current iteration: 10748
Current error: 0.000200375088972

Current iteration: 10749
Current error: 0.00020322519999

Current iteration: 10750
Current error: 0.000195690183261

Current iteration: 10751
Current error: 0.00038575630826

Current iteration: 10752
Current error: 0.106352707838

Current iteration: 10753
Current error: 0.000158124169975

Current iteration: 10754
Current error: 0.0758164695468

Current iteration: 10755
Current error: 0.000179304529895

Current iteration: 10756
Current error: 0.000177334688533

Current iteration: 10757
Current error: 0.000175683165175

Current iteration: 10758
Current error: 0.170584316155

Current iteration: 10759
Current error: 0.00013995302934

Current iteration: 10760
Current error: 0.000138624868813

Current iteration: 10761
Current error: 0.000137220124433

Current iteration: 10762
Current error: 0.000135966280274

Current iteration: 10763
Current error: 0.0938545173137

Current iteration: 10764
Current error: 0.000163289335869

Current iteration: 10765
Current error: 0.000155957158468

Current iteration: 10766
Current error: 0.0963893401532

Current iteration: 10767
Current error: 0.000181671746713

Current iteration: 10768
Current error: 0.000181643499194

Current iteration: 10769
Current error: 0.000177662571878

Current iteration: 10770
Current error: 0.00017568793543

Current iteration: 10771
Current error: 0.000174185773228

Current iteration: 10772
Current error: 0.000173005493129

Current iteration: 10773
Current error: 0.000171350701809

Current iteration: 10774
Current error: 0.000191144780333

Current iteration: 10775
Current error: 0.000166228197398

Current iteration: 10776
Current error: 0.0746689359421

Current iteration: 10777
Current error: 0.000188839459516

Current iteration: 10778
Current error: 0.000206339453524

Current iteration: 10779
Current error: 0.000183468899915

Current iteration: 10780
Current error: 0.00018136934833

Current iteration: 10781
Current error: 0.000179527298025

Current iteration: 10782
Current error: 0.000177409974371

Current iteration: 10783
Current error: 0.000175448540403

Current iteration: 10784
Current error: 0.089312771098

Current iteration: 10785
Current error: 0.000781767478599

Current iteration: 10786
Current error: 0.000142667743151

Current iteration: 10787
Current error: 0.000141213835065

Current iteration: 10788
Current error: 0.000139907117034

Current iteration: 10789
Current error: 0.000206463958926

Current iteration: 10790
Current error: 0.000138596032649

Current iteration: 10791
Current error: 0.000135591268946

Current iteration: 10792
Current error: 0.000134172613574

Current iteration: 10793
Current error: 0.000132878407603

Current iteration: 10794
Current error: 0.000131608012812

Current iteration: 10795
Current error: 0.00013036261386

Current iteration: 10796
Current error: 0.000129118259058

Current iteration: 10797
Current error: 0.000128412647291

Current iteration: 10798
Current error: 0.000127543748286

Current iteration: 10799
Current error: 0.000125506418469

Current iteration: 10800
Current error: 0.000124422309971

Current iteration: 10801
Current error: 0.000123186715076

Current iteration: 10802
Current error: 0.0868911443624

Current iteration: 10803
Current error: 0.000130583738787

Current iteration: 10804
Current error: 0.000105330301212

Current iteration: 10805
Current error: 0.0886236309882

Current iteration: 10806
Current error: 0.000117315575109

Current iteration: 10807
Current error: 0.000116286084337

Current iteration: 10808
Current error: 0.00011524483474

Current iteration: 10809
Current error: 0.000114217429265

Current iteration: 10810
Current error: 0.00235154795629

Current iteration: 10811
Current error: 0.000210217760902

Current iteration: 10812
Current error: 0.000107897212845

Current iteration: 10813
Current error: 0.000106950949632

Current iteration: 10814
Current error: 0.000106033633147

Current iteration: 10815
Current error: 0.000105347974473

Current iteration: 10816
Current error: 0.00180217463014

Current iteration: 10817
Current error: 0.000100951103625

Current iteration: 10818
Current error: 0.000366905813722

Current iteration: 10819
Current error: 9.85883777989e-05

Current iteration: 10820
Current error: 9.82158068293e-05

Current iteration: 10821
Current error: 0.000100324175313

Current iteration: 10822
Current error: 0.0799278633294

Current iteration: 10823
Current error: 8.26881763185e-05

Current iteration: 10824
Current error: 8.10189720332e-05

Current iteration: 10825
Current error: 8.03988020682e-05

Current iteration: 10826
Current error: 8.01255311246e-05

Current iteration: 10827
Current error: 7.91887578051e-05

Current iteration: 10828
Current error: 7.86106505844e-05

Current iteration: 10829
Current error: 7.87987192386e-05

Current iteration: 10830
Current error: 7.74539825679e-05

Current iteration: 10831
Current error: 7.68778948757e-05

Current iteration: 10832
Current error: 7.63183476858e-05

Current iteration: 10833
Current error: 7.5750291244e-05

Current iteration: 10834
Current error: 0.00014879298101

Current iteration: 10835
Current error: 7.4459677624e-05

Current iteration: 10836
Current error: 7.39408005707e-05

Current iteration: 10837
Current error: 7.3394621373e-05

Current iteration: 10838
Current error: 0.0234917908178

Current iteration: 10839
Current error: 0.103364391364

Current iteration: 10840
Current error: 0.131783894821

Current iteration: 10841
Current error: 0.000351857431628

Current iteration: 10842
Current error: 6.44003587792e-05

Current iteration: 10843
Current error: 6.22615876785e-05

Current iteration: 10844
Current error: 6.18568143327e-05

Current iteration: 10845
Current error: 6.14531761955e-05

Current iteration: 10846
Current error: 0.000359246562411

Current iteration: 10847
Current error: 6.01382007032e-05

Current iteration: 10848
Current error: 5.97545250679e-05

Current iteration: 10849
Current error: 5.93650612575e-05

Current iteration: 10850
Current error: 5.89839955237e-05

Current iteration: 10851
Current error: 0.00133464831023

Current iteration: 10852
Current error: 0.000192275292819

Current iteration: 10853
Current error: 5.64071509508e-05

Current iteration: 10854
Current error: 5.60407907149e-05

Current iteration: 10855
Current error: 8.4134244085e-05

Current iteration: 10856
Current error: 5.52659761931e-05

Current iteration: 10857
Current error: 7.57946822304e-05

Current iteration: 10858
Current error: 6.26086139146e-05

Current iteration: 10859
Current error: 5.41664086148e-05

Current iteration: 10860
Current error: 5.38348102281e-05

Current iteration: 10861
Current error: 5.35257991672e-05

Current iteration: 10862
Current error: 5.31764244629e-05

Current iteration: 10863
Current error: 5.5985094894e-05

Current iteration: 10864
Current error: 5.2521252419e-05

Current iteration: 10865
Current error: 5.98347593461e-05

Current iteration: 10866
Current error: 5.1864931779e-05

Current iteration: 10867
Current error: 5.15551155539e-05

Current iteration: 10868
Current error: 5.124504499e-05

Current iteration: 10869
Current error: 5.093395052e-05

Current iteration: 10870
Current error: 5.06328576732e-05

Current iteration: 10871
Current error: 6.60100045389e-05

Current iteration: 10872
Current error: 5.02527398348e-05

Current iteration: 10873
Current error: 4.96948870883e-05

Current iteration: 10874
Current error: 4.93984802811e-05

Current iteration: 10875
Current error: 4.91247456852e-05

Current iteration: 10876
Current error: 4.88236343847e-05

Current iteration: 10877
Current error: 4.85707504205e-05

Current iteration: 10878
Current error: 4.83268935902e-05

Current iteration: 10879
Current error: 4.80592928673e-05

Current iteration: 10880
Current error: 4.76917273612e-05

Current iteration: 10881
Current error: 4.74082642118e-05

Current iteration: 10882
Current error: 4.71379681077e-05

Current iteration: 10883
Current error: 4.69275192245e-05

Current iteration: 10884
Current error: 4.66028010501e-05

Current iteration: 10885
Current error: 4.63361562949e-05

Current iteration: 10886
Current error: 4.60719850855e-05

Current iteration: 10887
Current error: 4.58124063046e-05

Current iteration: 10888
Current error: 4.55513566194e-05

Current iteration: 10889
Current error: 4.52978025025e-05

Current iteration: 10890
Current error: 4.50360911308e-05

Current iteration: 10891
Current error: 4.4860897784e-05

Current iteration: 10892
Current error: 4.45520205785e-05

Current iteration: 10893
Current error: 4.4284214171e-05

Current iteration: 10894
Current error: 0.168170332238

Current iteration: 10895
Current error: 0.0996599019497

Current iteration: 10896
Current error: 4.76306249789e-05

Current iteration: 10897
Current error: 4.61911507732e-05

Current iteration: 10898
Current error: 4.59816618924e-05

Current iteration: 10899
Current error: 4.56690355589e-05

Current iteration: 10900
Current error: 4.54050090503e-05

Current iteration: 10901
Current error: 4.51442766505e-05

Current iteration: 10902
Current error: 4.49672177345e-05

Current iteration: 10903
Current error: 4.46487057654e-05

Current iteration: 10904
Current error: 4.43969815799e-05

Current iteration: 10905
Current error: 4.41492627956e-05

Current iteration: 10906
Current error: 4.39039507175e-05

Current iteration: 10907
Current error: 0.00304149151373

Current iteration: 10908
Current error: 4.19808519539e-05

Current iteration: 10909
Current error: 4.175716877e-05

Current iteration: 10910
Current error: 4.15474041715e-05

Current iteration: 10911
Current error: 4.13349025958e-05

Current iteration: 10912
Current error: 4.12939005794e-05

Current iteration: 10913
Current error: 4.08580045608e-05

Current iteration: 10914
Current error: 4.06342412844e-05

Current iteration: 10915
Current error: 4.04199915152e-05

Current iteration: 10916
Current error: 4.1890918611e-05

Current iteration: 10917
Current error: 3.99876204648e-05

Current iteration: 10918
Current error: 3.9795940818e-05

Current iteration: 10919
Current error: 3.956176356e-05

Current iteration: 10920
Current error: 6.58949666122e-05

Current iteration: 10921
Current error: 3.91028359487e-05

Current iteration: 10922
Current error: 0.123211475946

Current iteration: 10923
Current error: 0.000410239089299

Current iteration: 10924
Current error: 4.56487870538e-05

Current iteration: 10925
Current error: 4.54040789402e-05

Current iteration: 10926
Current error: 4.51370141878e-05

Current iteration: 10927
Current error: 4.48921716881e-05

Current iteration: 10928
Current error: 4.46306004716e-05

Current iteration: 10929
Current error: 4.43974342051e-05

Current iteration: 10930
Current error: 4.82104412752e-05

Current iteration: 10931
Current error: 4.86001302141e-05

Current iteration: 10932
Current error: 0.000173081329571

Current iteration: 10933
Current error: 0.000201639160467

Current iteration: 10934
Current error: 4.26722505443e-05

Current iteration: 10935
Current error: 4.24488857297e-05

Current iteration: 10936
Current error: 4.22128633561e-05

Current iteration: 10937
Current error: 0.137725250439

Current iteration: 10938
Current error: 5.10703708407e-05

Current iteration: 10939
Current error: 5.90951490994e-05

Current iteration: 10940
Current error: 0.000100224451963

Current iteration: 10941
Current error: 5.03036765698e-05

Current iteration: 10942
Current error: 4.97334046883e-05

Current iteration: 10943
Current error: 4.9570929702e-05

Current iteration: 10944
Current error: 4.9211450097e-05

Current iteration: 10945
Current error: 5.05265913352e-05

Current iteration: 10946
Current error: 4.85693020195e-05

Current iteration: 10947
Current error: 4.82859954604e-05

Current iteration: 10948
Current error: 4.80022600467e-05

Current iteration: 10949
Current error: 4.77273584274e-05

Current iteration: 10950
Current error: 4.74475361517e-05

Current iteration: 10951
Current error: 4.74331229267e-05

Current iteration: 10952
Current error: 4.6902042e-05

Current iteration: 10953
Current error: 0.0190022928823

Current iteration: 10954
Current error: 4.26863802357e-05

Current iteration: 10955
Current error: 4.25889894158e-05

Current iteration: 10956
Current error: 4.25920360275e-05

Current iteration: 10957
Current error: 4.1925969402e-05

Current iteration: 10958
Current error: 7.21095247399e-05

Current iteration: 10959
Current error: 0.118351742503

Current iteration: 10960
Current error: 4.94337020687e-05

Current iteration: 10961
Current error: 4.91423165442e-05

Current iteration: 10962
Current error: 4.88697485567e-05

Current iteration: 10963
Current error: 4.85666845354e-05

Current iteration: 10964
Current error: 4.82840027406e-05

Current iteration: 10965
Current error: 4.80035611832e-05

Current iteration: 10966
Current error: 4.9958101149e-05

Current iteration: 10967
Current error: 4.74583979969e-05

Current iteration: 10968
Current error: 4.71679445521e-05

Current iteration: 10969
Current error: 4.69839074926e-05

Current iteration: 10970
Current error: 0.000191653435966

Current iteration: 10971
Current error: 4.62640611525e-05

Current iteration: 10972
Current error: 4.58582086879e-05

Current iteration: 10973
Current error: 4.85453029911e-05

Current iteration: 10974
Current error: 4.53228856914e-05

Current iteration: 10975
Current error: 4.54349002699e-05

Current iteration: 10976
Current error: 0.049958142831

Current iteration: 10977
Current error: 0.0654075916015

Current iteration: 10978
Current error: 3.39614503649e-05

Current iteration: 10979
Current error: 3.36483235251e-05

Current iteration: 10980
Current error: 3.34894116041e-05

Current iteration: 10981
Current error: 3.33502748031e-05

Current iteration: 10982
Current error: 0.132862592053

Current iteration: 10983
Current error: 4.08141024099e-05

Current iteration: 10984
Current error: 3.96771558547e-05

Current iteration: 10985
Current error: 0.000189284234026

Current iteration: 10986
Current error: 0.000192485453635

Current iteration: 10987
Current error: 4.83550240871e-05

Current iteration: 10988
Current error: 0.124612332139

Current iteration: 10989
Current error: 4.7728864044e-05

Current iteration: 10990
Current error: 4.56258734985e-05

Current iteration: 10991
Current error: 0.0422904560032

Current iteration: 10992
Current error: 4.00221582426e-05

Current iteration: 10993
Current error: 3.98082838573e-05

Current iteration: 10994
Current error: 3.95966257873e-05

Current iteration: 10995
Current error: 3.93876484819e-05

Current iteration: 10996
Current error: 3.91785593021e-05

Current iteration: 10997
Current error: 3.89741919995e-05

Current iteration: 10998
Current error: 0.0914838026667

Current iteration: 10999
Current error: 3.28591123141e-05

Current iteration: 11000
Current error: 0.0732719778383

Current iteration: 11001
Current error: 0.173644189518

Current iteration: 11002
Current error: 3.52791135916e-05

Current iteration: 11003
Current error: 0.0001987578182

Current iteration: 11004
Current error: 3.47147548956e-05

Current iteration: 11005
Current error: 0.00104626218072

Current iteration: 11006
Current error: 3.37201558274e-05

Current iteration: 11007
Current error: 3.35549718321e-05

Current iteration: 11008
Current error: 3.33945741819e-05

Current iteration: 11009
Current error: 4.04103364931e-05

Current iteration: 11010
Current error: 3.30533574109e-05

Current iteration: 11011
Current error: 3.29001942755e-05

Current iteration: 11012
Current error: 7.48854008799e-05

Current iteration: 11013
Current error: 3.2509818946e-05

Current iteration: 11014
Current error: 3.2348686146e-05

Current iteration: 11015
Current error: 3.5327088778e-05

Current iteration: 11016
Current error: 3.20371697582e-05

Current iteration: 11017
Current error: 3.19644595905e-05

Current iteration: 11018
Current error: 3.17434819909e-05

Current iteration: 11019
Current error: 3.15808489447e-05

Current iteration: 11020
Current error: 0.142186087106

Current iteration: 11021
Current error: 3.83682962263e-05

Current iteration: 11022
Current error: 3.81709389356e-05

Current iteration: 11023
Current error: 3.79858393045e-05

Current iteration: 11024
Current error: 0.11865656498

Current iteration: 11025
Current error: 4.50497521525e-05

Current iteration: 11026
Current error: 4.48459902484e-05

Current iteration: 11027
Current error: 0.000248887961009

Current iteration: 11028
Current error: 4.38973770118e-05

Current iteration: 11029
Current error: 4.36545561351e-05

Current iteration: 11030
Current error: 4.34154180841e-05

Current iteration: 11031
Current error: 4.31743733118e-05

Current iteration: 11032
Current error: 4.29386317471e-05

Current iteration: 11033
Current error: 4.27007735578e-05

Current iteration: 11034
Current error: 4.24746455799e-05

Current iteration: 11035
Current error: 4.22346719335e-05

Current iteration: 11036
Current error: 4.20832199236e-05

Current iteration: 11037
Current error: 4.19190897273e-05

Current iteration: 11038
Current error: 4.15496897429e-05

Current iteration: 11039
Current error: 4.13371488498e-05

Current iteration: 11040
Current error: 0.0194904646739

Current iteration: 11041
Current error: 3.7531436321e-05

Current iteration: 11042
Current error: 3.73389837405e-05

Current iteration: 11043
Current error: 3.71412960579e-05

Current iteration: 11044
Current error: 3.70759526782e-05

Current iteration: 11045
Current error: 3.67873362887e-05

Current iteration: 11046
Current error: 3.66439781455e-05

Current iteration: 11047
Current error: 0.0514450486832

Current iteration: 11048
Current error: 3.20848459327e-05

Current iteration: 11049
Current error: 3.16498844002e-05

Current iteration: 11050
Current error: 3.15063625849e-05

Current iteration: 11051
Current error: 0.12187794507

Current iteration: 11052
Current error: 3.73491690612e-05

Current iteration: 11053
Current error: 3.71595057699e-05

Current iteration: 11054
Current error: 3.69667569854e-05

Current iteration: 11055
Current error: 3.67923121313e-05

Current iteration: 11056
Current error: 5.39330815937e-05

Current iteration: 11057
Current error: 3.63926093821e-05

Current iteration: 11058
Current error: 3.6184187285e-05

Current iteration: 11059
Current error: 3.61729790448e-05

Current iteration: 11060
Current error: 5.32552301312e-05

Current iteration: 11061
Current error: 3.56419270494e-05

Current iteration: 11062
Current error: 3.54249082501e-05

Current iteration: 11063
Current error: 3.53183470131e-05

Current iteration: 11064
Current error: 3.50721714972e-05

Current iteration: 11065
Current error: 0.107251176193

Current iteration: 11066
Current error: 4.10255885731e-05

Current iteration: 11067
Current error: 0.120062976627

Current iteration: 11068
Current error: 3.3880296736e-05

Current iteration: 11069
Current error: 3.37143996164e-05

Current iteration: 11070
Current error: 3.35895493448e-05

Current iteration: 11071
Current error: 3.33873336067e-05

Current iteration: 11072
Current error: 3.32339999994e-05

Current iteration: 11073
Current error: 0.0653293406282

Current iteration: 11074
Current error: 0.000714860618368

Current iteration: 11075
Current error: 2.79463240192e-05

Current iteration: 11076
Current error: 2.78412584133e-05

Current iteration: 11077
Current error: 3.56585615539e-05

Current iteration: 11078
Current error: 4.32033593295e-05

Current iteration: 11079
Current error: 2.74136422163e-05

Current iteration: 11080
Current error: 0.129287440047

Current iteration: 11081
Current error: 3.2843426232e-05

Current iteration: 11082
Current error: 3.269000463e-05

Current iteration: 11083
Current error: 0.0465645145097

Current iteration: 11084
Current error: 0.001824388688

Current iteration: 11085
Current error: 2.78159715424e-05

Current iteration: 11086
Current error: 0.000101852494324

Current iteration: 11087
Current error: 2.73500096092e-05

Current iteration: 11088
Current error: 0.492645638078

Current iteration: 11089
Current error: 6.69768216313e-05

Current iteration: 11090
Current error: 4.9052090515e-05

Current iteration: 11091
Current error: 5.14586452166e-05

Current iteration: 11092
Current error: 4.82295874024e-05

Current iteration: 11093
Current error: 4.80957209005e-05

Current iteration: 11094
Current error: 0.0894841517881

Current iteration: 11095
Current error: 4.02923779473e-05

Current iteration: 11096
Current error: 4.01019472993e-05

Current iteration: 11097
Current error: 0.370499074003

Current iteration: 11098
Current error: 6.01471954436e-05

Current iteration: 11099
Current error: 5.97525930773e-05

Current iteration: 11100
Current error: 0.0938434833093

Current iteration: 11101
Current error: 6.96628398482e-05

Current iteration: 11102
Current error: 0.000112398580189

Current iteration: 11103
Current error: 0.126937079945

Current iteration: 11104
Current error: 5.62198796153e-05

Current iteration: 11105
Current error: 5.77028508102e-05

Current iteration: 11106
Current error: 0.0192383482641

Current iteration: 11107
Current error: 5.06852577913e-05

Current iteration: 11108
Current error: 5.13415206375e-05

Current iteration: 11109
Current error: 5.00693757569e-05

Current iteration: 11110
Current error: 4.97757951109e-05

Current iteration: 11111
Current error: 4.95413337864e-05

Current iteration: 11112
Current error: 4.92004949284e-05

Current iteration: 11113
Current error: 4.89401100062e-05

Current iteration: 11114
Current error: 0.140338945563

Current iteration: 11115
Current error: 5.93903289967e-05

Current iteration: 11116
Current error: 6.31006136708e-05

Current iteration: 11117
Current error: 5.86144016036e-05

Current iteration: 11118
Current error: 0.129423390927

Current iteration: 11119
Current error: 4.80773817956e-05

Current iteration: 11120
Current error: 0.111998514883

Current iteration: 11121
Current error: 5.68781908203e-05

Current iteration: 11122
Current error: 5.64133163361e-05

Current iteration: 11123
Current error: 5.64947523961e-05

Current iteration: 11124
Current error: 5.57071008394e-05

Current iteration: 11125
Current error: 5.56477882775e-05

Current iteration: 11126
Current error: 6.12804784884e-05

Current iteration: 11127
Current error: 5.46535372863e-05

Current iteration: 11128
Current error: 5.43113155645e-05

Current iteration: 11129
Current error: 0.0940030045811

Current iteration: 11130
Current error: 6.29985723618e-05

Current iteration: 11131
Current error: 6.25706838512e-05

Current iteration: 11132
Current error: 9.47443014192e-05

Current iteration: 11133
Current error: 6.16621740198e-05

Current iteration: 11134
Current error: 6.13188639151e-05

Current iteration: 11135
Current error: 6.08666203568e-05

Current iteration: 11136
Current error: 6.0451718612e-05

Current iteration: 11137
Current error: 6.00699121021e-05

Current iteration: 11138
Current error: 5.97730167595e-05

Current iteration: 11139
Current error: 5.92909239379e-05

Current iteration: 11140
Current error: 5.89118709563e-05

Current iteration: 11141
Current error: 5.85286596362e-05

Current iteration: 11142
Current error: 5.81565795325e-05

Current iteration: 11143
Current error: 5.80928225445e-05

Current iteration: 11144
Current error: 6.07998624019e-05

Current iteration: 11145
Current error: 0.000470316132394

Current iteration: 11146
Current error: 5.62021255467e-05

Current iteration: 11147
Current error: 5.5748476429e-05

Current iteration: 11148
Current error: 5.5380937565e-05

Current iteration: 11149
Current error: 5.50383897436e-05

Current iteration: 11150
Current error: 5.48311871338e-05

Current iteration: 11151
Current error: 5.44429969033e-05

Current iteration: 11152
Current error: 0.107468833661

Current iteration: 11153
Current error: 4.52308967785e-05

Current iteration: 11154
Current error: 4.55204910948e-05

Current iteration: 11155
Current error: 0.379805143129

Current iteration: 11156
Current error: 6.79965722479e-05

Current iteration: 11157
Current error: 6.82305438171e-05

Current iteration: 11158
Current error: 0.000164716799806

Current iteration: 11159
Current error: 6.63586578005e-05

Current iteration: 11160
Current error: 0.00446437371827

Current iteration: 11161
Current error: 6.30732709719e-05

Current iteration: 11162
Current error: 6.23995678004e-05

Current iteration: 11163
Current error: 6.19936049503e-05

Current iteration: 11164
Current error: 6.15836026401e-05

Current iteration: 11165
Current error: 6.22249611622e-05

Current iteration: 11166
Current error: 6.07855697305e-05

Current iteration: 11167
Current error: 0.398300473963

Current iteration: 11168
Current error: 9.47173009254e-05

Current iteration: 11169
Current error: 9.4084841293e-05

Current iteration: 11170
Current error: 0.376767459451

Current iteration: 11171
Current error: 0.000333082246563

Current iteration: 11172
Current error: 0.483376799281

Current iteration: 11173
Current error: 0.0002505461395

Current iteration: 11174
Current error: 0.000247128495955

Current iteration: 11175
Current error: 0.000243767250085

Current iteration: 11176
Current error: 0.000241489677926

Current iteration: 11177
Current error: 0.000237703532066

Current iteration: 11178
Current error: 0.00220091141087

Current iteration: 11179
Current error: 0.000226276457721

Current iteration: 11180
Current error: 0.00022636826699

Current iteration: 11181
Current error: 0.000220686680044

Current iteration: 11182
Current error: 0.000218040716242

Current iteration: 11183
Current error: 0.000215325909849

Current iteration: 11184
Current error: 0.000212765024848

Current iteration: 11185
Current error: 0.000210450297173

Current iteration: 11186
Current error: 0.000208735708749

Current iteration: 11187
Current error: 0.000205154405248

Current iteration: 11188
Current error: 0.000202720985842

Current iteration: 11189
Current error: 0.000200346096818

Current iteration: 11190
Current error: 0.000198108019779

Current iteration: 11191
Current error: 0.000195674578975

Current iteration: 11192
Current error: 0.000198995347284

Current iteration: 11193
Current error: 0.000191532818689

Current iteration: 11194
Current error: 0.000189336866519

Current iteration: 11195
Current error: 0.000186845810957

Current iteration: 11196
Current error: 0.000184728039586

Current iteration: 11197
Current error: 0.000182758448768

Current iteration: 11198
Current error: 0.000182698801968

Current iteration: 11199
Current error: 0.000178589826725

Current iteration: 11200
Current error: 0.000177320167391

Current iteration: 11201
Current error: 0.000174669220937

Current iteration: 11202
Current error: 0.00037498806432

Current iteration: 11203
Current error: 0.000185252481661

Current iteration: 11204
Current error: 0.0538556940471

Current iteration: 11205
Current error: 0.00018797824867

Current iteration: 11206
Current error: 0.000185875619588

Current iteration: 11207
Current error: 0.000183928525709

Current iteration: 11208
Current error: 0.000181717740619

Current iteration: 11209
Current error: 0.000547860089521

Current iteration: 11210
Current error: 0.0001763386769

Current iteration: 11211
Current error: 0.000174835495388

Current iteration: 11212
Current error: 0.000172507587669

Current iteration: 11213
Current error: 0.000171944905816

Current iteration: 11214
Current error: 0.120193009296

Current iteration: 11215
Current error: 0.000138602226736

Current iteration: 11216
Current error: 0.000137225946026

Current iteration: 11217
Current error: 0.000135888396504

Current iteration: 11218
Current error: 0.336057113046

Current iteration: 11219
Current error: 0.00020035830936

Current iteration: 11220
Current error: 0.000199752623974

Current iteration: 11221
Current error: 0.150956793965

Current iteration: 11222
Current error: 0.00015823579081

Current iteration: 11223
Current error: 0.000689770048951

Current iteration: 11224
Current error: 0.000153345387053

Current iteration: 11225
Current error: 0.000154351138284

Current iteration: 11226
Current error: 0.000150229370758

Current iteration: 11227
Current error: 0.000148690106107

Current iteration: 11228
Current error: 0.000147240776371

Current iteration: 11229
Current error: 0.000147724305421

Current iteration: 11230
Current error: 0.00019714083553

Current iteration: 11231
Current error: 0.000142576045927

Current iteration: 11232
Current error: 0.153183303935

Current iteration: 11233
Current error: 0.000114439226023

Current iteration: 11234
Current error: 0.000114017776413

Current iteration: 11235
Current error: 0.000112285550863

Current iteration: 11236
Current error: 0.000119059324198

Current iteration: 11237
Current error: 0.000110291299162

Current iteration: 11238
Current error: 0.000109337423185

Current iteration: 11239
Current error: 0.098932761678

Current iteration: 11240
Current error: 9.03818788802e-05

Current iteration: 11241
Current error: 8.96850764318e-05

Current iteration: 11242
Current error: 0.147940727563

Current iteration: 11243
Current error: 7.24826429902e-05

Current iteration: 11244
Current error: 7.19714357711e-05

Current iteration: 11245
Current error: 7.14586478154e-05

Current iteration: 11246
Current error: 7.09587133814e-05

Current iteration: 11247
Current error: 7.17262198381e-05

Current iteration: 11248
Current error: 7.00349514917e-05

Current iteration: 11249
Current error: 6.9465836758e-05

Current iteration: 11250
Current error: 6.90210950305e-05

Current iteration: 11251
Current error: 0.0895548783571

Current iteration: 11252
Current error: 5.77726071687e-05

Current iteration: 11253
Current error: 5.74267634862e-05

Current iteration: 11254
Current error: 5.70315384831e-05

Current iteration: 11255
Current error: 5.66978879354e-05

Current iteration: 11256
Current error: 5.63178887979e-05

Current iteration: 11257
Current error: 5.59802929907e-05

Current iteration: 11258
Current error: 5.56082823737e-05

Current iteration: 11259
Current error: 0.0909584714839

Current iteration: 11260
Current error: 4.66130523684e-05

Current iteration: 11261
Current error: 0.0560754612849

Current iteration: 11262
Current error: 4.02697164106e-05

Current iteration: 11263
Current error: 0.000600990180757

Current iteration: 11264
Current error: 3.93156494018e-05

Current iteration: 11265
Current error: 3.90869937441e-05

Current iteration: 11266
Current error: 3.88829107461e-05

Current iteration: 11267
Current error: 3.8696278059e-05

Current iteration: 11268
Current error: 0.00375284213445

Current iteration: 11269
Current error: 3.68554975677e-05

Current iteration: 11270
Current error: 3.66575915455e-05

Current iteration: 11271
Current error: 3.64707867102e-05

Current iteration: 11272
Current error: 3.96166908606e-05

Current iteration: 11273
Current error: 3.61116467345e-05

Current iteration: 11274
Current error: 3.59102202874e-05

Current iteration: 11275
Current error: 3.57288370919e-05

Current iteration: 11276
Current error: 3.68061046472e-05

Current iteration: 11277
Current error: 3.53676990546e-05

Current iteration: 11278
Current error: 3.51980521038e-05

Current iteration: 11279
Current error: 3.50193077727e-05

Current iteration: 11280
Current error: 3.48450085136e-05

Current iteration: 11281
Current error: 3.4671724391e-05

Current iteration: 11282
Current error: 3.45672325364e-05

Current iteration: 11283
Current error: 3.43738485387e-05

Current iteration: 11284
Current error: 3.4160351278e-05

Current iteration: 11285
Current error: 3.41131667344e-05

Current iteration: 11286
Current error: 0.12642415813

Current iteration: 11287
Current error: 4.06724892927e-05

Current iteration: 11288
Current error: 4.04921341522e-05

Current iteration: 11289
Current error: 0.130134688077

Current iteration: 11290
Current error: 0.000249691696415

Current iteration: 11291
Current error: 4.80601310995e-05

Current iteration: 11292
Current error: 4.77833075149e-05

Current iteration: 11293
Current error: 4.75206489041e-05

Current iteration: 11294
Current error: 4.72270334672e-05

Current iteration: 11295
Current error: 4.69662515412e-05

Current iteration: 11296
Current error: 4.66928108681e-05

Current iteration: 11297
Current error: 4.64296936734e-05

Current iteration: 11298
Current error: 0.0955089934543

Current iteration: 11299
Current error: 3.88354454939e-05

Current iteration: 11300
Current error: 3.99657675358e-05

Current iteration: 11301
Current error: 4.69676390421e-05

Current iteration: 11302
Current error: 3.8209723517e-05

Current iteration: 11303
Current error: 3.81245220463e-05

Current iteration: 11304
Current error: 3.78151214528e-05

Current iteration: 11305
Current error: 3.76165161116e-05

Current iteration: 11306
Current error: 3.74252549006e-05

Current iteration: 11307
Current error: 0.00128572504594

Current iteration: 11308
Current error: 3.62548637043e-05

Current iteration: 11309
Current error: 3.60735568978e-05

Current iteration: 11310
Current error: 0.00111459380836

Current iteration: 11311
Current error: 3.50139990965e-05

Current iteration: 11312
Current error: 3.4839460901e-05

Current iteration: 11313
Current error: 0.331733615463

Current iteration: 11314
Current error: 5.0368322875e-05

Current iteration: 11315
Current error: 5.01917966541e-05

Current iteration: 11316
Current error: 0.180460330284

Current iteration: 11317
Current error: 6.34975999868e-05

Current iteration: 11318
Current error: 6.30728344497e-05

Current iteration: 11319
Current error: 6.26735333558e-05

Current iteration: 11320
Current error: 6.22413010609e-05

Current iteration: 11321
Current error: 0.103963249427

Current iteration: 11322
Current error: 5.16445888837e-05

Current iteration: 11323
Current error: 0.139136765132

Current iteration: 11324
Current error: 4.22392580193e-05

Current iteration: 11325
Current error: 4.20083425238e-05

Current iteration: 11326
Current error: 4.1780199398e-05

Current iteration: 11327
Current error: 0.000559870343905

Current iteration: 11328
Current error: 4.08031644538e-05

Current iteration: 11329
Current error: 4.05940233004e-05

Current iteration: 11330
Current error: 4.03760150578e-05

Current iteration: 11331
Current error: 4.65935239496e-05

Current iteration: 11332
Current error: 0.11320932087

Current iteration: 11333
Current error: 0.00603576774047

Current iteration: 11334
Current error: 4.49657823993e-05

Current iteration: 11335
Current error: 4.46659914147e-05

Current iteration: 11336
Current error: 4.44128438123e-05

Current iteration: 11337
Current error: 4.41657529398e-05

Current iteration: 11338
Current error: 4.39210970728e-05

Current iteration: 11339
Current error: 4.36777927432e-05

Current iteration: 11340
Current error: 4.35319803743e-05

Current iteration: 11341
Current error: 4.31949567748e-05

Current iteration: 11342
Current error: 4.295576276e-05

Current iteration: 11343
Current error: 4.27202110025e-05

Current iteration: 11344
Current error: 4.24883932178e-05

Current iteration: 11345
Current error: 0.104454377155

Current iteration: 11346
Current error: 4.97749635843e-05

Current iteration: 11347
Current error: 4.94880723069e-05

Current iteration: 11348
Current error: 4.91860663095e-05

Current iteration: 11349
Current error: 4.88968827171e-05

Current iteration: 11350
Current error: 4.86082994325e-05

Current iteration: 11351
Current error: 4.83259035156e-05

Current iteration: 11352
Current error: 4.80783147391e-05

Current iteration: 11353
Current error: 4.776234402e-05

Current iteration: 11354
Current error: 4.8688768026e-05

Current iteration: 11355
Current error: 4.72088478664e-05

Current iteration: 11356
Current error: 4.69378538027e-05

Current iteration: 11357
Current error: 4.71504197769e-05

Current iteration: 11358
Current error: 4.64028943399e-05

Current iteration: 11359
Current error: 4.61732453357e-05

Current iteration: 11360
Current error: 4.58770285421e-05

Current iteration: 11361
Current error: 4.56120864142e-05

Current iteration: 11362
Current error: 0.109976993584

Current iteration: 11363
Current error: 7.03623186667e-05

Current iteration: 11364
Current error: 5.38193315335e-05

Current iteration: 11365
Current error: 5.31656907695e-05

Current iteration: 11366
Current error: 5.27867767797e-05

Current iteration: 11367
Current error: 5.24658881533e-05

Current iteration: 11368
Current error: 5.23697802201e-05

Current iteration: 11369
Current error: 5.18580001871e-05

Current iteration: 11370
Current error: 0.0015817580868

Current iteration: 11371
Current error: 5.01968159182e-05

Current iteration: 11372
Current error: 4.97177439545e-05

Current iteration: 11373
Current error: 4.94252411781e-05

Current iteration: 11374
Current error: 5.08908890405e-05

Current iteration: 11375
Current error: 4.88399672791e-05

Current iteration: 11376
Current error: 4.8570589569e-05

Current iteration: 11377
Current error: 4.82721702699e-05

Current iteration: 11378
Current error: 4.79888379255e-05

Current iteration: 11379
Current error: 0.0313528128653

Current iteration: 11380
Current error: 4.26566686811e-05

Current iteration: 11381
Current error: 4.24140923832e-05

Current iteration: 11382
Current error: 4.25411912904e-05

Current iteration: 11383
Current error: 0.110409250637

Current iteration: 11384
Current error: 3.49754715739e-05

Current iteration: 11385
Current error: 3.48481786239e-05

Current iteration: 11386
Current error: 3.46267475729e-05

Current iteration: 11387
Current error: 3.44619930156e-05

Current iteration: 11388
Current error: 3.42920594203e-05

Current iteration: 11389
Current error: 3.41243010614e-05

Current iteration: 11390
Current error: 3.39585935789e-05

Current iteration: 11391
Current error: 3.64820641668e-05

Current iteration: 11392
Current error: 3.36135925755e-05

Current iteration: 11393
Current error: 3.94130697621e-05

Current iteration: 11394
Current error: 3.32743253321e-05

Current iteration: 11395
Current error: 3.31178768636e-05

Current iteration: 11396
Current error: 3.2954413741e-05

Current iteration: 11397
Current error: 3.27967184285e-05

Current iteration: 11398
Current error: 3.31751485629e-05

Current iteration: 11399
Current error: 3.24896034648e-05

Current iteration: 11400
Current error: 3.2325253018e-05

Current iteration: 11401
Current error: 3.21693143194e-05

Current iteration: 11402
Current error: 3.21096533209e-05

Current iteration: 11403
Current error: 3.18662908198e-05

Current iteration: 11404
Current error: 3.19119168555e-05

Current iteration: 11405
Current error: 0.139844945801

Current iteration: 11406
Current error: 3.85887329451e-05

Current iteration: 11407
Current error: 0.456127750888

Current iteration: 11408
Current error: 6.37189241207e-05

Current iteration: 11409
Current error: 0.0751701638696

Current iteration: 11410
Current error: 5.52916247884e-05

Current iteration: 11411
Current error: 0.00288706208313

Current iteration: 11412
Current error: 0.10406567594

Current iteration: 11413
Current error: 4.30283157826e-05

Current iteration: 11414
Current error: 4.32315678404e-05

Current iteration: 11415
Current error: 4.26048923783e-05

Current iteration: 11416
Current error: 0.00236998968141

Current iteration: 11417
Current error: 4.08723136745e-05

Current iteration: 11418
Current error: 0.0300996800225

Current iteration: 11419
Current error: 3.64226315868e-05

Current iteration: 11420
Current error: 0.102449804472

Current iteration: 11421
Current error: 3.04198570318e-05

Current iteration: 11422
Current error: 3.02672661477e-05

Current iteration: 11423
Current error: 0.000274229128657

Current iteration: 11424
Current error: 3.14834737828e-05

Current iteration: 11425
Current error: 0.0624033901841

Current iteration: 11426
Current error: 0.0190654051818

Current iteration: 11427
Current error: 2.34416672885e-05

Current iteration: 11428
Current error: 2.46842809641e-05

Current iteration: 11429
Current error: 2.32483198608e-05

Current iteration: 11430
Current error: 2.31538516621e-05

Current iteration: 11431
Current error: 0.0161528780777

Current iteration: 11432
Current error: 2.12566575195e-05

Current iteration: 11433
Current error: 2.12121675499e-05

Current iteration: 11434
Current error: 4.37953443013e-05

Current iteration: 11435
Current error: 2.09791120312e-05

Current iteration: 11436
Current error: 2.09000409151e-05

Current iteration: 11437
Current error: 2.08196190494e-05

Current iteration: 11438
Current error: 2.07368542048e-05

Current iteration: 11439
Current error: 2.06578763989e-05

Current iteration: 11440
Current error: 0.000952685619536

Current iteration: 11441
Current error: 2.01122535321e-05

Current iteration: 11442
Current error: 2.00364294759e-05

Current iteration: 11443
Current error: 2.00082913751e-05

Current iteration: 11444
Current error: 2.05719930694e-05

Current iteration: 11445
Current error: 1.98113164154e-05

Current iteration: 11446
Current error: 0.000913926561752

Current iteration: 11447
Current error: 1.93018537088e-05

Current iteration: 11448
Current error: 1.92291799861e-05

Current iteration: 11449
Current error: 1.91592067556e-05

Current iteration: 11450
Current error: 1.90943069382e-05

Current iteration: 11451
Current error: 1.95772928269e-05

Current iteration: 11452
Current error: 1.92208497827e-05

Current iteration: 11453
Current error: 0.00999542815265

Current iteration: 11454
Current error: 1.76963849251e-05

Current iteration: 11455
Current error: 1.76154616649e-05

Current iteration: 11456
Current error: 1.76572599164e-05

Current iteration: 11457
Current error: 1.74916901399e-05

Current iteration: 11458
Current error: 1.74300664606e-05

Current iteration: 11459
Current error: 5.39227965064e-05

Current iteration: 11460
Current error: 1.72784922072e-05

Current iteration: 11461
Current error: 1.72037794847e-05

Current iteration: 11462
Current error: 1.71444121095e-05

Current iteration: 11463
Current error: 1.71293257095e-05

Current iteration: 11464
Current error: 1.70259705291e-05

Current iteration: 11465
Current error: 1.69777018035e-05

Current iteration: 11466
Current error: 5.12916111936e-05

Current iteration: 11467
Current error: 1.68146230067e-05

Current iteration: 11468
Current error: 4.43300759748e-05

Current iteration: 11469
Current error: 1.68987961236e-05

Current iteration: 11470
Current error: 0.00258099283792

Current iteration: 11471
Current error: 1.60187673619e-05

Current iteration: 11472
Current error: 0.174409015227

Current iteration: 11473
Current error: 1.98657775939e-05

Current iteration: 11474
Current error: 1.98001107851e-05

Current iteration: 11475
Current error: 1.98296496032e-05

Current iteration: 11476
Current error: 1.97801285894e-05

Current iteration: 11477
Current error: 1.95683766486e-05

Current iteration: 11478
Current error: 1.94953065606e-05

Current iteration: 11479
Current error: 1.94227062629e-05

Current iteration: 11480
Current error: 1.93504862758e-05

Current iteration: 11481
Current error: 3.59116079012e-05

Current iteration: 11482
Current error: 1.91856522963e-05

Current iteration: 11483
Current error: 1.91132394699e-05

Current iteration: 11484
Current error: 1.90422378333e-05

Current iteration: 11485
Current error: 1.89778106081e-05

Current iteration: 11486
Current error: 2.46471116537e-05

Current iteration: 11487
Current error: 1.88280484508e-05

Current iteration: 11488
Current error: 1.87563804885e-05

Current iteration: 11489
Current error: 1.86881042349e-05

Current iteration: 11490
Current error: 1.86211494482e-05

Current iteration: 11491
Current error: 1.86478561213e-05

Current iteration: 11492
Current error: 0.0304386957557

Current iteration: 11493
Current error: 1.66158367556e-05

Current iteration: 11494
Current error: 1.65618743647e-05

Current iteration: 11495
Current error: 1.65032957866e-05

Current iteration: 11496
Current error: 0.172569573064

Current iteration: 11497
Current error: 2.06004266452e-05

Current iteration: 11498
Current error: 2.05236969744e-05

Current iteration: 11499
Current error: 2.04450321787e-05

Current iteration: 11500
Current error: 2.03643903619e-05

Current iteration: 11501
Current error: 2.02897190443e-05

Current iteration: 11502
Current error: 2.02114546006e-05

Current iteration: 11503
Current error: 0.0177180373615

Current iteration: 11504
Current error: 1.8526333042e-05

Current iteration: 11505
Current error: 0.0301051643321

Current iteration: 11506
Current error: 1.65660835691e-05

Current iteration: 11507
Current error: 2.23220068327e-05

Current iteration: 11508
Current error: 1.68878850499e-05

Current iteration: 11509
Current error: 1.63868234076e-05

Current iteration: 11510
Current error: 1.6332772069e-05

Current iteration: 11511
Current error: 1.65262141451e-05

Current iteration: 11512
Current error: 1.62207792109e-05

Current iteration: 11513
Current error: 1.61671027433e-05

Current iteration: 11514
Current error: 1.61143595868e-05

Current iteration: 11515
Current error: 1.69868244078e-05

Current iteration: 11516
Current error: 1.66841311478e-05

Current iteration: 11517
Current error: 1.59605881478e-05

Current iteration: 11518
Current error: 1.60251981658e-05

Current iteration: 11519
Current error: 1.58394808307e-05

Current iteration: 11520
Current error: 1.57928710061e-05

Current iteration: 11521
Current error: 1.58307881661e-05

Current iteration: 11522
Current error: 1.567856564e-05

Current iteration: 11523
Current error: 1.6118533671e-05

Current iteration: 11524
Current error: 0.0247838018717

Current iteration: 11525
Current error: 1.41642285597e-05

Current iteration: 11526
Current error: 1.40867527861e-05

Current iteration: 11527
Current error: 1.4044181666e-05

Current iteration: 11528
Current error: 1.39998209697e-05

Current iteration: 11529
Current error: 1.39595399222e-05

Current iteration: 11530
Current error: 1.39148229589e-05

Current iteration: 11531
Current error: 2.14703111824e-05

Current iteration: 11532
Current error: 1.44073313074e-05

Current iteration: 11533
Current error: 0.0158812399827

Current iteration: 11534
Current error: 1.27559506971e-05

Current iteration: 11535
Current error: 1.45419357821e-05

Current iteration: 11536
Current error: 0.253940135389

Current iteration: 11537
Current error: 1.70748686051e-05

Current iteration: 11538
Current error: 0.0185563612792

Current iteration: 11539
Current error: 1.54835244624e-05

Current iteration: 11540
Current error: 1.54350407129e-05

Current iteration: 11541
Current error: 1.56270845326e-05

Current iteration: 11542
Current error: 1.53321926648e-05

Current iteration: 11543
Current error: 0.00815470397279

Current iteration: 11544
Current error: 1.43955146218e-05

Current iteration: 11545
Current error: 1.43501366867e-05

Current iteration: 11546
Current error: 1.43031480172e-05

Current iteration: 11547
Current error: 0.0580894488821

Current iteration: 11548
Current error: 0.199882875119

Current iteration: 11549
Current error: 0.222582280402

Current iteration: 11550
Current error: 2.07692817708e-05

Current iteration: 11551
Current error: 2.0690700498e-05

Current iteration: 11552
Current error: 2.06122095366e-05

Current iteration: 11553
Current error: 2.05310463552e-05

Current iteration: 11554
Current error: 2.04553280146e-05

Current iteration: 11555
Current error: 2.03771703324e-05

Current iteration: 11556
Current error: 2.04150737497e-05

Current iteration: 11557
Current error: 2.02457886299e-05

Current iteration: 11558
Current error: 0.309135709223

Current iteration: 11559
Current error: 2.86772809606e-05

Current iteration: 11560
Current error: 2.84516677547e-05

Current iteration: 11561
Current error: 2.9424188227e-05

Current iteration: 11562
Current error: 2.82119356713e-05

Current iteration: 11563
Current error: 2.80840848445e-05

Current iteration: 11564
Current error: 0.000256203378669

Current iteration: 11565
Current error: 2.75934312521e-05

Current iteration: 11566
Current error: 2.74776198914e-05

Current iteration: 11567
Current error: 2.8770274312e-05

Current iteration: 11568
Current error: 0.0932222460049

Current iteration: 11569
Current error: 2.30766324024e-05

Current iteration: 11570
Current error: 2.29244171806e-05

Current iteration: 11571
Current error: 2.28319105038e-05

Current iteration: 11572
Current error: 2.27394752446e-05

Current iteration: 11573
Current error: 2.35992413757e-05

Current iteration: 11574
Current error: 0.00235289955493

Current iteration: 11575
Current error: 2.17843371498e-05

Current iteration: 11576
Current error: 2.16991107367e-05

Current iteration: 11577
Current error: 2.16154586078e-05

Current iteration: 11578
Current error: 0.0141729712942

Current iteration: 11579
Current error: 1.99227198896e-05

Current iteration: 11580
Current error: 2.38607483798e-05

Current iteration: 11581
Current error: 0.020273264539

Current iteration: 11582
Current error: 1.80576436186e-05

Current iteration: 11583
Current error: 1.80671662238e-05

Current iteration: 11584
Current error: 1.79264057673e-05

Current iteration: 11585
Current error: 1.7872071975e-05

Current iteration: 11586
Current error: 1.78003048889e-05

Current iteration: 11587
Current error: 0.0231204203417

Current iteration: 11588
Current error: 1.71527874515e-05

Current iteration: 11589
Current error: 1.60758580737e-05

Current iteration: 11590
Current error: 1.60552350984e-05

Current iteration: 11591
Current error: 1.59685991929e-05

Current iteration: 11592
Current error: 1.59210126334e-05

Current iteration: 11593
Current error: 5.59208410341e-05

Current iteration: 11594
Current error: 0.159661623927

Current iteration: 11595
Current error: 1.93889389409e-05

Current iteration: 11596
Current error: 2.01080717686e-05

Current iteration: 11597
Current error: 1.92437617904e-05

Current iteration: 11598
Current error: 2.27593980083e-05

Current iteration: 11599
Current error: 1.90966284644e-05

Current iteration: 11600
Current error: 1.91257148621e-05

Current iteration: 11601
Current error: 1.89575561054e-05

Current iteration: 11602
Current error: 1.88872867186e-05

Current iteration: 11603
Current error: 1.88479997673e-05

Current iteration: 11604
Current error: 1.88006806977e-05

Current iteration: 11605
Current error: 1.87449055807e-05

Current iteration: 11606
Current error: 1.86134253396e-05

Current iteration: 11607
Current error: 0.0685778063059

Current iteration: 11608
Current error: 1.59968407615e-05

Current iteration: 11609
Current error: 1.59446805649e-05

Current iteration: 11610
Current error: 1.59197924588e-05

Current iteration: 11611
Current error: 1.58349885143e-05

Current iteration: 11612
Current error: 1.57836479814e-05

Current iteration: 11613
Current error: 9.94523656188e-05

Current iteration: 11614
Current error: 1.63131202221e-05

Current iteration: 11615
Current error: 1.56019142559e-05

Current iteration: 11616
Current error: 0.156938499698

Current iteration: 11617
Current error: 1.92819172922e-05

Current iteration: 11618
Current error: 1.90546755635e-05

Current iteration: 11619
Current error: 1.89833398559e-05

Current iteration: 11620
Current error: 1.8921335948e-05

Current iteration: 11621
Current error: 1.88783764671e-05

Current iteration: 11622
Current error: 1.8773552756e-05

Current iteration: 11623
Current error: 1.87200141226e-05

Current iteration: 11624
Current error: 1.86396223255e-05

Current iteration: 11625
Current error: 0.127812718159

Current iteration: 11626
Current error: 0.000307480447357

Current iteration: 11627
Current error: 2.69816798855e-05

Current iteration: 11628
Current error: 0.0271533860458

Current iteration: 11629
Current error: 2.01041150804e-05

Current iteration: 11630
Current error: 1.96243483824e-05

Current iteration: 11631
Current error: 2.88800883561e-05

Current iteration: 11632
Current error: 1.94628175327e-05

Current iteration: 11633
Current error: 1.93884866119e-05

Current iteration: 11634
Current error: 2.14241911949e-05

Current iteration: 11635
Current error: 1.92424561898e-05

Current iteration: 11636
Current error: 1.91729027415e-05

Current iteration: 11637
Current error: 1.91086744559e-05

Current iteration: 11638
Current error: 0.00137475947202

Current iteration: 11639
Current error: 1.85279830532e-05

Current iteration: 11640
Current error: 1.84606826667e-05

Current iteration: 11641
Current error: 0.137762088071

Current iteration: 11642
Current error: 2.22473009463e-05

Current iteration: 11643
Current error: 0.000272331920741

Current iteration: 11644
Current error: 2.20092105833e-05

Current iteration: 11645
Current error: 2.17949249877e-05

Current iteration: 11646
Current error: 2.17094329871e-05

Current iteration: 11647
Current error: 2.16213655459e-05

Current iteration: 11648
Current error: 2.15353043426e-05

Current iteration: 11649
Current error: 6.86834204413e-05

Current iteration: 11650
Current error: 2.13065812275e-05

Current iteration: 11651
Current error: 2.12252508088e-05

Current iteration: 11652
Current error: 8.92620585447e-05

Current iteration: 11653
Current error: 2.09817755802e-05

Current iteration: 11654
Current error: 2.09093123479e-05

Current iteration: 11655
Current error: 2.0825725778e-05

Current iteration: 11656
Current error: 2.07895131551e-05

Current iteration: 11657
Current error: 2.06624254377e-05

Current iteration: 11658
Current error: 2.05830662511e-05

Current iteration: 11659
Current error: 2.05234662486e-05

Current iteration: 11660
Current error: 0.03415489708

Current iteration: 11661
Current error: 1.82425364751e-05

Current iteration: 11662
Current error: 7.40092553892e-05

Current iteration: 11663
Current error: 0.0041353570475

Current iteration: 11664
Current error: 1.72634277637e-05

Current iteration: 11665
Current error: 1.72030336039e-05

Current iteration: 11666
Current error: 1.71418335993e-05

Current iteration: 11667
Current error: 0.128472871826

Current iteration: 11668
Current error: 2.06118348634e-05

Current iteration: 11669
Current error: 2.04087988614e-05

Current iteration: 11670
Current error: 2.03322756665e-05

Current iteration: 11671
Current error: 2.0253864796e-05

Current iteration: 11672
Current error: 2.01811870233e-05

Current iteration: 11673
Current error: 2.01143718571e-05

Current iteration: 11674
Current error: 2.00230733116e-05

Current iteration: 11675
Current error: 2.02478784636e-05

Current iteration: 11676
Current error: 0.0684181617346

Current iteration: 11677
Current error: 1.71090206873e-05

Current iteration: 11678
Current error: 0.13794788547

Current iteration: 11679
Current error: 0.33349493145

Current iteration: 11680
Current error: 0.104104082062

Current iteration: 11681
Current error: 2.53792942731e-05

Current iteration: 11682
Current error: 2.50882763523e-05

Current iteration: 11683
Current error: 2.49082130173e-05

Current iteration: 11684
Current error: 4.64668674194e-05

Current iteration: 11685
Current error: 0.110486719181

Current iteration: 11686
Current error: 2.95130945341e-05

Current iteration: 11687
Current error: 2.91041229088e-05

Current iteration: 11688
Current error: 2.89833907592e-05

Current iteration: 11689
Current error: 0.00151919258212

Current iteration: 11690
Current error: 2.80351874662e-05

Current iteration: 11691
Current error: 2.7903491555e-05

Current iteration: 11692
Current error: 2.77827041468e-05

Current iteration: 11693
Current error: 2.76562601906e-05

Current iteration: 11694
Current error: 2.96131759946e-05

Current iteration: 11695
Current error: 2.7409844677e-05

Current iteration: 11696
Current error: 0.103128223523

Current iteration: 11697
Current error: 0.00744504535616

Current iteration: 11698
Current error: 3.02650277525e-05

Current iteration: 11699
Current error: 0.0175303758132

Current iteration: 11700
Current error: 2.76018850099e-05

Current iteration: 11701
Current error: 2.76447312555e-05

Current iteration: 11702
Current error: 2.73613408149e-05

Current iteration: 11703
Current error: 2.7239373882e-05

Current iteration: 11704
Current error: 2.71305936968e-05

Current iteration: 11705
Current error: 2.7003198468e-05

Current iteration: 11706
Current error: 2.68837035832e-05

Current iteration: 11707
Current error: 2.67812684256e-05

Current iteration: 11708
Current error: 0.0877702567212

Current iteration: 11709
Current error: 2.25446568983e-05

Current iteration: 11710
Current error: 0.113511020801

Current iteration: 11711
Current error: 0.0948775164127

Current iteration: 11712
Current error: 3.09281004803e-05

Current iteration: 11713
Current error: 3.0761872494e-05

Current iteration: 11714
Current error: 3.06160916967e-05

Current iteration: 11715
Current error: 3.04736092324e-05

Current iteration: 11716
Current error: 0.0519795642363

Current iteration: 11717
Current error: 2.65858331681e-05

Current iteration: 11718
Current error: 2.64036782194e-05

Current iteration: 11719
Current error: 2.6212735648e-05

Current iteration: 11720
Current error: 2.61033094766e-05

Current iteration: 11721
Current error: 2.59896303349e-05

Current iteration: 11722
Current error: 2.58808871477e-05

Current iteration: 11723
Current error: 2.59227920366e-05

Current iteration: 11724
Current error: 2.57985720381e-05

Current iteration: 11725
Current error: 2.55547561431e-05

Current iteration: 11726
Current error: 2.55196988347e-05

Current iteration: 11727
Current error: 2.53333028987e-05

Current iteration: 11728
Current error: 2.8654102068e-05

Current iteration: 11729
Current error: 2.51114775596e-05

Current iteration: 11730
Current error: 2.50060052085e-05

Current iteration: 11731
Current error: 2.49014130595e-05

Current iteration: 11732
Current error: 2.48016256245e-05

Current iteration: 11733
Current error: 2.46902039916e-05

Current iteration: 11734
Current error: 0.102780737163

Current iteration: 11735
Current error: 0.0456164218785

Current iteration: 11736
Current error: 2.52912072023e-05

Current iteration: 11737
Current error: 0.0589982294796

Current iteration: 11738
Current error: 2.18567797082e-05

Current iteration: 11739
Current error: 2.173404698e-05

Current iteration: 11740
Current error: 2.16529961547e-05

Current iteration: 11741
Current error: 2.15666166304e-05

Current iteration: 11742
Current error: 2.14795729592e-05

Current iteration: 11743
Current error: 2.13961472888e-05

Current iteration: 11744
Current error: 2.13136968483e-05

Current iteration: 11745
Current error: 2.12365393891e-05

Current iteration: 11746
Current error: 0.00210464751907

Current iteration: 11747
Current error: 2.04551553971e-05

Current iteration: 11748
Current error: 2.03789881957e-05

Current iteration: 11749
Current error: 3.40230450605e-05

Current iteration: 11750
Current error: 2.02050110447e-05

Current iteration: 11751
Current error: 2.01273243859e-05

Current iteration: 11752
Current error: 2.00515558005e-05

Current iteration: 11753
Current error: 0.00029315251841

Current iteration: 11754
Current error: 1.97142207436e-05

Current iteration: 11755
Current error: 1.96400797703e-05

Current iteration: 11756
Current error: 1.95664621447e-05

Current iteration: 11757
Current error: 4.34330968938e-05

Current iteration: 11758
Current error: 2.86519547021e-05

Current iteration: 11759
Current error: 1.93024089671e-05

Current iteration: 11760
Current error: 1.92345393907e-05

Current iteration: 11761
Current error: 1.91717475685e-05

Current iteration: 11762
Current error: 1.90893897588e-05

Current iteration: 11763
Current error: 1.9019632894e-05

Current iteration: 11764
Current error: 1.89467031937e-05

Current iteration: 11765
Current error: 1.888816383e-05

Current iteration: 11766
Current error: 1.90292492631e-05

Current iteration: 11767
Current error: 1.87416265292e-05

Current iteration: 11768
Current error: 0.123623579924

Current iteration: 11769
Current error: 2.24123189479e-05

Current iteration: 11770
Current error: 2.23312336062e-05

Current iteration: 11771
Current error: 2.22382466498e-05

Current iteration: 11772
Current error: 2.214466585e-05

Current iteration: 11773
Current error: 2.20651855245e-05

Current iteration: 11774
Current error: 0.102899844428

Current iteration: 11775
Current error: 2.58252363397e-05

Current iteration: 11776
Current error: 2.57146987481e-05

Current iteration: 11777
Current error: 0.00052470273555

Current iteration: 11778
Current error: 2.51663505629e-05

Current iteration: 11779
Current error: 3.03540659372e-05

Current iteration: 11780
Current error: 3.35541030399e-05

Current iteration: 11781
Current error: 2.48185579404e-05

Current iteration: 11782
Current error: 2.47152046772e-05

Current iteration: 11783
Current error: 2.46126898368e-05

Current iteration: 11784
Current error: 2.45067149483e-05

Current iteration: 11785
Current error: 2.44769603492e-05

Current iteration: 11786
Current error: 2.43036174247e-05

Current iteration: 11787
Current error: 2.42036302963e-05

Current iteration: 11788
Current error: 4.6837901535e-05

Current iteration: 11789
Current error: 0.097287126642

Current iteration: 11790
Current error: 2.0149093939e-05

Current iteration: 11791
Current error: 2.00761883281e-05

Current iteration: 11792
Current error: 1.99876020776e-05

Current iteration: 11793
Current error: 1.99240241046e-05

Current iteration: 11794
Current error: 1.98333651719e-05

Current iteration: 11795
Current error: 0.110407731878

Current iteration: 11796
Current error: 2.3429567242e-05

Current iteration: 11797
Current error: 2.33328544261e-05

Current iteration: 11798
Current error: 2.3239878354e-05

Current iteration: 11799
Current error: 2.31434165686e-05

Current iteration: 11800
Current error: 2.30518526733e-05

Current iteration: 11801
Current error: 2.29598025957e-05

Current iteration: 11802
Current error: 0.093296809554

Current iteration: 11803
Current error: 1.92691134691e-05

Current iteration: 11804
Current error: 1.91979952962e-05

Current iteration: 11805
Current error: 1.91272365953e-05

Current iteration: 11806
Current error: 0.0933459479563

Current iteration: 11807
Current error: 1.60811255817e-05

Current iteration: 11808
Current error: 0.0354255277057

Current iteration: 11809
Current error: 1.42900169546e-05

Current iteration: 11810
Current error: 1.42499128513e-05

Current iteration: 11811
Current error: 1.42135848426e-05

Current iteration: 11812
Current error: 0.169928020352

Current iteration: 11813
Current error: 1.7782354241e-05

Current iteration: 11814
Current error: 1.76986546135e-05

Current iteration: 11815
Current error: 1.76374926231e-05

Current iteration: 11816
Current error: 1.75742024884e-05

Current iteration: 11817
Current error: 1.83872045781e-05

Current iteration: 11818
Current error: 0.000545153289361

Current iteration: 11819
Current error: 1.7149159969e-05

Current iteration: 11820
Current error: 1.70878563656e-05

Current iteration: 11821
Current error: 1.70282657837e-05

Current iteration: 11822
Current error: 1.70800430729e-05

Current iteration: 11823
Current error: 1.81197361623e-05

Current iteration: 11824
Current error: 1.69995882465e-05

Current iteration: 11825
Current error: 0.00125331328783

Current iteration: 11826
Current error: 0.2834959073

Current iteration: 11827
Current error: 0.000814045289613

Current iteration: 11828
Current error: 2.22866677451e-05

Current iteration: 11829
Current error: 2.21768712991e-05

Current iteration: 11830
Current error: 2.20883843349e-05

Current iteration: 11831
Current error: 2.20029282504e-05

Current iteration: 11832
Current error: 2.39596133246e-05

Current iteration: 11833
Current error: 2.1839719246e-05

Current iteration: 11834
Current error: 2.36226539548e-05

Current iteration: 11835
Current error: 0.00037328877498

Current iteration: 11836
Current error: 2.13297211058e-05

Current iteration: 11837
Current error: 2.12477099874e-05

Current iteration: 11838
Current error: 0.137844330726

Current iteration: 11839
Current error: 2.58497195547e-05

Current iteration: 11840
Current error: 2.57570247808e-05

Current iteration: 11841
Current error: 2.56292694185e-05

Current iteration: 11842
Current error: 0.098297564792

Current iteration: 11843
Current error: 2.14071479488e-05

Current iteration: 11844
Current error: 0.0285043979799

Current iteration: 11845
Current error: 2.25481840972e-05

Current iteration: 11846
Current error: 1.98936458773e-05

Current iteration: 11847
Current error: 1.90344432483e-05

Current iteration: 11848
Current error: 0.108223260356

Current iteration: 11849
Current error: 0.000805760007719

Current iteration: 11850
Current error: 2.19554038928e-05

Current iteration: 11851
Current error: 2.18884668848e-05

Current iteration: 11852
Current error: 2.18855257921e-05

Current iteration: 11853
Current error: 2.17106974044e-05

Current iteration: 11854
Current error: 2.16129264635e-05

Current iteration: 11855
Current error: 0.0320614593465

Current iteration: 11856
Current error: 1.92674229976e-05

Current iteration: 11857
Current error: 6.59853537305e-05

Current iteration: 11858
Current error: 2.23102142069e-05

Current iteration: 11859
Current error: 1.89908046852e-05

Current iteration: 11860
Current error: 1.89184154119e-05

Current iteration: 11861
Current error: 1.88490535719e-05

Current iteration: 11862
Current error: 1.8778669977e-05

Current iteration: 11863
Current error: 1.87119258844e-05

Current iteration: 11864
Current error: 0.114915144568

Current iteration: 11865
Current error: 2.21428212349e-05

Current iteration: 11866
Current error: 2.22580369208e-05

Current iteration: 11867
Current error: 2.23190639444e-05

Current iteration: 11868
Current error: 2.18814116451e-05

Current iteration: 11869
Current error: 2.18098050013e-05

Current iteration: 11870
Current error: 2.17074228086e-05

Current iteration: 11871
Current error: 2.16302345465e-05

Current iteration: 11872
Current error: 2.27834090622e-05

Current iteration: 11873
Current error: 2.14524852793e-05

Current iteration: 11874
Current error: 2.13682022779e-05

Current iteration: 11875
Current error: 0.0135412502854

Current iteration: 11876
Current error: 1.97100770574e-05

Current iteration: 11877
Current error: 1.96348415023e-05

Current iteration: 11878
Current error: 1.95651479869e-05

Current iteration: 11879
Current error: 1.9503588771e-05

Current iteration: 11880
Current error: 1.94182907596e-05

Current iteration: 11881
Current error: 1.93460198128e-05

Current iteration: 11882
Current error: 2.37077353737e-05

Current iteration: 11883
Current error: 1.91956031612e-05

Current iteration: 11884
Current error: 0.00770272498244

Current iteration: 11885
Current error: 1.80819194969e-05

Current iteration: 11886
Current error: 1.79730465004e-05

Current iteration: 11887
Current error: 3.27125675323e-05

Current iteration: 11888
Current error: 0.000536729016247

Current iteration: 11889
Current error: 1.74907665931e-05

Current iteration: 11890
Current error: 1.74287421561e-05

Current iteration: 11891
Current error: 1.73706167252e-05

Current iteration: 11892
Current error: 1.80140806551e-05

Current iteration: 11893
Current error: 1.72393246673e-05

Current iteration: 11894
Current error: 1.71841075371e-05

Current iteration: 11895
Current error: 1.71270325976e-05

Current iteration: 11896
Current error: 1.71102418603e-05

Current iteration: 11897
Current error: 1.70431671051e-05

Current iteration: 11898
Current error: 1.69466263484e-05

Current iteration: 11899
Current error: 1.6888302933e-05

Current iteration: 11900
Current error: 1.68481137117e-05

Current iteration: 11901
Current error: 1.67975445046e-05

Current iteration: 11902
Current error: 1.67083302406e-05

Current iteration: 11903
Current error: 1.66784924621e-05

Current iteration: 11904
Current error: 1.66269141085e-05

Current iteration: 11905
Current error: 1.65375894684e-05

Current iteration: 11906
Current error: 1.64957963465e-05

Current iteration: 11907
Current error: 1.64289166253e-05

Current iteration: 11908
Current error: 1.63751629006e-05

Current iteration: 11909
Current error: 1.63276440317e-05

Current iteration: 11910
Current error: 1.6261307763e-05

Current iteration: 11911
Current error: 1.62123543036e-05

Current iteration: 11912
Current error: 1.62052663475e-05

Current iteration: 11913
Current error: 1.66891507527e-05

Current iteration: 11914
Current error: 0.349282071297

Current iteration: 11915
Current error: 2.36625759518e-05

Current iteration: 11916
Current error: 2.35580603351e-05

Current iteration: 11917
Current error: 2.34718772051e-05

Current iteration: 11918
Current error: 2.36228568025e-05

Current iteration: 11919
Current error: 2.32720421076e-05

Current iteration: 11920
Current error: 2.31777991902e-05

Current iteration: 11921
Current error: 0.000522281680564

Current iteration: 11922
Current error: 2.26853174939e-05

Current iteration: 11923
Current error: 2.35095766376e-05

Current iteration: 11924
Current error: 2.33780978635e-05

Current iteration: 11925
Current error: 2.24955236447e-05

Current iteration: 11926
Current error: 2.23218701473e-05

Current iteration: 11927
Current error: 2.22326678278e-05

Current iteration: 11928
Current error: 0.102513519089

Current iteration: 11929
Current error: 2.60329083045e-05

Current iteration: 11930
Current error: 0.110645930102

Current iteration: 11931
Current error: 0.000881787552049

Current iteration: 11932
Current error: 0.109266062706

Current iteration: 11933
Current error: 1.7594799513e-05

Current iteration: 11934
Current error: 1.75444388889e-05

Current iteration: 11935
Current error: 1.75896966624e-05

Current iteration: 11936
Current error: 1.74081664026e-05

Current iteration: 11937
Current error: 1.73462806277e-05

Current iteration: 11938
Current error: 1.72911398278e-05

Current iteration: 11939
Current error: 1.72295514955e-05

Current iteration: 11940
Current error: 1.71662157059e-05

Current iteration: 11941
Current error: 1.7102224535e-05

Current iteration: 11942
Current error: 2.07506000313e-05

Current iteration: 11943
Current error: 0.108039948325

Current iteration: 11944
Current error: 2.00874646633e-05

Current iteration: 11945
Current error: 2.00128614213e-05

Current iteration: 11946
Current error: 1.99372394201e-05

Current iteration: 11947
Current error: 1.98589247146e-05

Current iteration: 11948
Current error: 1.97884554887e-05

Current iteration: 11949
Current error: 1.9713625094e-05

Current iteration: 11950
Current error: 0.000356728655043

Current iteration: 11951
Current error: 0.0427579136986

Current iteration: 11952
Current error: 1.70597868396e-05

Current iteration: 11953
Current error: 1.69987491186e-05

Current iteration: 11954
Current error: 1.69668714761e-05

Current iteration: 11955
Current error: 1.69318193537e-05

Current iteration: 11956
Current error: 0.0001973946278

Current iteration: 11957
Current error: 1.66409423459e-05

Current iteration: 11958
Current error: 1.65829392669e-05

Current iteration: 11959
Current error: 1.65267953466e-05

Current iteration: 11960
Current error: 1.65784113617e-05

Current iteration: 11961
Current error: 1.6413033384e-05

Current iteration: 11962
Current error: 0.0216507762088

Current iteration: 11963
Current error: 1.86642382327e-05

Current iteration: 11964
Current error: 1.48421269984e-05

Current iteration: 11965
Current error: 1.48391346519e-05

Current iteration: 11966
Current error: 2.57820353339e-05

Current iteration: 11967
Current error: 1.4698608282e-05

Current iteration: 11968
Current error: 0.0208715512228

Current iteration: 11969
Current error: 1.33557543041e-05

Current iteration: 11970
Current error: 1.33101769418e-05

Current iteration: 11971
Current error: 1.32698255404e-05

Current iteration: 11972
Current error: 0.00646756061858

Current iteration: 11973
Current error: 1.25270476248e-05

Current iteration: 11974
Current error: 1.25656888627e-05

Current iteration: 11975
Current error: 1.24528587675e-05

Current iteration: 11976
Current error: 1.24171742697e-05

Current iteration: 11977
Current error: 1.2385010852e-05

Current iteration: 11978
Current error: 1.24171683267e-05

Current iteration: 11979
Current error: 1.23689857294e-05

Current iteration: 11980
Current error: 1.22680538481e-05

Current iteration: 11981
Current error: 1.22345298239e-05

Current iteration: 11982
Current error: 3.783022108e-05

Current iteration: 11983
Current error: 0.0773667621957

Current iteration: 11984
Current error: 1.03857011001e-05

Current iteration: 11985
Current error: 1.31113950539e-05

Current iteration: 11986
Current error: 1.03263744269e-05

Current iteration: 11987
Current error: 1.02993268511e-05

Current iteration: 11988
Current error: 1.0279123008e-05

Current iteration: 11989
Current error: 1.28627961815e-05

Current iteration: 11990
Current error: 1.02122448178e-05

Current iteration: 11991
Current error: 1.04476731786e-05

Current iteration: 11992
Current error: 1.01545574707e-05

Current iteration: 11993
Current error: 1.01294565499e-05

Current iteration: 11994
Current error: 1.01064776687e-05

Current iteration: 11995
Current error: 0.00683833479282

Current iteration: 11996
Current error: 1.20159064027e-05

Current iteration: 11997
Current error: 9.51778781363e-06

Current iteration: 11998
Current error: 9.47886332267e-06

Current iteration: 11999
Current error: 9.55017323104e-06

Current iteration: 12000
Current error: 0.0677526964559

Current iteration: 12001
Current error: 8.14178871835e-06

Current iteration: 12002
Current error: 8.43974635532e-06

Current iteration: 12003
Current error: 0.000198211203727

Current iteration: 12004
Current error: 0.0116253922362

Current iteration: 12005
Current error: 7.47373785337e-06

Current iteration: 12006
Current error: 8.56030210945e-06

Current iteration: 12007
Current error: 7.46354086247e-06

Current iteration: 12008
Current error: 7.42153233622e-06

Current iteration: 12009
Current error: 7.41376342154e-06

Current iteration: 12010
Current error: 0.253868421832

Current iteration: 12011
Current error: 9.93470843948e-06

Current iteration: 12012
Current error: 9.90900732248e-06

Current iteration: 12013
Current error: 1.61083083214e-05

Current iteration: 12014
Current error: 9.85097291023e-06

Current iteration: 12015
Current error: 0.151554046387

Current iteration: 12016
Current error: 1.22378615137e-05

Current iteration: 12017
Current error: 6.76432395936e-05

Current iteration: 12018
Current error: 1.19683171487e-05

Current iteration: 12019
Current error: 1.19321054928e-05

Current iteration: 12020
Current error: 1.18976324437e-05

Current iteration: 12021
Current error: 1.18877967161e-05

Current iteration: 12022
Current error: 1.18371550938e-05

Current iteration: 12023
Current error: 1.17943759044e-05

Current iteration: 12024
Current error: 1.17598686519e-05

Current iteration: 12025
Current error: 1.17705254289e-05

Current iteration: 12026
Current error: 1.16988735974e-05

Current iteration: 12027
Current error: 1.16579671878e-05

Current iteration: 12028
Current error: 1.16237153903e-05

Current iteration: 12029
Current error: 1.15917899603e-05

Current iteration: 12030
Current error: 1.15586733725e-05

Current iteration: 12031
Current error: 1.15272006073e-05

Current iteration: 12032
Current error: 1.14916092854e-05

Current iteration: 12033
Current error: 1.1458906586e-05

Current iteration: 12034
Current error: 1.1426559037e-05

Current iteration: 12035
Current error: 1.78539813121e-05

Current iteration: 12036
Current error: 1.13560202969e-05

Current iteration: 12037
Current error: 0.0005922749142

Current iteration: 12038
Current error: 1.11208587624e-05

Current iteration: 12039
Current error: 1.10895039024e-05

Current iteration: 12040
Current error: 0.036621706267

Current iteration: 12041
Current error: 9.92012906841e-06

Current iteration: 12042
Current error: 9.82333078559e-06

Current iteration: 12043
Current error: 9.89251469741e-06

Current iteration: 12044
Current error: 9.77155350882e-06

Current iteration: 12045
Current error: 1.02526874728e-05

Current iteration: 12046
Current error: 9.71906149387e-06

Current iteration: 12047
Current error: 9.69419239111e-06

Current iteration: 12048
Current error: 0.136228441828

Current iteration: 12049
Current error: 1.16779087664e-05

Current iteration: 12050
Current error: 1.16456088139e-05

Current iteration: 12051
Current error: 1.16101503637e-05

Current iteration: 12052
Current error: 1.15763512955e-05

Current iteration: 12053
Current error: 1.15527101034e-05

Current iteration: 12054
Current error: 1.15132384468e-05

Current iteration: 12055
Current error: 0.0642821675023

Current iteration: 12056
Current error: 9.93702394681e-06

Current iteration: 12057
Current error: 9.90439598728e-06

Current iteration: 12058
Current error: 9.8711479847e-06

Current iteration: 12059
Current error: 9.89653340681e-06

Current iteration: 12060
Current error: 9.81692229082e-06

Current iteration: 12061
Current error: 9.78963624005e-06

Current iteration: 12062
Current error: 9.76286235386e-06

Current iteration: 12063
Current error: 9.73779949363e-06

Current iteration: 12064
Current error: 9.71278701049e-06

Current iteration: 12065
Current error: 9.68728134709e-06

Current iteration: 12066
Current error: 9.6613030687e-06

Current iteration: 12067
Current error: 9.63604535004e-06

Current iteration: 12068
Current error: 9.61090170663e-06

Current iteration: 12069
Current error: 9.60909846903e-06

Current iteration: 12070
Current error: 9.55946921e-06

Current iteration: 12071
Current error: 9.53565763245e-06

Current iteration: 12072
Current error: 9.51341640675e-06

Current iteration: 12073
Current error: 9.48802848726e-06

Current iteration: 12074
Current error: 0.040350514848

Current iteration: 12075
Current error: 8.3931534964e-06

Current iteration: 12076
Current error: 8.37350554638e-06

Current iteration: 12077
Current error: 8.3526614148e-06

Current iteration: 12078
Current error: 8.33494173093e-06

Current iteration: 12079
Current error: 0.000163285660526

Current iteration: 12080
Current error: 8.66843423453e-06

Current iteration: 12081
Current error: 1.0481042115e-05

Current iteration: 12082
Current error: 8.1881026929e-06

Current iteration: 12083
Current error: 8.17257888657e-06

Current iteration: 12084
Current error: 8.15056737714e-06

Current iteration: 12085
Current error: 1.66374072703e-05

Current iteration: 12086
Current error: 8.10168003873e-06

Current iteration: 12087
Current error: 8.88326680249e-06

Current iteration: 12088
Current error: 8.06159996856e-06

Current iteration: 12089
Current error: 8.04308546107e-06

Current iteration: 12090
Current error: 8.03358953349e-06

Current iteration: 12091
Current error: 8.06500488747e-06

Current iteration: 12092
Current error: 7.99566058139e-06

Current iteration: 12093
Current error: 7.96895828616e-06

Current iteration: 12094
Current error: 7.97656920511e-06

Current iteration: 12095
Current error: 7.93068521503e-06

Current iteration: 12096
Current error: 7.90970531823e-06

Current iteration: 12097
Current error: 7.89323660944e-06

Current iteration: 12098
Current error: 0.190404066844

Current iteration: 12099
Current error: 1.00386180938e-05

Current iteration: 12100
Current error: 3.83356286309e-05

Current iteration: 12101
Current error: 0.138344693528

Current iteration: 12102
Current error: 1.21307669683e-05

Current iteration: 12103
Current error: 0.0693446308832

Current iteration: 12104
Current error: 1.04017008721e-05

Current iteration: 12105
Current error: 1.03747767405e-05

Current iteration: 12106
Current error: 0.00222300935884

Current iteration: 12107
Current error: 0.0231511836815

Current iteration: 12108
Current error: 9.10200614911e-06

Current iteration: 12109
Current error: 9.08725556608e-06

Current iteration: 12110
Current error: 9.055133771e-06

Current iteration: 12111
Current error: 9.03167414723e-06

Current iteration: 12112
Current error: 9.00942262197e-06

Current iteration: 12113
Current error: 9.20811557461e-06

Current iteration: 12114
Current error: 0.324395229474

Current iteration: 12115
Current error: 1.29994166292e-05

Current iteration: 12116
Current error: 0.111281966729

Current iteration: 12117
Current error: 1.51213324894e-05

Current iteration: 12118
Current error: 1.54218388982e-05

Current iteration: 12119
Current error: 1.51484611458e-05

Current iteration: 12120
Current error: 1.52265913035e-05

Current iteration: 12121
Current error: 1.49316647918e-05

Current iteration: 12122
Current error: 1.4878862221e-05

Current iteration: 12123
Current error: 1.48428948e-05

Current iteration: 12124
Current error: 1.48080600008e-05

Current iteration: 12125
Current error: 1.47720307442e-05

Current iteration: 12126
Current error: 1.46869500453e-05

Current iteration: 12127
Current error: 1.46369047493e-05

Current iteration: 12128
Current error: 1.458778054e-05

Current iteration: 12129
Current error: 0.104010110707

Current iteration: 12130
Current error: 2.0833930867e-05

Current iteration: 12131
Current error: 1.70764991053e-05

Current iteration: 12132
Current error: 1.70166551693e-05

Current iteration: 12133
Current error: 0.102503669498

Current iteration: 12134
Current error: 0.012950885218

Current iteration: 12135
Current error: 1.85599874173e-05

Current iteration: 12136
Current error: 0.00437373093628

Current iteration: 12137
Current error: 1.76511207609e-05

Current iteration: 12138
Current error: 1.7588302253e-05

Current iteration: 12139
Current error: 1.75330837255e-05

Current iteration: 12140
Current error: 1.74626786957e-05

Current iteration: 12141
Current error: 1.74280926506e-05

Current iteration: 12142
Current error: 1.73405112174e-05

Current iteration: 12143
Current error: 0.0446730100596

Current iteration: 12144
Current error: 1.51994678359e-05

Current iteration: 12145
Current error: 1.51488948277e-05

Current iteration: 12146
Current error: 1.5121730206e-05

Current iteration: 12147
Current error: 1.50501820632e-05

Current iteration: 12148
Current error: 2.02505841435e-05

Current iteration: 12149
Current error: 1.49444907078e-05

Current iteration: 12150
Current error: 1.48968429502e-05

Current iteration: 12151
Current error: 1.48474310751e-05

Current iteration: 12152
Current error: 1.48084520002e-05

Current iteration: 12153
Current error: 1.47622612214e-05

Current iteration: 12154
Current error: 1.47308832665e-05

Current iteration: 12155
Current error: 1.4656054805e-05

Current iteration: 12156
Current error: 0.102629361764

Current iteration: 12157
Current error: 1.71479732136e-05

Current iteration: 12158
Current error: 0.00175472333334

Current iteration: 12159
Current error: 1.66635724874e-05

Current iteration: 12160
Current error: 1.7562321474e-05

Current iteration: 12161
Current error: 1.64621326974e-05

Current iteration: 12162
Current error: 1.64088657265e-05

Current iteration: 12163
Current error: 1.63508296955e-05

Current iteration: 12164
Current error: 1.63052546964e-05

Current iteration: 12165
Current error: 0.219588785135

Current iteration: 12166
Current error: 2.1530810099e-05

Current iteration: 12167
Current error: 2.13700806473e-05

Current iteration: 12168
Current error: 2.12908549159e-05

Current iteration: 12169
Current error: 2.14161144961e-05

Current iteration: 12170
Current error: 2.12873861896e-05

Current iteration: 12171
Current error: 2.10472190078e-05

Current iteration: 12172
Current error: 2.09630096303e-05

Current iteration: 12173
Current error: 2.09069340639e-05

Current iteration: 12174
Current error: 2.08071747119e-05

Current iteration: 12175
Current error: 2.07218251686e-05

Current iteration: 12176
Current error: 0.0020606696935

Current iteration: 12177
Current error: 1.99745037681e-05

Current iteration: 12178
Current error: 1.98954207327e-05

Current iteration: 12179
Current error: 1.9821458331e-05

Current iteration: 12180
Current error: 1.97938600193e-05

Current iteration: 12181
Current error: 1.97062230062e-05

Current iteration: 12182
Current error: 1.96011864399e-05

Current iteration: 12183
Current error: 1.95274468354e-05

Current iteration: 12184
Current error: 1.9453606028e-05

Current iteration: 12185
Current error: 1.93806652833e-05

Current iteration: 12186
Current error: 1.93217262958e-05

Current iteration: 12187
Current error: 1.92409755612e-05

Current iteration: 12188
Current error: 1.91697234803e-05

Current iteration: 12189
Current error: 1.90982202755e-05

Current iteration: 12190
Current error: 1.92282100164e-05

Current iteration: 12191
Current error: 0.0824908863313

Current iteration: 12192
Current error: 2.18004859577e-05

Current iteration: 12193
Current error: 2.17244806865e-05

Current iteration: 12194
Current error: 0.075117548043

Current iteration: 12195
Current error: 2.57303856468e-05

Current iteration: 12196
Current error: 2.45797484861e-05

Current iteration: 12197
Current error: 2.44791844422e-05

Current iteration: 12198
Current error: 2.43784373305e-05

Current iteration: 12199
Current error: 0.0769334848636

Current iteration: 12200
Current error: 2.79357264714e-05

Current iteration: 12201
Current error: 3.45826617669e-05

Current iteration: 12202
Current error: 3.0271791436e-05

Current iteration: 12203
Current error: 2.76183786534e-05

Current iteration: 12204
Current error: 2.74026255091e-05

Current iteration: 12205
Current error: 2.72791088013e-05

Current iteration: 12206
Current error: 2.73013347322e-05

Current iteration: 12207
Current error: 2.70422864502e-05

Current iteration: 12208
Current error: 2.69230257619e-05

Current iteration: 12209
Current error: 2.6867140831e-05

Current iteration: 12210
Current error: 2.6692015409e-05

Current iteration: 12211
Current error: 4.55202376634e-05

Current iteration: 12212
Current error: 2.64238963577e-05

Current iteration: 12213
Current error: 2.65912877066e-05

Current iteration: 12214
Current error: 0.112433433313

Current iteration: 12215
Current error: 0.00664534704957

Current iteration: 12216
Current error: 2.0512315864e-05

Current iteration: 12217
Current error: 2.0460270661e-05

Current iteration: 12218
Current error: 2.05169357132e-05

Current iteration: 12219
Current error: 2.02965646918e-05

Current iteration: 12220
Current error: 2.0229582291e-05

Current iteration: 12221
Current error: 2.03903596661e-05

Current iteration: 12222
Current error: 2.00930581352e-05

Current iteration: 12223
Current error: 1.99725833626e-05

Current iteration: 12224
Current error: 2.11299040098e-05

Current iteration: 12225
Current error: 1.98373523707e-05

Current iteration: 12226
Current error: 0.0763602087204

Current iteration: 12227
Current error: 2.256595073e-05

Current iteration: 12228
Current error: 2.24774482276e-05

Current iteration: 12229
Current error: 2.23892773739e-05

Current iteration: 12230
Current error: 0.113608801939

Current iteration: 12231
Current error: 1.91418170084e-05

Current iteration: 12232
Current error: 6.10012147776e-05

Current iteration: 12233
Current error: 0.0119840389202

Current iteration: 12234
Current error: 1.70322004451e-05

Current iteration: 12235
Current error: 1.69463976553e-05

Current iteration: 12236
Current error: 1.68857193013e-05

Current iteration: 12237
Current error: 1.68295824308e-05

Current iteration: 12238
Current error: 1.67703098662e-05

Current iteration: 12239
Current error: 1.67150059447e-05

Current iteration: 12240
Current error: 1.66556419469e-05

Current iteration: 12241
Current error: 1.65989502775e-05

Current iteration: 12242
Current error: 1.65406605322e-05

Current iteration: 12243
Current error: 1.64830805835e-05

Current iteration: 12244
Current error: 1.64281782795e-05

Current iteration: 12245
Current error: 1.63709356518e-05

Current iteration: 12246
Current error: 1.631652597e-05

Current iteration: 12247
Current error: 0.0853804006029

Current iteration: 12248
Current error: 1.87856737902e-05

Current iteration: 12249
Current error: 1.87157739515e-05

Current iteration: 12250
Current error: 1.88005825123e-05

Current iteration: 12251
Current error: 0.082683354453

Current iteration: 12252
Current error: 1.59719908604e-05

Current iteration: 12253
Current error: 9.45596455735e-05

Current iteration: 12254
Current error: 1.55957271614e-05

Current iteration: 12255
Current error: 1.55134468029e-05

Current iteration: 12256
Current error: 1.54628356064e-05

Current iteration: 12257
Current error: 1.54218258838e-05

Current iteration: 12258
Current error: 1.53596266828e-05

Current iteration: 12259
Current error: 1.54879908517e-05

Current iteration: 12260
Current error: 1.90633144591e-05

Current iteration: 12261
Current error: 1.52035359979e-05

Current iteration: 12262
Current error: 1.51537904596e-05

Current iteration: 12263
Current error: 1.51039506476e-05

Current iteration: 12264
Current error: 1.50654798331e-05

Current iteration: 12265
Current error: 1.50031209173e-05

Current iteration: 12266
Current error: 1.49561716309e-05

Current iteration: 12267
Current error: 1.49215952522e-05

Current iteration: 12268
Current error: 1.48602494286e-05

Current iteration: 12269
Current error: 1.48147374996e-05

Current iteration: 12270
Current error: 1.69825107461e-05

Current iteration: 12271
Current error: 1.47344838844e-05

Current iteration: 12272
Current error: 1.46621331256e-05

Current iteration: 12273
Current error: 1.46169565154e-05

Current iteration: 12274
Current error: 0.08693967278

Current iteration: 12275
Current error: 1.23798313435e-05

Current iteration: 12276
Current error: 0.0304419922622

Current iteration: 12277
Current error: 1.10175852656e-05

Current iteration: 12278
Current error: 0.00012640966972

Current iteration: 12279
Current error: 1.08922719011e-05

Current iteration: 12280
Current error: 1.08618867575e-05

Current iteration: 12281
Current error: 1.08315281482e-05

Current iteration: 12282
Current error: 1.08027928767e-05

Current iteration: 12283
Current error: 1.07713446035e-05

Current iteration: 12284
Current error: 1.07410894539e-05

Current iteration: 12285
Current error: 1.12503148823e-05

Current iteration: 12286
Current error: 1.06827475743e-05

Current iteration: 12287
Current error: 1.06525683585e-05

Current iteration: 12288
Current error: 1.06226624279e-05

Current iteration: 12289
Current error: 1.05939458782e-05

Current iteration: 12290
Current error: 1.05644041468e-05

Current iteration: 12291
Current error: 1.05392212729e-05

Current iteration: 12292
Current error: 1.05070693129e-05

Current iteration: 12293
Current error: 0.104290740574

Current iteration: 12294
Current error: 0.0168205124042

Current iteration: 12295
Current error: 1.13329653165e-05

Current iteration: 12296
Current error: 1.12998744861e-05

Current iteration: 12297
Current error: 1.33483484611e-05

Current iteration: 12298
Current error: 1.12335259691e-05

Current iteration: 12299
Current error: 1.12017818174e-05

Current iteration: 12300
Current error: 2.32541975867e-05

Current iteration: 12301
Current error: 1.11515003967e-05

Current iteration: 12302
Current error: 1.10952886259e-05

Current iteration: 12303
Current error: 1.13613682559e-05

Current iteration: 12304
Current error: 1.10328570519e-05

Current iteration: 12305
Current error: 1.10017016106e-05

Current iteration: 12306
Current error: 1.09777945302e-05

Current iteration: 12307
Current error: 1.09388942713e-05

Current iteration: 12308
Current error: 1.09124402168e-05

Current iteration: 12309
Current error: 0.103625109272

Current iteration: 12310
Current error: 0.11362046173

Current iteration: 12311
Current error: 1.06685310432e-05

Current iteration: 12312
Current error: 1.06372671658e-05

Current iteration: 12313
Current error: 1.06084846988e-05

Current iteration: 12314
Current error: 1.05789358388e-05

Current iteration: 12315
Current error: 1.05620066488e-05

Current iteration: 12316
Current error: 1.05214743487e-05

Current iteration: 12317
Current error: 1.04924750892e-05

Current iteration: 12318
Current error: 1.046404142e-05

Current iteration: 12319
Current error: 1.0434896775e-05

Current iteration: 12320
Current error: 0.100483143706

Current iteration: 12321
Current error: 1.28123488839e-05

Current iteration: 12322
Current error: 1.21505628861e-05

Current iteration: 12323
Current error: 1.211164839e-05

Current iteration: 12324
Current error: 1.20824245857e-05

Current iteration: 12325
Current error: 1.20411867655e-05

Current iteration: 12326
Current error: 1.20635974062e-05

Current iteration: 12327
Current error: 1.19696121624e-05

Current iteration: 12328
Current error: 1.38477567051e-05

Current iteration: 12329
Current error: 1.19013733445e-05

Current iteration: 12330
Current error: 1.18641282338e-05

Current iteration: 12331
Current error: 1.18253592999e-05

Current iteration: 12332
Current error: 1.17956725205e-05

Current iteration: 12333
Current error: 1.17614710656e-05

Current iteration: 12334
Current error: 0.00071537853551

Current iteration: 12335
Current error: 1.14991339583e-05

Current iteration: 12336
Current error: 1.14631231036e-05

Current iteration: 12337
Current error: 0.100482988194

Current iteration: 12338
Current error: 9.59021561815e-06

Current iteration: 12339
Current error: 3.0157657601e-05

Current iteration: 12340
Current error: 9.5227363504e-06

Current iteration: 12341
Current error: 9.49730605528e-06

Current iteration: 12342
Current error: 9.47308094345e-06

Current iteration: 12343
Current error: 9.44809190013e-06

Current iteration: 12344
Current error: 9.42558851176e-06

Current iteration: 12345
Current error: 0.103955071611

Current iteration: 12346
Current error: 1.10312466211e-05

Current iteration: 12347
Current error: 1.25340118124e-05

Current iteration: 12348
Current error: 1.09683525875e-05

Current iteration: 12349
Current error: 1.69335093636e-05

Current iteration: 12350
Current error: 1.08991343258e-05

Current iteration: 12351
Current error: 1.08698380606e-05

Current iteration: 12352
Current error: 5.67357075395e-05

Current iteration: 12353
Current error: 0.22015116258

Current iteration: 12354
Current error: 1.41868044886e-05

Current iteration: 12355
Current error: 1.41911372046e-05

Current iteration: 12356
Current error: 1.40972144475e-05

Current iteration: 12357
Current error: 1.40521739816e-05

Current iteration: 12358
Current error: 3.71415477867e-05

Current iteration: 12359
Current error: 1.4951639347e-05

Current iteration: 12360
Current error: 1.38960119606e-05

Current iteration: 12361
Current error: 1.3847988151e-05

Current iteration: 12362
Current error: 1.38061125371e-05

Current iteration: 12363
Current error: 1.40167601876e-05

Current iteration: 12364
Current error: 1.37170746266e-05

Current iteration: 12365
Current error: 1.36770878543e-05

Current iteration: 12366
Current error: 1.36330961905e-05

Current iteration: 12367
Current error: 1.35897082955e-05

Current iteration: 12368
Current error: 1.73875918291e-05

Current iteration: 12369
Current error: 2.02894886548e-05

Current iteration: 12370
Current error: 1.34498972963e-05

Current iteration: 12371
Current error: 2.26936966748e-05

Current iteration: 12372
Current error: 1.33555414159e-05

Current iteration: 12373
Current error: 1.3321665801e-05

Current iteration: 12374
Current error: 0.00372506853069

Current iteration: 12375
Current error: 1.27161040801e-05

Current iteration: 12376
Current error: 1.26786731792e-05

Current iteration: 12377
Current error: 1.26377446044e-05

Current iteration: 12378
Current error: 1.26011035976e-05

Current iteration: 12379
Current error: 0.000502275532655

Current iteration: 12380
Current error: 2.15790577939e-05

Current iteration: 12381
Current error: 1.26883415524e-05

Current iteration: 12382
Current error: 1.22690468233e-05

Current iteration: 12383
Current error: 1.22314091514e-05

Current iteration: 12384
Current error: 1.21980692446e-05

Current iteration: 12385
Current error: 1.21619324262e-05

Current iteration: 12386
Current error: 1.21261279546e-05

Current iteration: 12387
Current error: 1.20932728698e-05

Current iteration: 12388
Current error: 1.20539919281e-05

Current iteration: 12389
Current error: 1.20313816792e-05

Current iteration: 12390
Current error: 1.1984191957e-05

Current iteration: 12391
Current error: 1.19742190853e-05

Current iteration: 12392
Current error: 1.27259645109e-05

Current iteration: 12393
Current error: 1.18778859069e-05

Current iteration: 12394
Current error: 1.18438797106e-05

Current iteration: 12395
Current error: 1.18246608833e-05

Current iteration: 12396
Current error: 1.17759960897e-05

Current iteration: 12397
Current error: 0.0975118554228

Current iteration: 12398
Current error: 9.88680030972e-06

Current iteration: 12399
Current error: 9.83767334003e-06

Current iteration: 12400
Current error: 9.82684917744e-06

Current iteration: 12401
Current error: 9.78488097921e-06

Current iteration: 12402
Current error: 9.75333797856e-06

Current iteration: 12403
Current error: 0.207722912153

Current iteration: 12404
Current error: 1.26737783957e-05

Current iteration: 12405
Current error: 1.26361324057e-05

Current iteration: 12406
Current error: 1.25974502135e-05

Current iteration: 12407
Current error: 5.77939609703e-05

Current iteration: 12408
Current error: 0.0327522129476

Current iteration: 12409
Current error: 1.12104071259e-05

Current iteration: 12410
Current error: 1.1126445913e-05

Current iteration: 12411
Current error: 1.1094077568e-05

Current iteration: 12412
Current error: 1.1063772247e-05

Current iteration: 12413
Current error: 0.0820778416663

Current iteration: 12414
Current error: 9.7391704252e-06

Current iteration: 12415
Current error: 9.34644040391e-06

Current iteration: 12416
Current error: 9.32530392555e-06

Current iteration: 12417
Current error: 9.31877110389e-06

Current iteration: 12418
Current error: 9.27475122738e-06

Current iteration: 12419
Current error: 0.00126398947155

Current iteration: 12420
Current error: 9.01967240249e-06

Current iteration: 12421
Current error: 8.99196139e-06

Current iteration: 12422
Current error: 8.9693239487e-06

Current iteration: 12423
Current error: 1.35879072709e-05

Current iteration: 12424
Current error: 9.04892376582e-06

Current iteration: 12425
Current error: 8.89680235605e-06

Current iteration: 12426
Current error: 8.87480992892e-06

Current iteration: 12427
Current error: 8.85078199554e-06

Current iteration: 12428
Current error: 8.82953183404e-06

Current iteration: 12429
Current error: 8.80635582511e-06

Current iteration: 12430
Current error: 8.78939956257e-06

Current iteration: 12431
Current error: 8.76326463809e-06

Current iteration: 12432
Current error: 8.74182410404e-06

Current iteration: 12433
Current error: 8.71955765071e-06

Current iteration: 12434
Current error: 9.80806190213e-06

Current iteration: 12435
Current error: 8.85773618776e-06

Current iteration: 12436
Current error: 8.65192300097e-06

Current iteration: 12437
Current error: 8.39978013711e-05

Current iteration: 12438
Current error: 8.56894736584e-06

Current iteration: 12439
Current error: 8.56791930169e-06

Current iteration: 12440
Current error: 8.52816787653e-06

Current iteration: 12441
Current error: 8.52828400545e-06

Current iteration: 12442
Current error: 8.4850996918e-06

Current iteration: 12443
Current error: 0.00853951717656

Current iteration: 12444
Current error: 7.95666822486e-06

Current iteration: 12445
Current error: 7.93546635812e-06

Current iteration: 12446
Current error: 7.9186998491e-06

Current iteration: 12447
Current error: 7.89949826505e-06

Current iteration: 12448
Current error: 7.88481337025e-06

Current iteration: 12449
Current error: 7.86179542141e-06

Current iteration: 12450
Current error: 7.97362175923e-06

Current iteration: 12451
Current error: 0.0605669571246

Current iteration: 12452
Current error: 6.78390937625e-06

Current iteration: 12453
Current error: 0.0593128792042

Current iteration: 12454
Current error: 5.91860520521e-06

Current iteration: 12455
Current error: 5.867188895e-06

Current iteration: 12456
Current error: 5.85588166669e-06

Current iteration: 12457
Current error: 5.85078310629e-06

Current iteration: 12458
Current error: 5.83085046529e-06

Current iteration: 12459
Current error: 5.85674836508e-06

Current iteration: 12460
Current error: 5.84618624875e-06

Current iteration: 12461
Current error: 6.31382966608e-06

Current iteration: 12462
Current error: 5.78479070861e-06

Current iteration: 12463
Current error: 0.00309546037905

Current iteration: 12464
Current error: 5.5673891617e-06

Current iteration: 12465
Current error: 5.5440434371e-06

Current iteration: 12466
Current error: 6.17954091845e-06

Current iteration: 12467
Current error: 5.52126772154e-06

Current iteration: 12468
Current error: 5.51530361896e-06

Current iteration: 12469
Current error: 5.49821504743e-06

Current iteration: 12470
Current error: 5.4876646935e-06

Current iteration: 12471
Current error: 5.47680397592e-06

Current iteration: 12472
Current error: 5.4679918429e-06

Current iteration: 12473
Current error: 5.45691599324e-06

Current iteration: 12474
Current error: 8.63541844758e-05

Current iteration: 12475
Current error: 0.140717003017

Current iteration: 12476
Current error: 6.57986856689e-06

Current iteration: 12477
Current error: 6.56436957214e-06

Current iteration: 12478
Current error: 6.54933351345e-06

Current iteration: 12479
Current error: 0.00910708818965

Current iteration: 12480
Current error: 6.13821787542e-06

Current iteration: 12481
Current error: 7.38263406852e-06

Current iteration: 12482
Current error: 6.12440610821e-06

Current iteration: 12483
Current error: 1.64364913054e-05

Current iteration: 12484
Current error: 0.0096168977431

Current iteration: 12485
Current error: 5.70054843255e-06

Current iteration: 12486
Current error: 5.68936210723e-06

Current iteration: 12487
Current error: 5.67895331229e-06

Current iteration: 12488
Current error: 5.66795462896e-06

Current iteration: 12489
Current error: 5.65486253891e-06

Current iteration: 12490
Current error: 5.6440680743e-06

Current iteration: 12491
Current error: 5.63244540184e-06

Current iteration: 12492
Current error: 5.62121580259e-06

Current iteration: 12493
Current error: 0.0129727443628

Current iteration: 12494
Current error: 5.21468471786e-06

Current iteration: 12495
Current error: 5.20510415958e-06

Current iteration: 12496
Current error: 5.19676830686e-06

Current iteration: 12497
Current error: 8.45925698769e-05

Current iteration: 12498
Current error: 5.14783905416e-06

Current iteration: 12499
Current error: 7.7012812685e-06

Current iteration: 12500
Current error: 5.13038819409e-06

Current iteration: 12501
Current error: 5.12102163645e-06

Current iteration: 12502
Current error: 5.10794981756e-06

Current iteration: 12503
Current error: 5.09699712547e-06

Current iteration: 12504
Current error: 5.11393563223e-06

Current iteration: 12505
Current error: 5.07709075009e-06

Current iteration: 12506
Current error: 0.235802360854

Current iteration: 12507
Current error: 6.71438622241e-06

Current iteration: 12508
Current error: 6.69910277953e-06

Current iteration: 12509
Current error: 6.68465214723e-06

Current iteration: 12510
Current error: 6.67100065642e-06

Current iteration: 12511
Current error: 6.65678918984e-06

Current iteration: 12512
Current error: 0.0402586904175

Current iteration: 12513
Current error: 5.88810055521e-06

Current iteration: 12514
Current error: 6.43913397365e-06

Current iteration: 12515
Current error: 5.86314017236e-06

Current iteration: 12516
Current error: 5.85082030499e-06

Current iteration: 12517
Current error: 0.137359830447

Current iteration: 12518
Current error: 7.09444726683e-06

Current iteration: 12519
Current error: 7.07801931342e-06

Current iteration: 12520
Current error: 7.06308292811e-06

Current iteration: 12521
Current error: 7.0452262711e-06

Current iteration: 12522
Current error: 7.03031170063e-06

Current iteration: 12523
Current error: 7.11526716123e-06

Current iteration: 12524
Current error: 0.000752898045783

Current iteration: 12525
Current error: 6.86048054932e-06

Current iteration: 12526
Current error: 6.84512760271e-06

Current iteration: 12527
Current error: 6.82997903676e-06

Current iteration: 12528
Current error: 6.81474412571e-06

Current iteration: 12529
Current error: 6.80610623206e-06

Current iteration: 12530
Current error: 6.78461501398e-06

Current iteration: 12531
Current error: 1.73873622422e-05

Current iteration: 12532
Current error: 6.74644342592e-06

Current iteration: 12533
Current error: 6.73217778845e-06

Current iteration: 12534
Current error: 6.71741608283e-06

Current iteration: 12535
Current error: 7.60485096156e-06

Current iteration: 12536
Current error: 6.68758704724e-06

Current iteration: 12537
Current error: 6.67408106716e-06

Current iteration: 12538
Current error: 6.79589687939e-06

Current iteration: 12539
Current error: 6.78031305595e-06

Current iteration: 12540
Current error: 6.64228539414e-06

Current iteration: 12541
Current error: 6.61475967133e-06

Current iteration: 12542
Current error: 6.60014221396e-06

Current iteration: 12543
Current error: 6.58543479798e-06

Current iteration: 12544
Current error: 6.57150433257e-06

Current iteration: 12545
Current error: 0.115630617447

Current iteration: 12546
Current error: 1.0922345006e-05

Current iteration: 12547
Current error: 7.78229092135e-06

Current iteration: 12548
Current error: 7.76360580957e-06

Current iteration: 12549
Current error: 8.79242160018e-06

Current iteration: 12550
Current error: 0.221500223833

Current iteration: 12551
Current error: 0.0348782069165

Current iteration: 12552
Current error: 3.10307144187e-05

Current iteration: 12553
Current error: 9.03963653591e-06

Current iteration: 12554
Current error: 9.01746478026e-06

Current iteration: 12555
Current error: 8.99558828699e-06

Current iteration: 12556
Current error: 8.97216171773e-06

Current iteration: 12557
Current error: 8.94943425319e-06

Current iteration: 12558
Current error: 0.100111843625

Current iteration: 12559
Current error: 1.04878514814e-05

Current iteration: 12560
Current error: 0.000821306609854

Current iteration: 12561
Current error: 1.02436373979e-05

Current iteration: 12562
Current error: 0.0680080107376

Current iteration: 12563
Current error: 8.77795749244e-06

Current iteration: 12564
Current error: 8.81539238484e-06

Current iteration: 12565
Current error: 8.86065923421e-06

Current iteration: 12566
Current error: 8.75513443132e-06

Current iteration: 12567
Current error: 8.99773979198e-06

Current iteration: 12568
Current error: 8.6668254085e-06

Current iteration: 12569
Current error: 9.82134154547e-06

Current iteration: 12570
Current error: 0.0116555378818

Current iteration: 12571
Current error: 8.03133922552e-06

Current iteration: 12572
Current error: 0.102064976281

Current iteration: 12573
Current error: 6.71659886127e-06

Current iteration: 12574
Current error: 6.70256112664e-06

Current iteration: 12575
Current error: 6.68707887829e-06

Current iteration: 12576
Current error: 6.67423116223e-06

Current iteration: 12577
Current error: 6.67994289192e-06

Current iteration: 12578
Current error: 6.64402793462e-06

Current iteration: 12579
Current error: 6.62970221542e-06

Current iteration: 12580
Current error: 6.6673062451e-06

Current iteration: 12581
Current error: 0.00129839979577

Current iteration: 12582
Current error: 6.43126771169e-06

Current iteration: 12583
Current error: 7.3411850706e-06

Current iteration: 12584
Current error: 6.40317142573e-06

Current iteration: 12585
Current error: 1.11320991272e-05

Current iteration: 12586
Current error: 6.41005115357e-06

Current iteration: 12587
Current error: 6.35826542564e-06

Current iteration: 12588
Current error: 6.3441236946e-06

Current iteration: 12589
Current error: 0.121011449513

Current iteration: 12590
Current error: 0.112675543257

Current iteration: 12591
Current error: 0.0906309953541

Current iteration: 12592
Current error: 7.58416547011e-06

Current iteration: 12593
Current error: 7.6096863192e-06

Current iteration: 12594
Current error: 7.57486808095e-06

Current iteration: 12595
Current error: 7.53067313829e-06

Current iteration: 12596
Current error: 7.55059321615e-06

Current iteration: 12597
Current error: 7.4966176144e-06

Current iteration: 12598
Current error: 7.48309493173e-06

Current iteration: 12599
Current error: 7.46029821523e-06

Current iteration: 12600
Current error: 0.14939212398

Current iteration: 12601
Current error: 9.19848071615e-06

Current iteration: 12602
Current error: 0.164346836512

Current iteration: 12603
Current error: 1.15104739367e-05

Current iteration: 12604
Current error: 1.14804217471e-05

Current iteration: 12605
Current error: 1.1444151547e-05

Current iteration: 12606
Current error: 0.0973233743046

Current iteration: 12607
Current error: 1.34249210875e-05

Current iteration: 12608
Current error: 1.35629633544e-05

Current iteration: 12609
Current error: 0.111178205828

Current iteration: 12610
Current error: 1.10826916652e-05

Current iteration: 12611
Current error: 1.10528680966e-05

Current iteration: 12612
Current error: 1.1025192116e-05

Current iteration: 12613
Current error: 1.09905085741e-05

Current iteration: 12614
Current error: 1.09634352607e-05

Current iteration: 12615
Current error: 1.0929743068e-05

Current iteration: 12616
Current error: 1.09011538525e-05

Current iteration: 12617
Current error: 1.08763618879e-05

Current iteration: 12618
Current error: 1.0836833647e-05

Current iteration: 12619
Current error: 1.08058927738e-05

Current iteration: 12620
Current error: 1.07785028972e-05

Current iteration: 12621
Current error: 1.07899213634e-05

Current iteration: 12622
Current error: 1.07230494739e-05

Current iteration: 12623
Current error: 1.06883406704e-05

Current iteration: 12624
Current error: 1.06596296769e-05

Current iteration: 12625
Current error: 1.0630209496e-05

Current iteration: 12626
Current error: 1.06021032133e-05

Current iteration: 12627
Current error: 1.05793232801e-05

Current iteration: 12628
Current error: 1.66692766053e-05

Current iteration: 12629
Current error: 1.05066949375e-05

Current iteration: 12630
Current error: 1.04782565456e-05

Current iteration: 12631
Current error: 0.00841408111233

Current iteration: 12632
Current error: 0.01674973178

Current iteration: 12633
Current error: 9.03127291371e-06

Current iteration: 12634
Current error: 9.04135047585e-06

Current iteration: 12635
Current error: 0.0907015593605

Current iteration: 12636
Current error: 1.04486610769e-05

Current iteration: 12637
Current error: 1.04270583562e-05

Current iteration: 12638
Current error: 0.144915463161

Current iteration: 12639
Current error: 8.51953367183e-06

Current iteration: 12640
Current error: 8.48420721863e-06

Current iteration: 12641
Current error: 8.46385699695e-06

Current iteration: 12642
Current error: 8.4439671742e-06

Current iteration: 12643
Current error: 8.4210750443e-06

Current iteration: 12644
Current error: 8.40097401322e-06

Current iteration: 12645
Current error: 8.38437931249e-06

Current iteration: 12646
Current error: 0.116686472416

Current iteration: 12647
Current error: 0.118087067644

Current iteration: 12648
Current error: 8.83179022954e-06

Current iteration: 12649
Current error: 8.27891374062e-06

Current iteration: 12650
Current error: 8.27212327177e-06

Current iteration: 12651
Current error: 0.0963889266139

Current iteration: 12652
Current error: 9.61454351853e-06

Current iteration: 12653
Current error: 1.09162965952e-05

Current iteration: 12654
Current error: 0.0874077304329

Current iteration: 12655
Current error: 1.10887559215e-05

Current iteration: 12656
Current error: 0.0291714187552

Current iteration: 12657
Current error: 0.0380510822542

Current iteration: 12658
Current error: 8.807329708e-06

Current iteration: 12659
Current error: 8.78582728166e-06

Current iteration: 12660
Current error: 8.77083905045e-06

Current iteration: 12661
Current error: 8.74751774764e-06

Current iteration: 12662
Current error: 0.0941119121712

Current iteration: 12663
Current error: 7.33960580851e-06

Current iteration: 12664
Current error: 7.32241142569e-06

Current iteration: 12665
Current error: 0.00527634234505

Current iteration: 12666
Current error: 0.025819801773

Current iteration: 12667
Current error: 6.28960374908e-06

Current iteration: 12668
Current error: 6.27755341877e-06

Current iteration: 12669
Current error: 6.26672245418e-06

Current iteration: 12670
Current error: 6.25004578334e-06

Current iteration: 12671
Current error: 6.2475673398e-06

Current iteration: 12672
Current error: 0.0348485942038

Current iteration: 12673
Current error: 5.59077326381e-06

Current iteration: 12674
Current error: 5.54434627923e-06

Current iteration: 12675
Current error: 5.53388955596e-06

Current iteration: 12676
Current error: 5.5224877861e-06

Current iteration: 12677
Current error: 5.51149490447e-06

Current iteration: 12678
Current error: 5.49909491213e-06

Current iteration: 12679
Current error: 5.48912709314e-06

Current iteration: 12680
Current error: 5.47875422618e-06

Current iteration: 12681
Current error: 5.46769694483e-06

Current iteration: 12682
Current error: 5.45656162052e-06

Current iteration: 12683
Current error: 2.08687246429e-05

Current iteration: 12684
Current error: 0.0521906703992

Current iteration: 12685
Current error: 0.121482185096

Current iteration: 12686
Current error: 5.67186755589e-06

Current iteration: 12687
Current error: 5.65383965922e-06

Current iteration: 12688
Current error: 5.64277387308e-06

Current iteration: 12689
Current error: 5.63321235226e-06

Current iteration: 12690
Current error: 5.62150803432e-06

Current iteration: 12691
Current error: 5.60886071506e-06

Current iteration: 12692
Current error: 5.59778197342e-06

Current iteration: 12693
Current error: 0.34460277596

Current iteration: 12694
Current error: 8.2199867272e-06

Current iteration: 12695
Current error: 8.13234235066e-06

Current iteration: 12696
Current error: 8.11453332759e-06

Current iteration: 12697
Current error: 8.09432211426e-06

Current iteration: 12698
Current error: 8.07577764417e-06

Current iteration: 12699
Current error: 0.0989582832269

Current iteration: 12700
Current error: 9.77742020901e-06

Current iteration: 12701
Current error: 9.42106243e-06

Current iteration: 12702
Current error: 0.0890778426462

Current iteration: 12703
Current error: 7.93053743041e-06

Current iteration: 12704
Current error: 7.98089908638e-06

Current iteration: 12705
Current error: 7.88309836413e-06

Current iteration: 12706
Current error: 0.000172853053008

Current iteration: 12707
Current error: 0.000157457397136

Current iteration: 12708
Current error: 7.76536280551e-06

Current iteration: 12709
Current error: 7.69347607924e-06

Current iteration: 12710
Current error: 7.67309329161e-06

Current iteration: 12711
Current error: 0.000269176133908

Current iteration: 12712
Current error: 7.560959159e-06

Current iteration: 12713
Current error: 7.56932245119e-06

Current iteration: 12714
Current error: 7.52706348734e-06

Current iteration: 12715
Current error: 7.52003341088e-06

Current iteration: 12716
Current error: 0.0210642137547

Current iteration: 12717
Current error: 6.83737850101e-06

Current iteration: 12718
Current error: 6.81790082023e-06

Current iteration: 12719
Current error: 6.80261273665e-06

Current iteration: 12720
Current error: 6.78749226021e-06

Current iteration: 12721
Current error: 6.78706783539e-06

Current iteration: 12722
Current error: 0.024192912964

Current iteration: 12723
Current error: 6.12891047948e-06

Current iteration: 12724
Current error: 6.11861377056e-06

Current iteration: 12725
Current error: 6.10375915136e-06

Current iteration: 12726
Current error: 8.5064866509e-06

Current iteration: 12727
Current error: 6.07611333609e-06

Current iteration: 12728
Current error: 6.06328992755e-06

Current iteration: 12729
Current error: 6.17566002222e-06

Current iteration: 12730
Current error: 0.000928394701737

Current iteration: 12731
Current error: 9.39903839299e-05

Current iteration: 12732
Current error: 5.86486848291e-06

Current iteration: 12733
Current error: 0.068885947833

Current iteration: 12734
Current error: 5.05395228992e-06

Current iteration: 12735
Current error: 5.02424452626e-06

Current iteration: 12736
Current error: 5.01375417283e-06

Current iteration: 12737
Current error: 5.00431370968e-06

Current iteration: 12738
Current error: 4.9946618817e-06

Current iteration: 12739
Current error: 4.98573486186e-06

Current iteration: 12740
Current error: 0.0108262414715

Current iteration: 12741
Current error: 4.65013403418e-06

Current iteration: 12742
Current error: 4.65591493437e-06

Current iteration: 12743
Current error: 4.63532855486e-06

Current iteration: 12744
Current error: 4.62388261317e-06

Current iteration: 12745
Current error: 4.88071770006e-06

Current iteration: 12746
Current error: 4.60904247882e-06

Current iteration: 12747
Current error: 4.6001835751e-06

Current iteration: 12748
Current error: 4.59023850469e-06

Current iteration: 12749
Current error: 0.126893108987

Current iteration: 12750
Current error: 5.51477416209e-06

Current iteration: 12751
Current error: 5.50415967141e-06

Current iteration: 12752
Current error: 0.0113223010642

Current iteration: 12753
Current error: 0.00181455572893

Current iteration: 12754
Current error: 4.97536575529e-06

Current iteration: 12755
Current error: 4.96663497086e-06

Current iteration: 12756
Current error: 4.95648863587e-06

Current iteration: 12757
Current error: 4.94839155524e-06

Current iteration: 12758
Current error: 4.95188912797e-06

Current iteration: 12759
Current error: 0.0703653670476

Current iteration: 12760
Current error: 4.23983110677e-06

Current iteration: 12761
Current error: 0.00811284994063

Current iteration: 12762
Current error: 3.99417618037e-06

Current iteration: 12763
Current error: 3.98172519257e-06

Current iteration: 12764
Current error: 3.97338560972e-06

Current iteration: 12765
Current error: 3.96785504315e-06

Current iteration: 12766
Current error: 3.95959730814e-06

Current iteration: 12767
Current error: 4.36212273842e-06

Current iteration: 12768
Current error: 3.9468403346e-06

Current iteration: 12769
Current error: 3.94026983776e-06

Current iteration: 12770
Current error: 3.93360072413e-06

Current iteration: 12771
Current error: 3.93044509033e-06

Current iteration: 12772
Current error: 0.000367869157037

Current iteration: 12773
Current error: 5.02907084096e-06

Current iteration: 12774
Current error: 3.85803249206e-06

Current iteration: 12775
Current error: 3.85213226369e-06

Current iteration: 12776
Current error: 3.845174326e-06

Current iteration: 12777
Current error: 3.83873395863e-06

Current iteration: 12778
Current error: 3.83242140413e-06

Current iteration: 12779
Current error: 3.82607060209e-06

Current iteration: 12780
Current error: 4.85111126428e-06

Current iteration: 12781
Current error: 4.00571694584e-06

Current iteration: 12782
Current error: 3.80637706194e-06

Current iteration: 12783
Current error: 3.80010681131e-06

Current iteration: 12784
Current error: 0.0291320280382

Current iteration: 12785
Current error: 3.42022269816e-06

Current iteration: 12786
Current error: 3.41720205769e-06

Current iteration: 12787
Current error: 3.41006521083e-06

Current iteration: 12788
Current error: 3.40386093969e-06

Current iteration: 12789
Current error: 3.39888846673e-06

Current iteration: 12790
Current error: 5.20639470906e-06

Current iteration: 12791
Current error: 3.4041386426e-06

Current iteration: 12792
Current error: 3.38170196524e-06

Current iteration: 12793
Current error: 3.45091538691e-06

Current iteration: 12794
Current error: 3.371152548e-06

Current iteration: 12795
Current error: 3.36615919226e-06

Current iteration: 12796
Current error: 3.36110011732e-06

Current iteration: 12797
Current error: 0.0129619572171

Current iteration: 12798
Current error: 3.20190666673e-06

Current iteration: 12799
Current error: 3.11691997704e-06

Current iteration: 12800
Current error: 3.11230129007e-06

Current iteration: 12801
Current error: 3.10765262738e-06

Current iteration: 12802
Current error: 0.134827207597

Current iteration: 12803
Current error: 3.73624534776e-06

Current iteration: 12804
Current error: 3.73121665089e-06

Current iteration: 12805
Current error: 3.74879670978e-06

Current iteration: 12806
Current error: 3.72701589327e-06

Current iteration: 12807
Current error: 3.71214530905e-06

Current iteration: 12808
Current error: 3.70519570829e-06

Current iteration: 12809
Current error: 3.70676434738e-06

Current iteration: 12810
Current error: 3.69556093601e-06

Current iteration: 12811
Current error: 1.5203716993e-05

Current iteration: 12812
Current error: 3.67925693443e-06

Current iteration: 12813
Current error: 0.151486835498

Current iteration: 12814
Current error: 4.52527502449e-06

Current iteration: 12815
Current error: 4.51667321603e-06

Current iteration: 12816
Current error: 4.67874674951e-06

Current iteration: 12817
Current error: 4.50025404252e-06

Current iteration: 12818
Current error: 0.0523070563925

Current iteration: 12819
Current error: 3.93040697092e-06

Current iteration: 12820
Current error: 4.33395830169e-06

Current iteration: 12821
Current error: 7.24741879611e-06

Current iteration: 12822
Current error: 3.93828630772e-06

Current iteration: 12823
Current error: 3.9019768825e-06

Current iteration: 12824
Current error: 3.89501356126e-06

Current iteration: 12825
Current error: 4.4678362922e-06

Current iteration: 12826
Current error: 3.90651836812e-06

Current iteration: 12827
Current error: 3.87481669722e-06

Current iteration: 12828
Current error: 3.86771104029e-06

Current iteration: 12829
Current error: 3.86349052691e-06

Current iteration: 12830
Current error: 3.85545852067e-06

Current iteration: 12831
Current error: 3.9166114206e-06

Current iteration: 12832
Current error: 3.84259518642e-06

Current iteration: 12833
Current error: 3.93409184869e-06

Current iteration: 12834
Current error: 3.82978383598e-06

Current iteration: 12835
Current error: 3.82353801904e-06

Current iteration: 12836
Current error: 3.81611732759e-06

Current iteration: 12837
Current error: 6.8504974385e-05

Current iteration: 12838
Current error: 3.78639326801e-06

Current iteration: 12839
Current error: 3.79420347363e-06

Current iteration: 12840
Current error: 3.77395758289e-06

Current iteration: 12841
Current error: 3.76827839117e-06

Current iteration: 12842
Current error: 3.76146232311e-06

Current iteration: 12843
Current error: 3.75527504418e-06

Current iteration: 12844
Current error: 3.75012866142e-06

Current iteration: 12845
Current error: 3.74578204318e-06

Current iteration: 12846
Current error: 3.73683242787e-06

Current iteration: 12847
Current error: 3.73470837468e-06

Current iteration: 12848
Current error: 3.72831809191e-06

Current iteration: 12849
Current error: 0.135308353701

Current iteration: 12850
Current error: 0.109372378882

Current iteration: 12851
Current error: 5.31629781861e-06

Current iteration: 12852
Current error: 0.0316378975756

Current iteration: 12853
Current error: 5.15332284023e-06

Current iteration: 12854
Current error: 4.7714480601e-06

Current iteration: 12855
Current error: 0.00029494141007

Current iteration: 12856
Current error: 4.68015271855e-06

Current iteration: 12857
Current error: 4.67029025335e-06

Current iteration: 12858
Current error: 4.66508490809e-06

Current iteration: 12859
Current error: 4.65370959739e-06

Current iteration: 12860
Current error: 5.87026126933e-06

Current iteration: 12861
Current error: 4.63973434205e-06

Current iteration: 12862
Current error: 5.45819214825e-06

Current iteration: 12863
Current error: 4.62087315867e-06

Current iteration: 12864
Current error: 0.147584098832

Current iteration: 12865
Current error: 5.68253745612e-06

Current iteration: 12866
Current error: 0.105335379403

Current iteration: 12867
Current error: 6.695424898e-06

Current iteration: 12868
Current error: 6.69167014692e-06

Current iteration: 12869
Current error: 6.66638954239e-06

Current iteration: 12870
Current error: 6.65196783152e-06

Current iteration: 12871
Current error: 6.63694053877e-06

Current iteration: 12872
Current error: 6.62265294114e-06

Current iteration: 12873
Current error: 2.84550307035e-05

Current iteration: 12874
Current error: 5.11410999111e-05

Current iteration: 12875
Current error: 0.00427521752268

Current iteration: 12876
Current error: 6.25524416188e-06

Current iteration: 12877
Current error: 6.25938739574e-06

Current iteration: 12878
Current error: 6.2305555259e-06

Current iteration: 12879
Current error: 6.21437477512e-06

Current iteration: 12880
Current error: 6.24235663162e-06

Current iteration: 12881
Current error: 7.0545048005e-06

Current iteration: 12882
Current error: 6.17486884731e-06

Current iteration: 12883
Current error: 6.16152239052e-06

Current iteration: 12884
Current error: 0.0991834337547

Current iteration: 12885
Current error: 7.23346619534e-06

Current iteration: 12886
Current error: 0.000109786398112

Current iteration: 12887
Current error: 0.0321011644289

Current iteration: 12888
Current error: 6.57295335007e-06

Current iteration: 12889
Current error: 6.38111663184e-06

Current iteration: 12890
Current error: 6.62734448422e-06

Current iteration: 12891
Current error: 6.36591962655e-06

Current iteration: 12892
Current error: 0.086200824686

Current iteration: 12893
Current error: 8.3962917884e-05

Current iteration: 12894
Current error: 7.25320542392e-06

Current iteration: 12895
Current error: 2.58856171487e-05

Current iteration: 12896
Current error: 0.125322207152

Current iteration: 12897
Current error: 5.94907783796e-06

Current iteration: 12898
Current error: 5.93739692853e-06

Current iteration: 12899
Current error: 6.79273749095e-06

Current iteration: 12900
Current error: 5.91302651405e-06

Current iteration: 12901
Current error: 6.1220681651e-06

Current iteration: 12902
Current error: 5.88711511001e-06

Current iteration: 12903
Current error: 5.88922746066e-06

Current iteration: 12904
Current error: 5.86371949332e-06

Current iteration: 12905
Current error: 6.08157971446e-06

Current iteration: 12906
Current error: 0.102781614502

Current iteration: 12907
Current error: 4.89130513427e-06

Current iteration: 12908
Current error: 6.49597623739e-06

Current iteration: 12909
Current error: 4.87184525616e-06

Current iteration: 12910
Current error: 4.86530890814e-06

Current iteration: 12911
Current error: 4.85244683898e-06

Current iteration: 12912
Current error: 4.84486337996e-06

Current iteration: 12913
Current error: 4.83547500888e-06

Current iteration: 12914
Current error: 4.8301363716e-06

Current iteration: 12915
Current error: 4.84523702802e-06

Current iteration: 12916
Current error: 4.80853303661e-06

Current iteration: 12917
Current error: 4.79983893515e-06

Current iteration: 12918
Current error: 4.79905779725e-06

Current iteration: 12919
Current error: 4.78187971488e-06

Current iteration: 12920
Current error: 4.77322359862e-06

Current iteration: 12921
Current error: 4.89854007814e-06

Current iteration: 12922
Current error: 0.112996000226

Current iteration: 12923
Current error: 5.6528493782e-06

Current iteration: 12924
Current error: 5.65067561709e-06

Current iteration: 12925
Current error: 6.13883634238e-06

Current iteration: 12926
Current error: 5.61889458424e-06

Current iteration: 12927
Current error: 5.60665356546e-06

Current iteration: 12928
Current error: 5.60354752003e-06

Current iteration: 12929
Current error: 5.5873985143e-06

Current iteration: 12930
Current error: 5.57300199901e-06

Current iteration: 12931
Current error: 3.56983110384e-05

Current iteration: 12932
Current error: 5.54426744379e-06

Current iteration: 12933
Current error: 5.5368959701e-06

Current iteration: 12934
Current error: 5.5127751605e-06

Current iteration: 12935
Current error: 7.18211935982e-06

Current iteration: 12936
Current error: 5.48999092449e-06

Current iteration: 12937
Current error: 5.47942709397e-06

Current iteration: 12938
Current error: 1.13220439231e-05

Current iteration: 12939
Current error: 5.52074007826e-06

Current iteration: 12940
Current error: 5.44202011909e-06

Current iteration: 12941
Current error: 5.43111468589e-06

Current iteration: 12942
Current error: 0.106351645335

Current iteration: 12943
Current error: 6.4133975676e-06

Current iteration: 12944
Current error: 4.94594735593e-05

Current iteration: 12945
Current error: 6.44530720609e-06

Current iteration: 12946
Current error: 6.35034231687e-06

Current iteration: 12947
Current error: 6.33548141427e-06

Current iteration: 12948
Current error: 6.32199453298e-06

Current iteration: 12949
Current error: 6.31837335278e-06

Current iteration: 12950
Current error: 6.29472185027e-06

Current iteration: 12951
Current error: 6.28399151072e-06

Current iteration: 12952
Current error: 6.26808891964e-06

Current iteration: 12953
Current error: 6.2552388747e-06

Current iteration: 12954
Current error: 6.24199666124e-06

Current iteration: 12955
Current error: 6.2592423817e-06

Current iteration: 12956
Current error: 6.21592408592e-06

Current iteration: 12957
Current error: 6.20417056128e-06

Current iteration: 12958
Current error: 6.18973573017e-06

Current iteration: 12959
Current error: 0.0368417376604

Current iteration: 12960
Current error: 0.087634516916

Current iteration: 12961
Current error: 4.65005031346e-06

Current iteration: 12962
Current error: 4.64513613071e-06

Current iteration: 12963
Current error: 4.69032893046e-06

Current iteration: 12964
Current error: 4.68395643681e-06

Current iteration: 12965
Current error: 4.61767687009e-06

Current iteration: 12966
Current error: 4.60781405433e-06

Current iteration: 12967
Current error: 5.18792751518e-06

Current iteration: 12968
Current error: 4.59068868578e-06

Current iteration: 12969
Current error: 4.58249462492e-06

Current iteration: 12970
Current error: 4.57501973311e-06

Current iteration: 12971
Current error: 0.00124332971625

Current iteration: 12972
Current error: 4.50147305149e-06

Current iteration: 12973
Current error: 4.44705105628e-06

Current iteration: 12974
Current error: 4.43671904446e-06

Current iteration: 12975
Current error: 4.42794875499e-06

Current iteration: 12976
Current error: 0.193879765825

Current iteration: 12977
Current error: 5.75262026025e-06

Current iteration: 12978
Current error: 5.67328824067e-06

Current iteration: 12979
Current error: 5.66239120336e-06

Current iteration: 12980
Current error: 6.14113893953e-06

Current iteration: 12981
Current error: 5.64097528487e-06

Current iteration: 12982
Current error: 0.092169992184

Current iteration: 12983
Current error: 2.53543581857e-05

Current iteration: 12984
Current error: 5.22172277284e-06

Current iteration: 12985
Current error: 4.72022134951e-06

Current iteration: 12986
Current error: 0.000699580712121

Current iteration: 12987
Current error: 4.62837193458e-06

Current iteration: 12988
Current error: 4.61164698747e-06

Current iteration: 12989
Current error: 4.60337123199e-06

Current iteration: 12990
Current error: 4.59577620184e-06

Current iteration: 12991
Current error: 4.58819888275e-06

Current iteration: 12992
Current error: 4.59178494872e-06

Current iteration: 12993
Current error: 4.57726960857e-06

Current iteration: 12994
Current error: 0.103282631102

Current iteration: 12995
Current error: 5.37299061302e-06

Current iteration: 12996
Current error: 5.3536025086e-06

Current iteration: 12997
Current error: 5.3365429171e-06

Current iteration: 12998
Current error: 5.36093777769e-06

Current iteration: 12999
Current error: 7.12784192369e-06

Data has converged at the 13000th run.
Neural network is done training! Hit enter to validation processing.
Error percentage on training set: 0.01396

Parsing the validation dataset...
Begining validating the neural network:
Current iteration: 0
Current error: 5.42343447129e-06

Current iteration: 1
Current error: 5.30248588137e-06

Current iteration: 2
Current error: 5.29406967618e-06

Current iteration: 3
Current error: 5.29381482859e-06

Current iteration: 4
Current error: 5.29369715285e-06

Current iteration: 5
Current error: 5.29319296283e-06

Current iteration: 6
Current error: 5.29414488868e-06

Current iteration: 7
Current error: 5.29543861275e-06

Current iteration: 8
Current error: 5.37201544553e-06

Current iteration: 9
Current error: 5.29825731194e-06

Current iteration: 10
Current error: 5.29353772403e-06

Current iteration: 11
Current error: 5.30181766509e-06

Current iteration: 12
Current error: 5.29631121374e-06

Current iteration: 13
Current error: 5.30652581458e-06

Current iteration: 14
Current error: 5.29441366486e-06

Current iteration: 15
Current error: 5.29378000267e-06

Current iteration: 16
Current error: 5.29438870436e-06

Current iteration: 17
Current error: 5.29390832482e-06

Current iteration: 18
Current error: 5.29393277172e-06

Current iteration: 19
Current error: 5.29379067439e-06

Current iteration: 20
Current error: 5.2933298595e-06

Current iteration: 21
Current error: 5.30264371865e-06

Current iteration: 22
Current error: 5.29415353248e-06

Current iteration: 23
Current error: 5.29339592003e-06

Current iteration: 24
Current error: 5.29369604218e-06

Current iteration: 25
Current error: 1.37236418024e-05

Current iteration: 26
Current error: 5.29398146659e-06

Current iteration: 27
Current error: 5.29372091976e-06

Current iteration: 28
Current error: 5.2956983279e-06

Current iteration: 29
Current error: 5.42982242963e-06

Current iteration: 30
Current error: 5.29365624048e-06

Current iteration: 31
Current error: 5.29293671572e-06

Current iteration: 32
Current error: 5.29315854964e-06

Current iteration: 33
Current error: 5.29623498002e-06

Current iteration: 34
Current error: 5.29377452576e-06

Current iteration: 35
Current error: 5.29356871832e-06

Current iteration: 36
Current error: 5.35666141492e-06

Current iteration: 37
Current error: 5.2947772215e-06

Current iteration: 38
Current error: 5.29499411613e-06

Current iteration: 39
Current error: 5.29378987605e-06

Current iteration: 40
Current error: 5.2938474401e-06

Current iteration: 41
Current error: 5.29333893265e-06

Current iteration: 42
Current error: 9.55072378317e-06

Current iteration: 43
Current error: 5.29345032956e-06

Current iteration: 44
Current error: 1.09811364308e-05

Current iteration: 45
Current error: 5.71658722646e-06

Current iteration: 46
Current error: 5.74185497139e-06

Current iteration: 47
Current error: 5.29419679315e-06

Current iteration: 48
Current error: 5.29264758831e-06

Current iteration: 49
Current error: 5.29371028544e-06

Current iteration: 50
Current error: 5.29421296683e-06

Current iteration: 51
Current error: 5.63810552042e-06

Current iteration: 52
Current error: 5.29322671831e-06

Current iteration: 53
Current error: 5.29365752465e-06

Current iteration: 54
Current error: 5.29354733962e-06

Current iteration: 55
Current error: 5.31854642088e-06

Current iteration: 56
Current error: 5.29382146935e-06

Current iteration: 57
Current error: 5.29411758461e-06

Current iteration: 58
Current error: 5.29329536947e-06

Current iteration: 59
Current error: 5.29466596559e-06

Current iteration: 60
Current error: 5.29316128656e-06

Current iteration: 61
Current error: 5.29342124458e-06

Current iteration: 62
Current error: 5.29337356225e-06

Current iteration: 63
Current error: 5.29363494377e-06

Current iteration: 64
Current error: 5.29352395774e-06

Current iteration: 65
Current error: 5.2943579713e-06

Current iteration: 66
Current error: 0.151550624967

Current iteration: 67
Current error: 5.37727783541e-06

Current iteration: 68
Current error: 5.2943957971e-06

Current iteration: 69
Current error: 0.134388685306

Current iteration: 70
Current error: 5.29396555361e-06

Current iteration: 71
Current error: 5.29590747484e-06

Current iteration: 72
Current error: 5.29387484533e-06

Current iteration: 73
Current error: 5.2938614926e-06

Current iteration: 74
Current error: 5.29366645148e-06

Current iteration: 75
Current error: 5.29428452814e-06

Current iteration: 76
Current error: 5.93896584066e-06

Current iteration: 77
Current error: 0.132951438204

Current iteration: 78
Current error: 5.29671736909e-06

Current iteration: 79
Current error: 5.71940939072e-06

Current iteration: 80
Current error: 5.94742315379e-06

Current iteration: 81
Current error: 5.32001533574e-06

Current iteration: 82
Current error: 5.29398146659e-06

Current iteration: 83
Current error: 5.31637646631e-06

Current iteration: 84
Current error: 5.32011603018e-06

Current iteration: 85
Current error: 5.29367837606e-06

Current iteration: 86
Current error: 5.29955417529e-06

Current iteration: 87
Current error: 5.30555443483e-06

Current iteration: 88
Current error: 5.29270972071e-06

Current iteration: 89
Current error: 5.29513557848e-06

Current iteration: 90
Current error: 5.29376324218e-06

Current iteration: 91
Current error: 5.29386508354e-06

Current iteration: 92
Current error: 5.2937476608e-06

Current iteration: 93
Current error: 5.29341268959e-06

Current iteration: 94
Current error: 5.29417549333e-06

Current iteration: 95
Current error: 5.34045052186e-06

Current iteration: 96
Current error: 5.29425729634e-06

Current iteration: 97
Current error: 5.37727783541e-06

Current iteration: 98
Current error: 5.29380178535e-06

Current iteration: 99
Current error: 0.0755246159238

Data has converged at the 100th run.
Neural network is done validating! Hit enter to test it.
Error percentage on validation set: 6e-05

Begin testing the neural network:
Current iteration: 0
Current Error: 5.29682080884e-06

Current iteration: 1
Current Error: 5.29431277012e-06

Current iteration: 2
Current Error: 0.0965636046831

Current iteration: 3
Current Error: 5.29358717653e-06

Current iteration: 4
Current Error: 5.29364480929e-06

Current iteration: 5
Current Error: 5.29808749972e-06

Current iteration: 6
Current Error: 5.31838892382e-06

Current iteration: 7
Current Error: 0.0938806074007

Current iteration: 8
Current Error: 5.32393986785e-06

Current iteration: 9
Current Error: 0.00535891790315

Current iteration: 10
Current Error: 5.29444276351e-06

Current iteration: 11
Current Error: 5.32432653949e-06

Current iteration: 12
Current Error: 5.29388947631e-06

Current iteration: 13
Current Error: 5.2933093837e-06

Current iteration: 14
Current Error: 5.29324440025e-06

Current iteration: 15
Current Error: 5.29316846392e-06

Current iteration: 16
Current Error: 5.29371910346e-06

Current iteration: 17
Current Error: 5.29842196677e-06

Current iteration: 18
Current Error: 5.29358695076e-06

Current iteration: 19
Current Error: 5.34188251623e-06

Current iteration: 20
Current Error: 1.68095776852e-05

Current iteration: 21
Current Error: 5.29375637717e-06

Current iteration: 22
Current Error: 5.2934014661e-06

Current iteration: 23
Current Error: 5.29488074813e-06

Current iteration: 24
Current Error: 5.30409808711e-06

Current iteration: 25
Current Error: 0.000106174132417

Current iteration: 26
Current Error: 5.29790338613e-06

Current iteration: 27
Current Error: 5.29444549174e-06

Current iteration: 28
Current Error: 5.29643922609e-06

Current iteration: 29
Current Error: 5.29400540701e-06

Current iteration: 30
Current Error: 0.019803728984

Current iteration: 31
Current Error: 5.30435971731e-06

Current iteration: 32
Current Error: 5.45900887101e-06

Current iteration: 33
Current Error: 0.095120459187

Current iteration: 34
Current Error: 5.30760423027e-06

Current iteration: 35
Current Error: 5.29318918335e-06

Current iteration: 36
Current Error: 8.12103434847e-06

Current iteration: 37
Current Error: 5.29372464176e-06

Current iteration: 38
Current Error: 5.29359925491e-06

Current iteration: 39
Current Error: 1.57873428286e-05

Current iteration: 40
Current Error: 5.29542876089e-06

Current iteration: 41
Current Error: 0.00140595915341

Current iteration: 42
Current Error: 5.48130019623e-06

Current iteration: 43
Current Error: 1.15117124734e-05

Current iteration: 44
Current Error: 5.29790597375e-06

Current iteration: 45
Current Error: 5.29380546901e-06

Current iteration: 46
Current Error: 5.29514357352e-06

Current iteration: 47
Current Error: 5.29414439632e-06

Current iteration: 48
Current Error: 0.101408791063

Current iteration: 49
Current Error: 5.3632642886e-06

Current iteration: 50
Current Error: 5.30294104877e-06

Current iteration: 51
Current Error: 5.29375968154e-06

Current iteration: 52
Current Error: 2.73633506897e-05

Current iteration: 53
Current Error: 0.000394455514776

Current iteration: 54
Current Error: 5.29389204133e-06

Current iteration: 55
Current Error: 5.29354228545e-06

Current iteration: 56
Current Error: 5.2937588789e-06

Current iteration: 57
Current Error: 5.30298055695e-06

Current iteration: 58
Current Error: 5.30399730243e-06

Current iteration: 59
Current Error: 5.29378857642e-06

Current iteration: 60
Current Error: 5.29473391962e-06

Current iteration: 61
Current Error: 2.37818435245e-05

Current iteration: 62
Current Error: 0.159508689013

Current iteration: 63
Current Error: 5.89643551464e-06

Current iteration: 64
Current Error: 5.304187239e-06

Current iteration: 65
Current Error: 0.000119149272118

Current iteration: 66
Current Error: 5.296427489e-06

Current iteration: 67
Current Error: 5.2938705793e-06

Current iteration: 68
Current Error: 5.2932517209e-06

Current iteration: 69
Current Error: 5.34261844908e-06

Current iteration: 70
Current Error: 5.29229001908e-06

Current iteration: 71
Current Error: 5.29375136612e-06

Current iteration: 72
Current Error: 5.29350845328e-06

Current iteration: 73
Current Error: 0.104376587447

Current iteration: 74
Current Error: 5.29391728215e-06

Current iteration: 75
Current Error: 5.33571452286e-06

Current iteration: 76
Current Error: 5.29371093006e-06

Current iteration: 77
Current Error: 5.29651447032e-06

Current iteration: 78
Current Error: 5.35234208135e-06

Current iteration: 79
Current Error: 5.29397540802e-06

Current iteration: 80
Current Error: 5.29509044163e-06

Current iteration: 81
Current Error: 5.29383461483e-06

Current iteration: 82
Current Error: 5.29387624364e-06

Current iteration: 83
Current Error: 5.37164599734e-06

Current iteration: 84
Current Error: 8.99501163882e-06

Current iteration: 85
Current Error: 5.30365839656e-06

Current iteration: 86
Current Error: 0.000859401585862

Current iteration: 87
Current Error: 5.29349678402e-06

Current iteration: 88
Current Error: 5.29364703732e-06

Current iteration: 89
Current Error: 5.2938980672e-06

Current iteration: 90
Current Error: 5.29355710349e-06

Current iteration: 91
Current Error: 0.102137090663

Current iteration: 92
Current Error: 0.098444709292

Current iteration: 93
Current Error: 0.00359610144263

Current iteration: 94
Current Error: 5.30179904883e-06

Current iteration: 95
Current Error: 0.000184916562764

Current iteration: 96
Current Error: 4.99670129618e-05

Current iteration: 97
Current Error: 0.0955138156968

Current iteration: 98
Current Error: 5.29431893383e-06

Current iteration: 99
Current Error: 5.30534786156e-06

Current iteration: 100
Current Error: 5.2956983279e-06

Current iteration: 101
Current Error: 0.018601888867

Current iteration: 102
Current Error: 5.29387928799e-06

Current iteration: 103
Current Error: 5.32542328858e-06

Current iteration: 104
Current Error: 5.30074041131e-06

Current iteration: 105
Current Error: 0.0921557202645

Current iteration: 106
Current Error: 5.32011603018e-06

Current iteration: 107
Current Error: 5.11936989745e-05

Current iteration: 108
Current Error: 5.29368669701e-06

Current iteration: 109
Current Error: 5.29580091476e-06

Current iteration: 110
Current Error: 5.29304898081e-06

Current iteration: 111
Current Error: 5.29503035898e-06

Current iteration: 112
Current Error: 5.29386500046e-06

Current iteration: 113
Current Error: 5.29393277172e-06

Current iteration: 114
Current Error: 0.109772123379

Current iteration: 115
Current Error: 9.64771538443e-06

Current iteration: 116
Current Error: 5.29353567248e-06

Current iteration: 117
Current Error: 5.29256725276e-06

Current iteration: 118
Current Error: 5.29368004406e-06

Current iteration: 119
Current Error: 5.35115247481e-06

Current iteration: 120
Current Error: 5.29474150094e-06

Current iteration: 121
Current Error: 0.000104967247442

Current iteration: 122
Current Error: 5.29513947108e-06

Current iteration: 123
Current Error: 5.2945156988e-06

Current iteration: 124
Current Error: 5.48810216674e-06

Current iteration: 125
Current Error: 5.29950988135e-06

Current iteration: 126
Current Error: 0.106541934307

Current iteration: 127
Current Error: 5.2935372477e-06

Current iteration: 128
Current Error: 5.30675014214e-06

Current iteration: 129
Current Error: 5.29382847498e-06

Current iteration: 130
Current Error: 5.29489958737e-06

Current iteration: 131
Current Error: 5.29456553053e-06

Current iteration: 132
Current Error: 5.29393836857e-06

Current iteration: 133
Current Error: 5.29328112141e-06

Current iteration: 134
Current Error: 5.29382265164e-06

Current iteration: 135
Current Error: 0.320048872622

Current iteration: 136
Current Error: 5.29293308772e-06

Current iteration: 137
Current Error: 0.00140595915341

Current iteration: 138
Current Error: 5.97458705565e-06

Current iteration: 139
Current Error: 0.496749751144

Current iteration: 140
Current Error: 5.304187239e-06

Current iteration: 141
Current Error: 5.34285147334e-06

Current iteration: 142
Current Error: 5.29348800735e-06

Current iteration: 143
Current Error: 5.3813553925e-06

Current iteration: 144
Current Error: 0.00325022064995

Current iteration: 145
Current Error: 5.29380711829e-06

Current iteration: 146
Current Error: 5.29369608422e-06

Current iteration: 147
Current Error: 5.52109425598e-06

Current iteration: 148
Current Error: 5.29603782616e-06

Current iteration: 149
Current Error: 5.29459287447e-06

Current iteration: 150
Current Error: 5.30428482801e-06

Current iteration: 151
Current Error: 5.29397859337e-06

Current iteration: 152
Current Error: 5.29360586931e-06

Current iteration: 153
Current Error: 5.36650188426e-06

Current iteration: 154
Current Error: 5.29371454878e-06

Current iteration: 155
Current Error: 5.29724877783e-06

Current iteration: 156
Current Error: 5.29338692376e-06

Current iteration: 157
Current Error: 0.129819692888

Current iteration: 158
Current Error: 5.35234208135e-06

Current iteration: 159
Current Error: 5.29334077301e-06

Current iteration: 160
Current Error: 5.29381471614e-06

Current iteration: 161
Current Error: 0.000171842216473

Current iteration: 162
Current Error: 5.29372464176e-06

Current iteration: 163
Current Error: 5.29474496264e-06

Current iteration: 164
Current Error: 8.25166114582e-06

Current iteration: 165
Current Error: 5.29383947615e-06

Current iteration: 166
Current Error: 5.29495557111e-06

Current iteration: 167
Current Error: 0.00358667369413

Current iteration: 168
Current Error: 7.31439334942e-06

Current iteration: 169
Current Error: 5.29392114372e-06

Current iteration: 170
Current Error: 5.57855619842e-06

Current iteration: 171
Current Error: 5.29958776511e-06

Current iteration: 172
Current Error: 5.29470830407e-06

Current iteration: 173
Current Error: 5.29866923135e-06

Current iteration: 174
Current Error: 5.51435550587e-06

Current iteration: 175
Current Error: 5.29716525426e-06

Current iteration: 176
Current Error: 5.29409551763e-06

Current iteration: 177
Current Error: 5.29346289052e-06

Current iteration: 178
Current Error: 5.29708696838e-06

Current iteration: 179
Current Error: 0.000365706064518

Current iteration: 180
Current Error: 5.29488074813e-06

Current iteration: 181
Current Error: 5.30119573543e-06

Current iteration: 182
Current Error: 5.29354408461e-06

Current iteration: 183
Current Error: 0.0695832708643

Current iteration: 184
Current Error: 0.103197099704

Current iteration: 185
Current Error: 5.29645271683e-06

Current iteration: 186
Current Error: 5.29343605861e-06

Current iteration: 187
Current Error: 5.29593680783e-06

Current iteration: 188
Current Error: 5.29350297964e-06

Current iteration: 189
Current Error: 5.29395399817e-06

Current iteration: 190
Current Error: 5.2958706126e-06

Current iteration: 191
Current Error: 0.101089815395

Current iteration: 192
Current Error: 0.0994132434404

Current iteration: 193
Current Error: 5.13396790225e-05

Current iteration: 194
Current Error: 5.29435895474e-06

Current iteration: 195
Current Error: 5.29438531844e-06

Current iteration: 196
Current Error: 5.29713458584e-06

Current iteration: 197
Current Error: 6.83671382882e-06

Current iteration: 198
Current Error: 5.29360265448e-06

Current iteration: 199
Current Error: 0.135190263665

Current iteration: 200
Current Error: 5.29368688792e-06

Current iteration: 201
Current Error: 5.29326663259e-06

Current iteration: 202
Current Error: 5.32540056964e-06

Current iteration: 203
Current Error: 5.29441366486e-06

Current iteration: 204
Current Error: 5.36650188426e-06

Current iteration: 205
Current Error: 5.29335882439e-06

Current iteration: 206
Current Error: 5.29314575088e-06

Current iteration: 207
Current Error: 5.29427027555e-06

Current iteration: 208
Current Error: 5.87181778864e-06

Current iteration: 209
Current Error: 5.29378231813e-06

Current iteration: 210
Current Error: 0.0780866783063

Current iteration: 211
Current Error: 5.29541959841e-06

Current iteration: 212
Current Error: 6.18224313152e-06

Current iteration: 213
Current Error: 0.0277862217386

Current iteration: 214
Current Error: 1.09331737263e-05

Current iteration: 215
Current Error: 0.00168503064545

Current iteration: 216
Current Error: 5.29315044862e-06

Current iteration: 217
Current Error: 5.29372677716e-06

Current iteration: 218
Current Error: 5.29358474443e-06

Current iteration: 219
Current Error: 0.495989401616

Current iteration: 220
Current Error: 5.29346589863e-06

Current iteration: 221
Current Error: 5.29476423939e-06

Current iteration: 222
Current Error: 5.29451147899e-06

Current iteration: 223
Current Error: 5.29367101472e-06

Current iteration: 224
Current Error: 0.000187902499177

Current iteration: 225
Current Error: 5.29377766711e-06

Current iteration: 226
Current Error: 5.29431913912e-06

Current iteration: 227
Current Error: 5.29413517466e-06

Current iteration: 228
Current Error: 0.0547495441737

Current iteration: 229
Current Error: 5.30949166828e-06

Current iteration: 230
Current Error: 0.0306851483246

Current iteration: 231
Current Error: 5.29648610248e-06

Current iteration: 232
Current Error: 5.29863530788e-06

Current iteration: 233
Current Error: 5.29813754812e-06

Current iteration: 234
Current Error: 5.29309634887e-06

Current iteration: 235
Current Error: 5.29446355004e-06

Current iteration: 236
Current Error: 5.2936952127e-06

Current iteration: 237
Current Error: 5.29579853118e-06

Current iteration: 238
Current Error: 5.2935591655e-06

Current iteration: 239
Current Error: 5.32011603018e-06

Current iteration: 240
Current Error: 5.29443086125e-06

Current iteration: 241
Current Error: 5.29682284167e-06

Current iteration: 242
Current Error: 5.29337538808e-06

Current iteration: 243
Current Error: 5.29424808689e-06

Current iteration: 244
Current Error: 0.00910785084745

Current iteration: 245
Current Error: 5.29404853577e-06

Current iteration: 246
Current Error: 7.52728563075e-05

Current iteration: 247
Current Error: 5.29343696423e-06

Current iteration: 248
Current Error: 5.29376772071e-06

Current iteration: 249
Current Error: 5.29379397205e-06

Current iteration: 250
Current Error: 5.29419679315e-06

Current iteration: 251
Current Error: 5.29317295111e-06

Current iteration: 252
Current Error: 5.29360764033e-06

Current iteration: 253
Current Error: 5.46971451246e-06

Current iteration: 254
Current Error: 5.29388627308e-06

Current iteration: 255
Current Error: 5.29638810489e-06

Current iteration: 256
Current Error: 5.29460388957e-06

Current iteration: 257
Current Error: 5.29368358482e-06

Current iteration: 258
Current Error: 5.35333927107e-06

Current iteration: 259
Current Error: 5.29345972366e-06

Current iteration: 260
Current Error: 5.55291381385e-06

Current iteration: 261
Current Error: 5.29599799976e-06

Current iteration: 262
Current Error: 5.29355162664e-06

Current iteration: 263
Current Error: 6.58115863666e-06

Current iteration: 264
Current Error: 5.29386187348e-06

Current iteration: 265
Current Error: 5.29330059806e-06

Current iteration: 266
Current Error: 7.57392398769e-05

Current iteration: 267
Current Error: 5.29372641212e-06

Current iteration: 268
Current Error: 5.42343447129e-06

Current iteration: 269
Current Error: 5.34188251623e-06

Current iteration: 270
Current Error: 5.29269862465e-06

Current iteration: 271
Current Error: 5.30079756385e-06

Current iteration: 272
Current Error: 5.30800541207e-06

Current iteration: 273
Current Error: 5.29305734295e-06

Current iteration: 274
Current Error: 5.29391541607e-06

Current iteration: 275
Current Error: 5.3121092387e-06

Current iteration: 276
Current Error: 5.5263163734e-06

Current iteration: 277
Current Error: 5.29608150614e-06

Current iteration: 278
Current Error: 0.294728845263

Current iteration: 279
Current Error: 0.0925129960292

Current iteration: 280
Current Error: 5.29292620465e-06

Current iteration: 281
Current Error: 5.29803092869e-06

Current iteration: 282
Current Error: 5.43554953782e-06

Current iteration: 283
Current Error: 5.30547120489e-06

Current iteration: 284
Current Error: 5.29755850254e-06

Current iteration: 285
Current Error: 5.29447138051e-06

Current iteration: 286
Current Error: 0.0162854073699

Current iteration: 287
Current Error: 5.29460439402e-06

Current iteration: 288
Current Error: 5.29293694707e-06

Current iteration: 289
Current Error: 5.29355000461e-06

Current iteration: 290
Current Error: 5.29377976157e-06

Current iteration: 291
Current Error: 5.29373805491e-06

Current iteration: 292
Current Error: 5.29325022206e-06

Current iteration: 293
Current Error: 5.30436769708e-06

Current iteration: 294
Current Error: 5.29471093376e-06

Current iteration: 295
Current Error: 5.41803321677e-06

Current iteration: 296
Current Error: 5.29366645148e-06

Current iteration: 297
Current Error: 5.29375758805e-06

Current iteration: 298
Current Error: 5.29347702433e-06

Current iteration: 299
Current Error: 5.33169293197e-06

Current iteration: 300
Current Error: 0.00199575121827

Current iteration: 301
Current Error: 5.29329952755e-06

Current iteration: 302
Current Error: 0.00122790242109

Current iteration: 303
Current Error: 5.29425661639e-06

Current iteration: 304
Current Error: 5.29384219375e-06

Current iteration: 305
Current Error: 5.29421947265e-06

Current iteration: 306
Current Error: 5.29425729634e-06

Current iteration: 307
Current Error: 1.00671137004e-05

Current iteration: 308
Current Error: 0.00251458355667

Current iteration: 309
Current Error: 5.29338450015e-06

Current iteration: 310
Current Error: 5.30368714257e-06

Current iteration: 311
Current Error: 5.29327068951e-06

Current iteration: 312
Current Error: 5.29355490427e-06

Current iteration: 313
Current Error: 0.0275549743212

Current iteration: 314
Current Error: 5.29366846493e-06

Current iteration: 315
Current Error: 5.2938354489e-06

Current iteration: 316
Current Error: 9.64771538443e-06

Current iteration: 317
Current Error: 6.34084189896e-06

Current iteration: 318
Current Error: 5.29348620759e-06

Current iteration: 319
Current Error: 5.29308656447e-06

Current iteration: 320
Current Error: 5.30011189256e-06

Current iteration: 321
Current Error: 5.29374706264e-06

Current iteration: 322
Current Error: 0.0681161405386

Current iteration: 323
Current Error: 5.29373476975e-06

Current iteration: 324
Current Error: 5.29368657241e-06

Current iteration: 325
Current Error: 5.31759889362e-06

Current iteration: 326
Current Error: 5.29360832475e-06

Current iteration: 327
Current Error: 5.29437975196e-06

Current iteration: 328
Current Error: 5.29470830407e-06

Current iteration: 329
Current Error: 5.29373017512e-06

Current iteration: 330
Current Error: 5.2927983238e-06

Current iteration: 331
Current Error: 8.43537693946e-06

Current iteration: 332
Current Error: 5.29330715331e-06

Current iteration: 333
Current Error: 5.29381287569e-06

Current iteration: 334
Current Error: 5.29379820861e-06

Current iteration: 335
Current Error: 5.29341720909e-06

Current iteration: 336
Current Error: 5.30547120489e-06

Current iteration: 337
Current Error: 5.29359119801e-06

Current iteration: 338
Current Error: 5.29366207741e-06

Current iteration: 339
Current Error: 5.2936112262e-06

Current iteration: 340
Current Error: 6.00954499169e-06

Current iteration: 341
Current Error: 5.29343089722e-06

Current iteration: 342
Current Error: 5.35884625782e-06

Current iteration: 343
Current Error: 5.29430668166e-06

Current iteration: 344
Current Error: 1.27573197313e-05

Current iteration: 345
Current Error: 5.29349238549e-06

Current iteration: 346
Current Error: 5.29330798476e-06

Current iteration: 347
Current Error: 5.2949837789e-06

Current iteration: 348
Current Error: 5.30165489018e-06

Current iteration: 349
Current Error: 5.33116458515e-06

Current iteration: 350
Current Error: 5.29724877783e-06

Current iteration: 351
Current Error: 5.29298381861e-06

Current iteration: 352
Current Error: 6.06622678127e-06

Current iteration: 353
Current Error: 5.29327449883e-06

Current iteration: 354
Current Error: 5.29356943455e-06

Current iteration: 355
Current Error: 5.29611211209e-06

Current iteration: 356
Current Error: 5.29358494413e-06

Current iteration: 357
Current Error: 5.29450795952e-06

Current iteration: 358
Current Error: 5.29611230515e-06

Current iteration: 359
Current Error: 5.2941324309e-06

Current iteration: 360
Current Error: 5.29380711829e-06

Current iteration: 361
Current Error: 5.2975060936e-06

Current iteration: 362
Current Error: 4.21873484156e-05

Current iteration: 363
Current Error: 6.0767065832e-06

Current iteration: 364
Current Error: 0.0576193555561

Current iteration: 365
Current Error: 3.11624535343e-05

Current iteration: 366
Current Error: 5.29341208774e-06

Current iteration: 367
Current Error: 5.29411136236e-06

Current iteration: 368
Current Error: 0.0222970642664

Current iteration: 369
Current Error: 5.29203713753e-06

Current iteration: 370
Current Error: 5.29341887975e-06

Current iteration: 371
Current Error: 5.29292444801e-06

Current iteration: 372
Current Error: 5.29392555223e-06

Current iteration: 373
Current Error: 5.29355963381e-06

Current iteration: 374
Current Error: 0.000578919019353

Current iteration: 375
Current Error: 5.2931701723e-06

Current iteration: 376
Current Error: 5.29355134962e-06

Current iteration: 377
Current Error: 5.29389750975e-06

Current iteration: 378
Current Error: 0.121997103557

Current iteration: 379
Current Error: 5.2938282568e-06

Current iteration: 380
Current Error: 0.0392445344182

Current iteration: 381
Current Error: 5.29456235064e-06

Current iteration: 382
Current Error: 5.29393552778e-06

Current iteration: 383
Current Error: 5.29379120817e-06

Current iteration: 384
Current Error: 5.3113102996e-06

Current iteration: 385
Current Error: 1.81745390086e-05

Current iteration: 386
Current Error: 5.29394274259e-06

Current iteration: 387
Current Error: 5.2934535207e-06

Current iteration: 388
Current Error: 5.29346846331e-06

Current iteration: 389
Current Error: 5.29369955215e-06

Current iteration: 390
Current Error: 5.29368632792e-06

Current iteration: 391
Current Error: 5.29552727752e-06

Current iteration: 392
Current Error: 5.29352739416e-06

Current iteration: 393
Current Error: 5.29321887844e-06

Current iteration: 394
Current Error: 5.35326944857e-06

Current iteration: 395
Current Error: 5.29379820861e-06

Current iteration: 396
Current Error: 4.21873484156e-05

Current iteration: 397
Current Error: 5.29380486802e-06

Current iteration: 398
Current Error: 5.29387618448e-06

Current iteration: 399
Current Error: 5.30056247722e-06

Current iteration: 400
Current Error: 5.29558817189e-06

Current iteration: 401
Current Error: 0.0301860661455

Current iteration: 402
Current Error: 5.29380250378e-06

Current iteration: 403
Current Error: 0.102857921732

Current iteration: 404
Current Error: 0.0474854035616

Current iteration: 405
Current Error: 5.29374828823e-06

Current iteration: 406
Current Error: 0.000119149272118

Current iteration: 407
Current Error: 5.32886251189e-06

Current iteration: 408
Current Error: 0.0645624164836

Current iteration: 409
Current Error: 5.41858060074e-06

Current iteration: 410
Current Error: 5.29806366373e-06

Current iteration: 411
Current Error: 5.29316362599e-06

Current iteration: 412
Current Error: 5.47865474509e-06

Current iteration: 413
Current Error: 5.92117991375e-06

Current iteration: 414
Current Error: 5.44157677989e-06

Current iteration: 415
Current Error: 5.29416740137e-06

Current iteration: 416
Current Error: 0.113068263461

Current iteration: 417
Current Error: 5.32082052457e-06

Current iteration: 418
Current Error: 5.32602744854e-06

Current iteration: 419
Current Error: 5.29337277033e-06

Current iteration: 420
Current Error: 5.33941158713e-06

Current iteration: 421
Current Error: 5.29459287447e-06

Current iteration: 422
Current Error: 5.32542328858e-06

Current iteration: 423
Current Error: 0.0306851483246

Current iteration: 424
Current Error: 5.30002168282e-06

Current iteration: 425
Current Error: 5.55648037066e-06

Current iteration: 426
Current Error: 5.30065320884e-06

Current iteration: 427
Current Error: 5.29379449434e-06

Current iteration: 428
Current Error: 5.29351930693e-06

Current iteration: 429
Current Error: 5.29392285951e-06

Current iteration: 430
Current Error: 0.129819692888

Current iteration: 431
Current Error: 5.29358278768e-06

Current iteration: 432
Current Error: 0.100313731756

Current iteration: 433
Current Error: 5.29357377872e-06

Current iteration: 434
Current Error: 5.2934897036e-06

Current iteration: 435
Current Error: 5.29349878241e-06

Current iteration: 436
Current Error: 5.38015259983e-06

Current iteration: 437
Current Error: 5.55648037066e-06

Current iteration: 438
Current Error: 0.0904202988251

Current iteration: 439
Current Error: 5.29371858775e-06

Current iteration: 440
Current Error: 5.293554386e-06

Current iteration: 441
Current Error: 5.29353607169e-06

Current iteration: 442
Current Error: 5.2950858065e-06

Current iteration: 443
Current Error: 5.29363998386e-06

Current iteration: 444
Current Error: 5.3680225489e-06

Current iteration: 445
Current Error: 5.29368004406e-06

Current iteration: 446
Current Error: 5.2943705645e-06

Current iteration: 447
Current Error: 5.29336277554e-06

Current iteration: 448
Current Error: 5.29404211461e-06

Current iteration: 449
Current Error: 5.29503035898e-06

Current iteration: 450
Current Error: 5.29434164665e-06

Current iteration: 451
Current Error: 5.2936364711e-06

Current iteration: 452
Current Error: 5.29384061468e-06

Current iteration: 453
Current Error: 5.2942394681e-06

Current iteration: 454
Current Error: 5.2958706126e-06

Current iteration: 455
Current Error: 5.29366470229e-06

Current iteration: 456
Current Error: 5.29334115354e-06

Current iteration: 457
Current Error: 5.29318550542e-06

Current iteration: 458
Current Error: 5.29385817209e-06

Current iteration: 459
Current Error: 0.0931285719454

Current iteration: 460
Current Error: 5.29417549333e-06

Current iteration: 461
Current Error: 0.0757259558046

Current iteration: 462
Current Error: 5.31636136955e-06

Current iteration: 463
Current Error: 0.10743574859

Current iteration: 464
Current Error: 5.29394878972e-06

Current iteration: 465
Current Error: 5.29641009468e-06

Current iteration: 466
Current Error: 0.000137224006312

Current iteration: 467
Current Error: 5.29386064807e-06

Current iteration: 468
Current Error: 5.29374646276e-06

Current iteration: 469
Current Error: 5.29955545942e-06

Current iteration: 470
Current Error: 5.29357414447e-06

Current iteration: 471
Current Error: 5.33572408676e-06

Current iteration: 472
Current Error: 5.29499411613e-06

Current iteration: 473
Current Error: 5.29389164714e-06

Current iteration: 474
Current Error: 5.29433941425e-06

Current iteration: 475
Current Error: 5.29366803547e-06

Current iteration: 476
Current Error: 5.29396720274e-06

Current iteration: 477
Current Error: 5.29375121898e-06

Current iteration: 478
Current Error: 5.29404853577e-06

Current iteration: 479
Current Error: 5.30760345222e-06

Current iteration: 480
Current Error: 0.00535361328119

Current iteration: 481
Current Error: 5.29376538119e-06

Current iteration: 482
Current Error: 5.29309954634e-06

Current iteration: 483
Current Error: 5.58512795193e-06

Current iteration: 484
Current Error: 5.91526910395e-06

Current iteration: 485
Current Error: 5.29391474421e-06

Current iteration: 486
Current Error: 5.29368023094e-06

Current iteration: 487
Current Error: 5.29565214364e-06

Current iteration: 488
Current Error: 5.49432289729e-06

Current iteration: 489
Current Error: 5.29424478319e-06

Current iteration: 490
Current Error: 5.29398051549e-06

Current iteration: 491
Current Error: 5.34883877466e-06

Current iteration: 492
Current Error: 0.164116234973

Current iteration: 493
Current Error: 0.164116234973

Current iteration: 494
Current Error: 5.52879653331e-06

Current iteration: 495
Current Error: 5.29376772071e-06

Current iteration: 496
Current Error: 5.29377999836e-06

Current iteration: 497
Current Error: 5.29424374878e-06

Current iteration: 498
Current Error: 5.29365542822e-06

Current iteration: 499
Current Error: 0.083415647395

Current iteration: 500
Current Error: 5.29352386898e-06

Current iteration: 501
Current Error: 5.57855619842e-06

Current iteration: 502
Current Error: 5.29441096239e-06

Current iteration: 503
Current Error: 5.31595897494e-06

Current iteration: 504
Current Error: 5.29349878241e-06

Current iteration: 505
Current Error: 5.29441678937e-06

Current iteration: 506
Current Error: 5.29453070543e-06

Current iteration: 507
Current Error: 5.2942947735e-06

Current iteration: 508
Current Error: 5.29386830678e-06

Current iteration: 509
Current Error: 0.0965874891105

Current iteration: 510
Current Error: 5.56823379829e-06

Current iteration: 511
Current Error: 0.0289715673608

Current iteration: 512
Current Error: 5.33497627988e-06

Current iteration: 513
Current Error: 0.0943029698163

Current iteration: 514
Current Error: 5.29411136236e-06

Current iteration: 515
Current Error: 5.29333971217e-06

Current iteration: 516
Current Error: 5.33845499926e-06

Current iteration: 517
Current Error: 0.294118308413

Current iteration: 518
Current Error: 0.000359569518575

Current iteration: 519
Current Error: 5.29554668882e-06

Current iteration: 520
Current Error: 5.2937834427e-06

Current iteration: 521
Current Error: 5.31936658152e-06

Current iteration: 522
Current Error: 5.296427489e-06

Current iteration: 523
Current Error: 5.29465727511e-06

Current iteration: 524
Current Error: 5.29366018241e-06

Current iteration: 525
Current Error: 0.0919503558345

Current iteration: 526
Current Error: 5.30675014214e-06

Current iteration: 527
Current Error: 5.29354927248e-06

Current iteration: 528
Current Error: 0.0254389683472

Current iteration: 529
Current Error: 5.29665739605e-06

Current iteration: 530
Current Error: 1.19793654252e-05

Current iteration: 531
Current Error: 0.0474854035616

Current iteration: 532
Current Error: 5.29339972503e-06

Current iteration: 533
Current Error: 6.83671382882e-06

Current iteration: 534
Current Error: 5.29380628634e-06

Current iteration: 535
Current Error: 5.2935884849e-06

Current iteration: 536
Current Error: 5.29533398279e-06

Current iteration: 537
Current Error: 5.32812347547e-06

Current iteration: 538
Current Error: 5.29366746511e-06

Current iteration: 539
Current Error: 5.29343476472e-06

Current iteration: 540
Current Error: 0.00358667369413

Current iteration: 541
Current Error: 5.29427027555e-06

Current iteration: 542
Current Error: 0.000137224006312

Current iteration: 543
Current Error: 5.29501398695e-06

Current iteration: 544
Current Error: 5.29389984076e-06

Current iteration: 545
Current Error: 0.0953784044298

Current iteration: 546
Current Error: 5.29377827319e-06

Current iteration: 547
Current Error: 5.29842196677e-06

Current iteration: 548
Current Error: 5.29368293727e-06

Current iteration: 549
Current Error: 5.2940344751e-06

Current iteration: 550
Current Error: 5.29372082953e-06

Current iteration: 551
Current Error: 5.29518582164e-06

Current iteration: 552
Current Error: 5.29321813253e-06

Current iteration: 553
Current Error: 5.30368714257e-06

Current iteration: 554
Current Error: 5.29364042557e-06

Current iteration: 555
Current Error: 8.99501163882e-06

Current iteration: 556
Current Error: 5.29556160205e-06

Current iteration: 557
Current Error: 5.31248932194e-06

Current iteration: 558
Current Error: 5.29280408378e-06

Current iteration: 559
Current Error: 5.29368817589e-06

Current iteration: 560
Current Error: 0.0887485562931

Current iteration: 561
Current Error: 5.29357471131e-06

Current iteration: 562
Current Error: 1.58053759628e-05

Current iteration: 563
Current Error: 5.29297288731e-06

Current iteration: 564
Current Error: 0.105234619368

Current iteration: 565
Current Error: 5.29391281628e-06

Current iteration: 566
Current Error: 5.29422949189e-06

Current iteration: 567
Current Error: 5.35411158464e-06

Current iteration: 568
Current Error: 0.0904202988251

Current iteration: 569
Current Error: 4.73961249685e-05

Current iteration: 570
Current Error: 5.66101725075e-06

Current iteration: 571
Current Error: 5.30383016409e-06

Current iteration: 572
Current Error: 5.29421296683e-06

Current iteration: 573
Current Error: 5.29450167174e-06

Current iteration: 574
Current Error: 6.21088595191e-06

Current iteration: 575
Current Error: 5.29341100177e-06

Current iteration: 576
Current Error: 5.29337866863e-06

Current iteration: 577
Current Error: 1.85606864555e-05

Current iteration: 578
Current Error: 0.187194330447

Current iteration: 579
Current Error: 5.29373885525e-06

Current iteration: 580
Current Error: 5.29305789439e-06

Current iteration: 581
Current Error: 0.0664939093564

Current iteration: 582
Current Error: 5.29560273962e-06

Current iteration: 583
Current Error: 5.29385759797e-06

Current iteration: 584
Current Error: 5.29328093838e-06

Current iteration: 585
Current Error: 5.29364754633e-06

Current iteration: 586
Current Error: 0.118240475919

Current iteration: 587
Current Error: 5.40896984092e-06

Current iteration: 588
Current Error: 5.29331829212e-06

Current iteration: 589
Current Error: 5.66989267281e-06

Current iteration: 590
Current Error: 5.29350644988e-06

Current iteration: 591
Current Error: 5.29398051549e-06

Current iteration: 592
Current Error: 5.29350845328e-06

Current iteration: 593
Current Error: 0.0970766249453

Current iteration: 594
Current Error: 5.36650188426e-06

Current iteration: 595
Current Error: 0.000187902499177

Current iteration: 596
Current Error: 5.29451301318e-06

Current iteration: 597
Current Error: 0.147368877052

Current iteration: 598
Current Error: 5.29386665428e-06

Current iteration: 599
Current Error: 5.45284144347e-06

Current iteration: 600
Current Error: 5.29382247518e-06

Current iteration: 601
Current Error: 5.29356565725e-06

Current iteration: 602
Current Error: 5.29350819339e-06

Current iteration: 603
Current Error: 5.29361781502e-06

Current iteration: 604
Current Error: 5.29264758831e-06

Current iteration: 605
Current Error: 5.29389164714e-06

Current iteration: 606
Current Error: 0.000150323114655

Current iteration: 607
Current Error: 7.64975162567e-06

Current iteration: 608
Current Error: 5.35024432391e-06

Current iteration: 609
Current Error: 5.29488074813e-06

Current iteration: 610
Current Error: 5.30436769708e-06

Current iteration: 611
Current Error: 5.30077720852e-06

Current iteration: 612
Current Error: 6.84389250102e-06

Current iteration: 613
Current Error: 5.29370277032e-06

Current iteration: 614
Current Error: 5.29307085208e-06

Current iteration: 615
Current Error: 5.29385487827e-06

Current iteration: 616
Current Error: 5.29918237954e-06

Current iteration: 617
Current Error: 0.0160745252918

Current iteration: 618
Current Error: 5.29380546901e-06

Current iteration: 619
Current Error: 0.000111381475823

Current iteration: 620
Current Error: 5.29644747698e-06

Current iteration: 621
Current Error: 5.29410299801e-06

Current iteration: 622
Current Error: 5.29380799012e-06

Current iteration: 623
Current Error: 5.29514591273e-06

Current iteration: 624
Current Error: 5.29151078414e-06

Current iteration: 625
Current Error: 5.41803321677e-06

Current iteration: 626
Current Error: 0.00633364361684

Current iteration: 627
Current Error: 0.0991159232564

Current iteration: 628
Current Error: 5.29483743226e-06

Current iteration: 629
Current Error: 5.3113102996e-06

Current iteration: 630
Current Error: 5.29361286007e-06

Current iteration: 631
Current Error: 5.29416076601e-06

Current iteration: 632
Current Error: 0.0855766025476

Current iteration: 633
Current Error: 0.0981991609736

Current iteration: 634
Current Error: 5.29396093457e-06

Current iteration: 635
Current Error: 5.29387928799e-06

Current iteration: 636
Current Error: 5.30409275748e-06

Current iteration: 637
Current Error: 5.34762334203e-06

Current iteration: 638
Current Error: 5.40343673742e-06

Current iteration: 639
Current Error: 1.00927617971e-05

Current iteration: 640
Current Error: 5.2932271338e-06

Current iteration: 641
Current Error: 5.29382246614e-06

Current iteration: 642
Current Error: 5.29333075258e-06

Current iteration: 643
Current Error: 0.00543365548842

Current iteration: 644
Current Error: 5.41956416079e-06

Current iteration: 645
Current Error: 5.94537893436e-06

Current iteration: 646
Current Error: 5.29368939327e-06

Current iteration: 647
Current Error: 5.29255923427e-06

Current iteration: 648
Current Error: 0.0266853169411

Current iteration: 649
Current Error: 1.46567115812e-05

Current iteration: 650
Current Error: 7.87427764628e-06

Current iteration: 651
Current Error: 5.29384331078e-06

Current iteration: 652
Current Error: 5.2941735028e-06

Current iteration: 653
Current Error: 5.29358745709e-06

Current iteration: 654
Current Error: 5.57982362407e-06

Current iteration: 655
Current Error: 5.29355378864e-06

Current iteration: 656
Current Error: 0.0940710193042

Current iteration: 657
Current Error: 5.29363610051e-06

Current iteration: 658
Current Error: 5.2947350456e-06

Current iteration: 659
Current Error: 5.29465727511e-06

Current iteration: 660
Current Error: 5.29276725279e-06

Current iteration: 661
Current Error: 5.29362487573e-06

Current iteration: 662
Current Error: 0.277004341039

Current iteration: 663
Current Error: 5.29366915302e-06

Current iteration: 664
Current Error: 5.29432853188e-06

Current iteration: 665
Current Error: 0.0314514370485

Current iteration: 666
Current Error: 5.30119573543e-06

Current iteration: 667
Current Error: 5.29270540344e-06

Current iteration: 668
Current Error: 5.29389899382e-06

Current iteration: 669
Current Error: 5.29367722142e-06

Current iteration: 670
Current Error: 5.29363399398e-06

Current iteration: 671
Current Error: 5.29348884819e-06

Current iteration: 672
Current Error: 5.29437975196e-06

Current iteration: 673
Current Error: 5.29532005432e-06

Current iteration: 674
Current Error: 5.29321628364e-06

Current iteration: 675
Current Error: 5.31637646631e-06

Current iteration: 676
Current Error: 5.3680225489e-06

Current iteration: 677
Current Error: 5.29722268492e-06

Current iteration: 678
Current Error: 5.37727783541e-06

Current iteration: 679
Current Error: 5.29409623378e-06

Current iteration: 680
Current Error: 5.33205863954e-06

Current iteration: 681
Current Error: 5.29385817209e-06

Current iteration: 682
Current Error: 6.56554417895e-06

Current iteration: 683
Current Error: 0.0999229937533

Current iteration: 684
Current Error: 5.29346630336e-06

Current iteration: 685
Current Error: 0.00325022064995

Current iteration: 686
Current Error: 5.29307737359e-06

Current iteration: 687
Current Error: 5.29691033219e-06

Current iteration: 688
Current Error: 5.30551407991e-06

Current iteration: 689
Current Error: 5.2932996679e-06

Current iteration: 690
Current Error: 5.29396584336e-06

Current iteration: 691
Current Error: 0.316977489231

Current iteration: 692
Current Error: 5.29342858868e-06

Current iteration: 693
Current Error: 5.29369604218e-06

Current iteration: 694
Current Error: 5.29471883401e-06

Current iteration: 695
Current Error: 1.94606274729e-05

Current iteration: 696
Current Error: 5.73551117178e-06

Current iteration: 697
Current Error: 5.29415237941e-06

Current iteration: 698
Current Error: 5.29258136906e-06

Current iteration: 699
Current Error: 5.29342257664e-06

Current iteration: 700
Current Error: 5.29392114372e-06

Current iteration: 701
Current Error: 5.29402072087e-06

Current iteration: 702
Current Error: 0.123510709039

Current iteration: 703
Current Error: 5.29398797296e-06

Current iteration: 704
Current Error: 0.042052102367

Current iteration: 705
Current Error: 5.29387112567e-06

Current iteration: 706
Current Error: 5.31104432681e-06

Current iteration: 707
Current Error: 5.30801750679e-06

Current iteration: 708
Current Error: 5.29354626043e-06

Current iteration: 709
Current Error: 5.29375523685e-06

Current iteration: 710
Current Error: 5.32764723783e-06

Current iteration: 711
Current Error: 5.29433941425e-06

Current iteration: 712
Current Error: 5.29492972749e-06

Current iteration: 713
Current Error: 5.29393836857e-06

Current iteration: 714
Current Error: 5.29509044163e-06

Current iteration: 715
Current Error: 5.29372677716e-06

Current iteration: 716
Current Error: 5.29366550938e-06

Current iteration: 717
Current Error: 5.29959421311e-06

Current iteration: 718
Current Error: 6.39183789861e-05

Current iteration: 719
Current Error: 4.73961249685e-05

Current iteration: 720
Current Error: 8.2413909096e-06

Current iteration: 721
Current Error: 5.29438870436e-06

Current iteration: 722
Current Error: 1.19793654252e-05

Current iteration: 723
Current Error: 5.29275074126e-06

Current iteration: 724
Current Error: 5.29322320461e-06

Current iteration: 725
Current Error: 5.29708696838e-06

Current iteration: 726
Current Error: 5.29327530027e-06

Current iteration: 727
Current Error: 5.29405692932e-06

Current iteration: 728
Current Error: 5.29354586342e-06

Current iteration: 729
Current Error: 0.0282185838512

Current iteration: 730
Current Error: 5.29351661847e-06

Current iteration: 731
Current Error: 1.09219004601e-05

Current iteration: 732
Current Error: 5.29264758831e-06

Current iteration: 733
Current Error: 5.32646151817e-06

Current iteration: 734
Current Error: 5.29699730669e-06

Current iteration: 735
Current Error: 5.29438195835e-06

Current iteration: 736
Current Error: 5.2939572676e-06

Current iteration: 737
Current Error: 6.24189024018e-06

Current iteration: 738
Current Error: 5.29633623114e-06

Current iteration: 739
Current Error: 5.29387624364e-06

Current iteration: 740
Current Error: 5.59100979893e-06

Current iteration: 741
Current Error: 5.29669698259e-06

Current iteration: 742
Current Error: 5.29861616308e-06

Current iteration: 743
Current Error: 0.0722478214365

Current iteration: 744
Current Error: 5.29364703732e-06

Current iteration: 745
Current Error: 5.29380382082e-06

Current iteration: 746
Current Error: 5.55541482587e-06

Current iteration: 747
Current Error: 5.39414085786e-06

Current iteration: 748
Current Error: 5.29350233393e-06

Current iteration: 749
Current Error: 9.06762632229e-06

Current iteration: 750
Current Error: 5.29425729634e-06

Current iteration: 751
Current Error: 5.29372999459e-06

Current iteration: 752
Current Error: 7.15114681302e-06

Current iteration: 753
Current Error: 5.29373126364e-06

Current iteration: 754
Current Error: 5.30287996731e-06

Current iteration: 755
Current Error: 5.29308855364e-06

Current iteration: 756
Current Error: 0.0908799714904

Current iteration: 757
Current Error: 5.29826807637e-06

Current iteration: 758
Current Error: 5.63323446362e-06

Current iteration: 759
Current Error: 0.0953784044298

Current iteration: 760
Current Error: 5.29374209371e-06

Current iteration: 761
Current Error: 5.5838257293e-06

Current iteration: 762
Current Error: 0.192538522553

Current iteration: 763
Current Error: 5.29362567489e-06

Current iteration: 764
Current Error: 5.29331302736e-06

Current iteration: 765
Current Error: 0.0158520875996

Current iteration: 766
Current Error: 5.29354843519e-06

Current iteration: 767
Current Error: 5.30627785225e-06

Current iteration: 768
Current Error: 5.29370558267e-06

Current iteration: 769
Current Error: 5.29323873871e-06

Current iteration: 770
Current Error: 5.75325598994e-06

Current iteration: 771
Current Error: 5.2937834427e-06

Current iteration: 772
Current Error: 5.29667949958e-06

Current iteration: 773
Current Error: 5.29379067439e-06

Current iteration: 774
Current Error: 5.29327107943e-06

Current iteration: 775
Current Error: 5.29381980833e-06

Current iteration: 776
Current Error: 5.29357432687e-06

Current iteration: 777
Current Error: 5.29279231541e-06

Current iteration: 778
Current Error: 0.0991159232564

Current iteration: 779
Current Error: 5.29808749972e-06

Current iteration: 780
Current Error: 5.29315010598e-06

Current iteration: 781
Current Error: 5.29775813149e-06

Current iteration: 782
Current Error: 5.30171240182e-06

Current iteration: 783
Current Error: 5.29395443447e-06

Current iteration: 784
Current Error: 5.29387897644e-06

Current iteration: 785
Current Error: 5.29381113013e-06

Current iteration: 786
Current Error: 5.29723902021e-06

Current iteration: 787
Current Error: 5.29310041198e-06

Current iteration: 788
Current Error: 5.29346816416e-06

Current iteration: 789
Current Error: 5.29374081985e-06

Current iteration: 790
Current Error: 9.91485769591e-06

Current iteration: 791
Current Error: 5.29330678965e-06

Current iteration: 792
Current Error: 5.29394803652e-06

Current iteration: 793
Current Error: 5.29775813149e-06

Current iteration: 794
Current Error: 5.29384338646e-06

Current iteration: 795
Current Error: 5.29355066443e-06

Current iteration: 796
Current Error: 0.431116324836

Current iteration: 797
Current Error: 5.29392605888e-06

Current iteration: 798
Current Error: 0.000106174132417

Current iteration: 799
Current Error: 5.293527513e-06

Current iteration: 800
Current Error: 5.30568836661e-06

Current iteration: 801
Current Error: 5.29581079282e-06

Current iteration: 802
Current Error: 5.29471093376e-06

Current iteration: 803
Current Error: 0.0282185838512

Current iteration: 804
Current Error: 0.0357516281281

Current iteration: 805
Current Error: 5.29842154943e-06

Current iteration: 806
Current Error: 5.68741245349e-06

Current iteration: 807
Current Error: 5.29342982884e-06

Current iteration: 808
Current Error: 5.29355940682e-06

Current iteration: 809
Current Error: 5.2937087012e-06

Current iteration: 810
Current Error: 0.0254389683472

Current iteration: 811
Current Error: 5.42098619488e-06

Current iteration: 812
Current Error: 5.2949837789e-06

Current iteration: 813
Current Error: 5.30231752042e-06

Current iteration: 814
Current Error: 0.0904531281758

Current iteration: 815
Current Error: 5.29355590867e-06

Current iteration: 816
Current Error: 5.29298562286e-06

Current iteration: 817
Current Error: 5.29639645849e-06

Current iteration: 818
Current Error: 5.29359925491e-06

Current iteration: 819
Current Error: 5.29346371045e-06

Current iteration: 820
Current Error: 5.29363970972e-06

Current iteration: 821
Current Error: 5.29923584755e-06

Current iteration: 822
Current Error: 5.29372862702e-06

Current iteration: 823
Current Error: 5.29382870911e-06

Current iteration: 824
Current Error: 8.69263267604e-06

Current iteration: 825
Current Error: 5.29386618579e-06

Current iteration: 826
Current Error: 5.33991299209e-06

Current iteration: 827
Current Error: 0.13174941968

Current iteration: 828
Current Error: 5.29358485425e-06

Current iteration: 829
Current Error: 5.294781473e-06

Current iteration: 830
Current Error: 5.29393717038e-06

Current iteration: 831
Current Error: 5.29365689006e-06

Current iteration: 832
Current Error: 5.29356434432e-06

Current iteration: 833
Current Error: 0.0171559662661

Current iteration: 834
Current Error: 1.09532181564e-05

Current iteration: 835
Current Error: 5.30537563243e-06

Current iteration: 836
Current Error: 5.29593415575e-06

Current iteration: 837
Current Error: 5.29381130451e-06

Current iteration: 838
Current Error: 5.29717196674e-06

Current iteration: 839
Current Error: 5.29361735093e-06

Current iteration: 840
Current Error: 0.0895861811434

Current iteration: 841
Current Error: 5.29388947631e-06

Current iteration: 842
Current Error: 1.54236092395e-05

Current iteration: 843
Current Error: 5.29273951381e-06

Current iteration: 844
Current Error: 5.29330747846e-06

Current iteration: 845
Current Error: 5.29379911023e-06

Current iteration: 846
Current Error: 5.29362775367e-06

Current iteration: 847
Current Error: 5.38091167178e-06

Current iteration: 848
Current Error: 9.91485769591e-06

Current iteration: 849
Current Error: 6.0767065832e-06

Current iteration: 850
Current Error: 1.37236418024e-05

Current iteration: 851
Current Error: 5.30502887631e-06

Current iteration: 852
Current Error: 5.30011189256e-06

Current iteration: 853
Current Error: 5.30948571377e-06

Current iteration: 854
Current Error: 5.29390593619e-06

Current iteration: 855
Current Error: 5.29251519907e-06

Current iteration: 856
Current Error: 5.29388105835e-06

Current iteration: 857
Current Error: 5.30978861618e-06

Current iteration: 858
Current Error: 5.29351570557e-06

Current iteration: 859
Current Error: 5.33845499926e-06

Current iteration: 860
Current Error: 5.29353064212e-06

Current iteration: 861
Current Error: 5.29513557848e-06

Current iteration: 862
Current Error: 5.3059151553e-06

Current iteration: 863
Current Error: 5.30428482801e-06

Current iteration: 864
Current Error: 5.29371093006e-06

Current iteration: 865
Current Error: 6.83671382882e-06

Current iteration: 866
Current Error: 5.29683973047e-06

Current iteration: 867
Current Error: 1.19700928092e-05

Current iteration: 868
Current Error: 5.29371194227e-06

Current iteration: 869
Current Error: 5.29790597375e-06

Current iteration: 870
Current Error: 9.06762632229e-06

Current iteration: 871
Current Error: 5.29366967673e-06

Current iteration: 872
Current Error: 5.29723902021e-06

Current iteration: 873
Current Error: 5.29317795795e-06

Current iteration: 874
Current Error: 5.29345889056e-06

Current iteration: 875
Current Error: 5.29291163894e-06

Current iteration: 876
Current Error: 5.29382847498e-06

Current iteration: 877
Current Error: 5.29819659098e-06

Current iteration: 878
Current Error: 5.91526910395e-06

Current iteration: 879
Current Error: 5.29441503166e-06

Current iteration: 880
Current Error: 5.29241008017e-06

Current iteration: 881
Current Error: 5.29342982884e-06

Current iteration: 882
Current Error: 5.29296385771e-06

Current iteration: 883
Current Error: 0.0996284486363

Current iteration: 884
Current Error: 5.29362471234e-06

Current iteration: 885
Current Error: 0.0241736322189

Current iteration: 886
Current Error: 5.2938980672e-06

Current iteration: 887
Current Error: 5.29391694815e-06

Current iteration: 888
Current Error: 6.21831968536e-06

Current iteration: 889
Current Error: 5.29355256906e-06

Current iteration: 890
Current Error: 5.29302745861e-06

Current iteration: 891
Current Error: 5.29502422356e-06

Current iteration: 892
Current Error: 5.2938273209e-06

Current iteration: 893
Current Error: 5.29351223232e-06

Current iteration: 894
Current Error: 5.29379879376e-06

Current iteration: 895
Current Error: 5.29358909561e-06

Current iteration: 896
Current Error: 5.30925160254e-06

Current iteration: 897
Current Error: 5.29343089722e-06

Current iteration: 898
Current Error: 1.46567115812e-05

Current iteration: 899
Current Error: 5.32082052457e-06

Current iteration: 900
Current Error: 5.29285028324e-06

Current iteration: 901
Current Error: 5.34501715541e-06

Current iteration: 902
Current Error: 5.29320742542e-06

Current iteration: 903
Current Error: 5.29450795952e-06

Current iteration: 904
Current Error: 5.29735973918e-06

Current iteration: 905
Current Error: 5.29641009468e-06

Current iteration: 906
Current Error: 5.29340170084e-06

Current iteration: 907
Current Error: 5.29517709924e-06

Current iteration: 908
Current Error: 5.29327068951e-06

Current iteration: 909
Current Error: 0.0162854073699

Current iteration: 910
Current Error: 5.30555443483e-06

Current iteration: 911
Current Error: 5.29375911064e-06

Current iteration: 912
Current Error: 5.29514591273e-06

Current iteration: 913
Current Error: 0.0959847447413

Current iteration: 914
Current Error: 5.29367805625e-06

Current iteration: 915
Current Error: 5.29370194235e-06

Current iteration: 916
Current Error: 5.68741245349e-06

Current iteration: 917
Current Error: 5.29385759797e-06

Current iteration: 918
Current Error: 5.29350441054e-06

Current iteration: 919
Current Error: 5.29345672827e-06

Current iteration: 920
Current Error: 5.29343060742e-06

Current iteration: 921
Current Error: 5.29346227407e-06

Current iteration: 922
Current Error: 0.0977551047619

Current iteration: 923
Current Error: 5.2937731803e-06

Current iteration: 924
Current Error: 5.29651447032e-06

Current iteration: 925
Current Error: 5.29322646537e-06

Current iteration: 926
Current Error: 0.000157416235857

Current iteration: 927
Current Error: 5.29394484566e-06

Current iteration: 928
Current Error: 5.31523251209e-06

Current iteration: 929
Current Error: 5.29575257296e-06

Current iteration: 930
Current Error: 5.29374828823e-06

Current iteration: 931
Current Error: 0.0695832708643

Current iteration: 932
Current Error: 0.000114368798806

Current iteration: 933
Current Error: 5.29410299801e-06

Current iteration: 934
Current Error: 5.29309295187e-06

Current iteration: 935
Current Error: 5.29382540799e-06

Current iteration: 936
Current Error: 5.29388627308e-06

Current iteration: 937
Current Error: 5.29431277012e-06

Current iteration: 938
Current Error: 0.0992574586224

Current iteration: 939
Current Error: 5.31054258762e-06

Current iteration: 940
Current Error: 5.29355722128e-06

Current iteration: 941
Current Error: 1.00927617971e-05

Current iteration: 942
Current Error: 8.67929038327e-06

Current iteration: 943
Current Error: 0.0935918973472

Current iteration: 944
Current Error: 5.30683543727e-06

Current iteration: 945
Current Error: 5.29377910868e-06

Current iteration: 946
Current Error: 5.29826807637e-06

Current iteration: 947
Current Error: 5.29923584755e-06

Current iteration: 948
Current Error: 5.29345350626e-06

Current iteration: 949
Current Error: 5.29378965729e-06

Current iteration: 950
Current Error: 5.29360968193e-06

Current iteration: 951
Current Error: 5.2945478062e-06

Current iteration: 952
Current Error: 0.316977489231

Current iteration: 953
Current Error: 5.34188251623e-06

Current iteration: 954
Current Error: 5.29381813018e-06

Current iteration: 955
Current Error: 0.000157416235857

Current iteration: 956
Current Error: 5.2935511788e-06

Current iteration: 957
Current Error: 9.64771538443e-06

Current iteration: 958
Current Error: 5.2931780359e-06

Current iteration: 959
Current Error: 5.29395399817e-06

Current iteration: 960
Current Error: 5.29352386898e-06

Current iteration: 961
Current Error: 5.29378351956e-06

Current iteration: 962
Current Error: 0.102664844887

Current iteration: 963
Current Error: 5.29342761853e-06

Current iteration: 964
Current Error: 5.29361372548e-06

Current iteration: 965
Current Error: 0.000254539120445

Current iteration: 966
Current Error: 5.2945916891e-06

Current iteration: 967
Current Error: 5.76898413269e-06

Current iteration: 968
Current Error: 0.000554273717481

Current iteration: 969
Current Error: 0.00922736540248

Current iteration: 970
Current Error: 0.0840415400567

Current iteration: 971
Current Error: 5.29380874546e-06

Current iteration: 972
Current Error: 5.30766003917e-06

Current iteration: 973
Current Error: 0.00352473302415

Current iteration: 974
Current Error: 5.29818850746e-06

Current iteration: 975
Current Error: 0.0228828078163

Current iteration: 976
Current Error: 5.29612060938e-06

Current iteration: 977
Current Error: 5.29497339827e-06

Current iteration: 978
Current Error: 5.30095640078e-06

Current iteration: 979
Current Error: 5.29308228243e-06

Current iteration: 980
Current Error: 5.30066384008e-06

Current iteration: 981
Current Error: 5.29939746387e-06

Current iteration: 982
Current Error: 5.31030111028e-06

Current iteration: 983
Current Error: 5.29611211209e-06

Current iteration: 984
Current Error: 5.29825731194e-06

Current iteration: 985
Current Error: 5.7598701514e-06

Current iteration: 986
Current Error: 0.0017422598288

Current iteration: 987
Current Error: 5.29349023787e-06

Current iteration: 988
Current Error: 5.29397575841e-06

Current iteration: 989
Current Error: 5.29295754231e-06

Current iteration: 990
Current Error: 2.85558610642e-05

Current iteration: 991
Current Error: 6.4162404125e-06

Current iteration: 992
Current Error: 5.29590229769e-06

Current iteration: 993
Current Error: 0.00880855756513

Current iteration: 994
Current Error: 0.0758591382713

Current iteration: 995
Current Error: 5.29414439632e-06

Current iteration: 996
Current Error: 5.4090821362e-06

Current iteration: 997
Current Error: 0.323898938478

Current iteration: 998
Current Error: 5.29327068951e-06

Current iteration: 999
Current Error: 5.29320742542e-06

Testing done! Check out the generated output files ('testing_err.txt' and 'training_err.txt')
Error percentage on testing set: 0.02
jkim@jKim-MacBook source % 
