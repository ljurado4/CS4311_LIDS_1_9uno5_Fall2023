# import socket
# import time

# class AgentConnector:
    
    
#     def __init__(self, configuration_dic) -> None:
#         """Initialize the AgentConnector with a configuration dictionary

#         Args:
#             configuration_dic (dict): Dictionary containing agent configuration details.
#         """
#         self.agent_configs = configuration_dic
    
#     def connect_other_agnets(self):
#         """Given agent configuration  establish connections
#         to other agents defined in the configuration.
#         """
#         agent_ip = self.agent_configs['ip']

#         for port in self.agent_configs['ports'].split(","):
#             for key, target_agent in self.agent_configs.items():
        
#                 target_ip = target_agent['ip']
            
#                 if target_ip != agent_ip:  
#                     try:
#                         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                             s.connect((target_ip, int(port)))
                            
#                             print(f"Connected {agent_ip} to {target_ip} on port {port}")
                            
#                             s.close()
#                     except Exception as e:
#                         print(f"Error connecting {agent_ip} to {target_ip} on port {port}: {e}")

#     def listen_for_connections(self):
#         """Start a listening server for the current agent to accept incoming connections."""
#         agent_ip = self.agent_configs['ip']

#         for port in self.agent_configs['ports'].split(","):
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                 s.bind((agent_ip, int(port)))
#                 s.listen()
#                 print(f"Agent {agent_ip} is now listening on port {port}...")
#                 conn, addr = s.accept()
#                 with conn:
#                     print(f"Connected by {addr}")
#                 s.close()
    
#     def connect_all_agents(self):
#         """Attempt to connect each agent to every other agent based on configuration.
#         """
#         for key, agent in self.agent_configs.items():
#             self.connect_to_others(agent)
#             time.sleep(1)  
