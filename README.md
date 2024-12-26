# P2P File Sharing Application

## Overview
This project is a Python-based interactive application designed for secure end-to-end peer-to-peer (P2P) file sharing. It consists of two main modules: a Host and a Client, allowing users to share and receive files in a private and secure manner.

## Project Structure
```
p2p-file-sharing-app
├── src
│   ├── client.py        # Client module for connecting to the host and downloading files
│   ├── host.py          # Host module for sharing files with clients
│   ├── utils
│   │   └── logger.py    # Utility functions for logging events and errors
│   └── types
│       └── __init__.py  # Custom types or data structures used in the application
├── input                # Directory for storing downloaded files
├── output               # Directory for storing files available for download
├── requirements.txt     # List of dependencies required for the project
└── README.md            # Documentation for the project
```

## Features
- **Host Module**: 
  - Set up a server to listen for incoming connections.
  - Share files from the `output` directory.
  - Log connection details and client information.

- **Client Module**: 
  - Connect to the host using IP and port.
  - List available files in the host's `output` directory.
  - Download selected files to the `input` directory with progress tracking.

- **Logging**: 
  - Detailed logging of operations, connections, and errors with formatted messages for better readability.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines
- To start the Host, run:
  ```
  python src/host.py
  ```
- To start the Client, run:
  ```
  python src/client.py
  ```
- Follow the prompts to either send or receive files.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.