<h1>LARPy - a user database tool for character maintenance</h1>
<p>This is my first major from the ground up project, unsolited advice given with grace is highly welcome. </p>
<h2>Overview</h2>
<p>This will be an integrated back end for Live Action Role Play(LARP) character
    and plot maintenance tool. It will povide a quick interface for plot to update characters,
    manage rule conflicts, add player attributes, add player abilities, and export data into 
    a user friendly form and manage game playerbases.</p>
<p>The biggest thing missing from most tools is that they are limited to a specific ruleset 
    and I'm looking to define a way to clearly and flexible add new game rules, attributes 
    and abilities.</p>
<p>The next problem to solve is the UI. It's all great to have a list of information but we 
    need to be able to access it via a logical, quick and user freidnly UI. We need to perform 
    updates across a selection of player's attributes(eg adding player experience or conditional 
    counters)</p>
<p>Strech ideas for this project to keep in mind are:</p>
<h2>How to install and run</h2>
<p>This program is written with python 3.10. Further instructions to come as it gains complexity.</p>
<ul>
    <li>a player/plot web interface, likely with Django</li> 
    <li>ability for player to created and curate new characters and submit for approval</li>
    <li>creation of a new game with new player characters</li>
    <li>hence tracking many games</li>
    <li>EXCEL CSV data ingestion</li>
    <li>PDF output using predefined templates</li>
    <li>expantion into a non-sqlite database</li>
    <li>As a seperate project a mobile app for players</li>
</ul>

<h2>License</h2>
<p>GNU Affero General Public License v3.0</p>
<p>See file COPYING