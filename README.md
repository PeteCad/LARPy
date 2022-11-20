<h1>LARPy - a user database tool for character maintenance</h1>
<p>This is my first major from the ground up project, unsolicited advice given with grace is highly welcome. </p>
<h2>Overview</h2>
<p>This will be an integrated back end for Live Action Role Play(LARP) character
    and plot maintenance tool. It will provide a quick interface for plot to update characters,
    manage rule conflicts, add player attributes, add player abilities, and export data into 
    a user friendly form and manage game playerbases.</p>
<p>The biggest thing missing from most tools is that they are limited to a specific ruleset 
    and I'm looking to define a way to clearly and flexible add new game rules, attributes 
    and abilities.</p>
<p>The next problem to solve is the UI. It's all great to have a list of information but we 
    need to be able to access it via a logical, quick and user friendly UI. We need to perform 
    updates across a selection of player's attributes(eg adding player experience or conditional 
    counters)</p>
<p>Stretch ideas for this project to keep in mind are:</p>
<ul>
    <li>a player/plot web interface, likely with Django</li> 
    <li>ability for player to created and curate new characters and submit for approval</li>
    <li>creation of a new game with new player characters</li>
    <li>hence tracking many games</li>
    <li>EXCEL CSV data ingestion</li>
    <li>PDF output using predefined templates</li>
    <li>expansion into a non-sqlite database</li>
    <li>As a separate project a mobile app for players</li>
    <li>Character Profile Pics</li>
</ul>
<p>The prototype UI can be found in the <a href="https://github.com/PeteCad/LARPy/tree/main/UI Layout Mockup/">/UI Layout Mockup</a> folder</p>
<h2>How to install and run</h2>
<p>This program is written with python 3.10. Kivy 2.1.0 will be used for a cross-platform user interface, we hope.</p>
<p>Further instructions to come as it gains complexity.</p>

<h2>License</h2>
<p>GNU Affero General Public License v3.0</p>
<p>See file COPYING
