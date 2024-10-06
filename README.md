# AI Pathfinding Simulation

## Overview
This project simulates an AI pathfinding algorithm designed to help civilians in warzones find safe evacuation routes. The focus is on reducing civilian casualties during bombing situations by providing real-time maps that highlight safe paths to aid camps, helping people avoid blocked roads or dangerous areas. 

The simulation uses a grid-based map where AI calculates the fastest route from one point to another, avoiding obstacles like destroyed buildings or blocked roads.

## Problem
Civilian casualties in warfare are tragically high, especially in bombing situations where people have little time to evacuate. The average warning time for missile strikes is often just 2 minutes, leaving civilians with limited time to gather necessities and find safety.

## Solution
This project aims to provide a platform that helps civilians during these critical moments by offering a map-based tool that can quickly identify safe routes. The map helps civilians:
- Navigate around blocked roads or damaged areas
- Find the fastest path to nearby aid camps
- Stay connected with family and friends through real-time updates

## Features
- **Announcement Page**: Displays statements from verified countries warning civilians of impending danger.
- **Map Page**: Displays real-time evacuation routes with AI-powered pathfinding that avoids blocked or unsafe areas.
- **Friends & Family**: Allows civilians to connect with important contacts and share their location for mutual emergency alerts.

## How it Works
The app uses the A* (A-star) pathfinding algorithm, which combines elements of Dijkstra's algorithm and Greedy Best-First Search to find the shortest path from one point to another. The AI accounts for obstacles like blocked roads or destroyed buildings by marking those cells as impassable on the grid, ensuring civilians are directed only through safe routes.

- **Heuristic Function**: The algorithm uses a heuristic (Manhattan distance) to estimate the shortest path.
- **Priority Queue**: A* uses a priority queue to explore nodes with the lowest cost first, making it efficient for pathfinding on large maps.

## This is the APP design my team made using figma:
![image](https://github.com/user-attachments/assets/89f653a2-b5ca-4540-914c-1a6ce175230f)
![image](https://github.com/user-attachments/assets/3a7ab344-361f-4a60-840e-0a2fd89bc71d)
![image](https://github.com/user-attachments/assets/d99fcd76-a357-4e7c-9b4c-601550a62b49)
![image](https://github.com/user-attachments/assets/28ccf61a-4bcf-4411-8e43-648f46defc8b)
