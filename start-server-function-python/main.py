from googleapiclient import discovery
import time
from flask import render_template_string

def StartVM():
    # Start the VM
    service = discovery.build('compute', 'v1')
    result = service.instances().start(project='GCP_PROJECT', zone='GCP_ZONE', instance='minecraft-server').execute()
    
    # wait 5s for the VM to start
    time.sleep(5)
    # Get The VM's External Eph IP
    vm_info = service.instances().get(project="GCP_PROJECT", zone="GCP_ZONE", instance='minecraft-server').execute()
    vm_access_config = vm_info['networkInterfaces'][0]['accessConfigs'][0]
    vm_ip = str(vm_access_config.get('natIP'))
    return vm_ip

def main(request):
    External_IP = StartVM()
    print(External_IP)

    return render_template_string(INDEX_HTML, EXTERNAL_VM_EPH_IP=External_IP)


INDEX_HTML = """
<!DOCTYPE html>
<html data-wf-page="621388b9befd323ca619643a" data-wf-site="621388b9befd32edc4196439">
<head>
  <style>
    * {
    margin: 0;
    padding: 0;
    }

    body{
        background-color: #FFF;
        font-size: 1px;
        animation: animate 0.7s ease infinite;
    }

    @keyframes animate {
        0% {font-size: 1px;}
        100% {font-size: 1px;}
      }

    #container{
        display: table;
        margin: 0 auto;
        height: 220em;
        width: 220em;
        margin-top: 25vh;
        transition: margin-top 2s ease-in-out;
    }

    #heart{
        background: rgba(0, 0, 0, 0);
        height: 20em;
        width: 20em;
        box-shadow: 
        /*1st line*/
        40em 0    0 #111,
        60em 0    0 #111,
        140em 0    0 #111,
        160em 0    0 #111,
        /*2nd line*/
        20em 20em    0 #111,
        40em 20em    0 #EF3030,
        60em 20em    0 #EF3030,
        80em 20em    0 #111,
        120em 20em    0 #111,
        140em 20em    0 #EF3030,
        160em 20em    0 #EF3030,
        180em 20em    0 #111,
        /*3rd line*/
        0em 40em    0 #111,
        20em 40em    0 #EF3030,
        40em 40em    0 #FFF,
        60em 40em    0 #EF3030,
        80em 40em    0 #EF3030,
        100em 40em    0 #111,
        120em 40em    0 #EF3030,
        140em 40em    0 #EF3030,
        160em 40em    0 #EF3030,
        180em 40em    0 #EF3030,
        200em 40em    0 #111,
        /*4th line*/
        0em 60em    0 #111,
        20em 60em    0 #EF3030,
        40em 60em    0  #EF3030,
        60em 60em    0 #EF3030,
        80em 60em    0 #EF3030,
        100em 60em    0 #EF3030,
        120em 60em    0 #EF3030,
        140em 60em    0 #EF3030,
        160em 60em    0 #EF3030,
        180em 60em    0 #EF3030,
        200em 60em    0 #111,
        /*5th line*/
        0em 80em    0 #111,
        20em 80em    0 #EF3030,
        40em 80em    0 #EF3030,
        60em 80em    0 #EF3030,
        80em 80em    0 #EF3030,
        100em 80em    0 #EF3030,
        120em 80em    0 #EF3030,
        140em 80em    0 #EF3030,
        160em 80em    0 #EF3030,
        180em 80em    0 #EF3030,
        200em 80em    0 #111,
        /*6th line*/
        0em 100em    0 #111,
        20em 100em    0 #EF3030,
        40em 100em    0 #EF3030,
        60em 100em    0 #EF3030,
        80em 100em    0 #EF3030,
        100em 100em    0 #EF3030,
        120em 100em    0 #EF3030,
        140em 100em    0 #EF3030,
        160em 100em    0 #EF3030,
        180em 100em    0 #EF3030,
        200em 100em    0 #111,
        /*7th line*/
        20em 120em    0 #111,
        40em 120em    0 #B71F33,
        60em 120em    0 #EF3030,
        80em 120em    0 #EF3030,
        100em 120em    0 #EF3030,
        120em 120em    0 #EF3030,
        140em 120em    0 #EF3030,
        160em 120em    0 #B71F33,
        180em 120em    0 #111,
        /*8th line*/
        40em 140em    0 #111,
        60em 140em    0 #B71F33,
        80em 140em    0 #EF3030,
        100em 140em    0 #EF3030,
        120em 140em    0 #EF3030,
        140em 140em    0 #B71F33,
        160em 140em    0 #111,
        /*9th line*/
        60em 160em    0 #111,
        80em 160em    0 #B71F33,
        100em 160em    0 #EF3030,
        120em 160em    0 #B71F33,
        140em 160em    0 #111,
        /*10th line*/
        80em 180em    0 #111,
        100em 180em    0 #B71F33,
        120em 180em    0 #111,
        /*11th line*/
        100em 200em    0 #111;
      }
  </style>
  <style>
    html, body {
    height: 100%;
    background: #000;
    }

    .scene {
      width: 100%;
      height: 100%;
      perspective: 800px;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .cube {
      position: relative;
      width: 200px;
      height: 200px;
      transform-style: preserve-3d;
      animation: rotation 10s infinite alternate;
    }

    @keyframes rotation {
      0% { transform: rotateY(0deg) rotateX(0deg); }
      100% { transform: rotateY(720deg) rotateX(60deg); }
    }

    .cube__face {
      position: absolute;
      width: 200px;
      height: 200px;
    }

    .cube__face--left {
      background-image: url('https://uploaddeimagens.com.br/images/000/955/232/full/side.jpg?1497835464');
      transform: translateX(-100px) rotateY(90deg);
    }

    .cube__face--right {
      background-image: url('https://uploaddeimagens.com.br/images/000/955/232/full/side.jpg?1497835464');
      transform: translateX(100px) rotateY(90deg);
    }

    .cube__face--bottom {
      background-image: url('https://uploaddeimagens.com.br/images/000/955/231/full/bottom.jpg?1497835434');
      transform: translateY(100px) rotateX(90deg);
    }

    .cube__face--top {
      background-image: url('https://uploaddeimagens.com.br/images/000/955/233/thumb/top.jpg?1497835487');
      transform: translateY(-100px) rotateX(90deg);
    }

    .cube__face--back {
      background-image: url('https://uploaddeimagens.com.br/images/000/955/232/full/side.jpg?1497835464');
      transform: translateZ(-100px);
    }

    .cube__face--front {
      background-image: url('https://uploaddeimagens.com.br/images/000/955/232/full/side.jpg?1497835464');
      transform: translateZ(100px);
    }
  </style>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link href="https://d2pas86kykpvmq.cloudfront.net/css/normalize.css?versionId=l.8LT1pdblerE9zhkEePyTu2LXNNQXeW" rel="stylesheet" type="text/css"/>
  <link href="https://d2pas86kykpvmq.cloudfront.net/css/webflow.css?versionId=hO.LUct5q4RCn2kW223LGqidhc8zbF8l" rel="stylesheet" type="text/css"/>
  <link href="https://d2pas86kykpvmq.cloudfront.net/css/retro-new-v4.css" rel="stylesheet" type="text/css"/>
  
  
  
</head>
<body class="body">
  <div class="section-4 wf-section">
    <div class="header">
      <div class="header-left">
        <div class="wa-text by">by ValentinLvr</div>
      </div>
    </div>
    <div class="hero-text-wrapper">
      <h1 class="text-hero-2 center">Enjoy<br></h1>
    </div>
    <div id="center">
      <div id=container>
          <div id="heart">
          </div>
      </div>
    </div>
    <div data-w-id="e130c6f9-107f-faa9-a6ae-5e07587ed0ce" class="hero-images-wrapper">
      <div class="desc-wrapper">
      </div>
    </div>
  </div>
  <div data-w-id="547a0de2-dbb2-6123-2eb9-ffa19c18d590" class="section wf-section" style="background-color:#ffa3ff;">
    <div class="frame-wrapper">
      <div class="vibes-wrapper">
        <div class="x-wrapper" >
          <div class="x">
            <svg width="70" height="80" viewBox="0 0 70 80" fill="none" style="margin-bottom: 60px;" xmlns="http://www.w3.org/2000/svg">
              <rect id="rect-0" y="20" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-1" x="10" y="30" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-2" x="10" y="40" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-3" x="20" y="40" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-4" y="50" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-5" x="30" y="30" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-6" x="50" y="40" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-7" x="50" y="30" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-8" x="60" y="20" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-9" x="60" y="50" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-10" x="30" y="50" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-11" x="40" y="40" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-12" x="30" y="20" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-13" x="30" y="10" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-14" x="30" y="60" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-15" x="30" y="70" width="10" height="10" fill="#529cfa" opacity="0.0"/>
              <rect id="rect-16" x="30" width="10" height="10" fill="#529cfa" opacity="0.0"/>
            </svg>
          </div>


        </div>
        <div class="header">
        <div class="header-left"></div>
            <a data-w-id="49aba4a1-89c4-8797-5061-7fec31e51a6e" href="https://GCP_REGION-GCP_PROJECT.cloudfunctions.net/stop-minecraft-server" class="link-demo mob w-inline-block" style="background-color:#EF3030;">
              <div class="wa-text">Shutdown</div>
            </a>
          </div>
        <div class="scene">
          <div class="cube">
            <div class="cube__face cube__face--left"></div>
            <div class="cube__face cube__face--right"></div>
            <div class="cube__face cube__face--top"></div>
            <div class="cube__face cube__face--bottom"></div>
            <div class="cube__face cube__face--front"></div>
            <div class="cube__face cube__face--back"></div>
          </div>
        </div>
        <div class="hero-text-wrapper">
          <h1 class="text-hero-2 center">{{ EXTERNAL_VM_EPH_IP }}</h1>
        </div>
      </div>
    </div>
  </div>
  <div id="smile" class="section-5 wf-section">
    <div class="smile-wrapper"><img src="https://d2pas86kykpvmq.cloudfront.net/img_retro/smile.svg" loading="lazy" alt="pixel smile" class="img-smile"></div>
  </div>
  </div>
  </body>
</html>
"""