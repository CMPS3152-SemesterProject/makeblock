import subprocess
import re


def get_com_ports_with_devcon():
    # Run devcon to get the list of all COM ports
    devcon_command = ["devcon", "hwids", "COM*"]

    try:
        # Run the devcon command and capture the output
        result = subprocess.run(devcon_command, capture_output=True, text=True, check=True)
        output = result.stdout

        # Print the raw output for debugging
        # print("Raw devcon output:\n")
        # print(output)

        # Dictionary to store port details
        ports = {}

        # Updated regex pattern to match both standard COM ports and virtual ones like com0com
        # This will capture entries like:
        # COM9
        # com0com - serial port emulator CNCA0 (COM9)
        # com0com\port (hardware id)
        port_pattern = re.compile(r"(COM[0-9A-Za-z]+|COM0COM\\PORT\\\S+)\s+Name:\s+(.*?)\s+Hardware IDs:\s+([^\n]+)")

        matches = port_pattern.findall(output)
        for match in matches:
            com_name = match[0]
            description = match[1]
            hwids = match[2].split('\n')

            port_info = {
                "Port Name": com_name,
                "Description": description,
                "Hardware IDs": hwids
            }
            ports[com_name] = port_info

        return ports

    except subprocess.CalledProcessError as e:
        print(f"Error running devcon: {e}")
        return {}
