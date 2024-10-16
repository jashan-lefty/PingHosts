from icmplib import ping


# Function to ping the selected host
def ping_host(host):
    try:
        # Pinging the host with 4 ICMP packets, interval of 2 seconds, and timeout of 2 seconds
        result = ping(host, count=4, interval=2, timeout=2, source=None, privileged=False)
        if result.is_alive:
            print(f"{result.address} is active. Ping time: {result.avg_rtt:.2f} ms")
        else:
            print(f"{result.address} is unreachable.")
    except Exception as e:
        print(f"Error: {str(e)} - Unable to ping the host.")


# Main program logic
def main():

    hosts = ["google.com", "youtube.com", "Facebook.com", "reddit.com", "xyz.com"]

    # Prompting user for a series of hostnames
    while True:
        host = input("Enter Hostname (or leave blank to finish): ")
        if not host:
            break
        hosts.append(host)

    # Error message if no input was entered
    if not hosts:
        print("Error: No hostnames entered. Exiting program.")
        return

    while True:
        # Displaying the list of entered hostnames
        print("\nList of entered hostnames:")
        for i, host in enumerate(hosts):
            print(f"{i}: {host}")

        # Prompting the user to choose an index
        try:
            index = input("\nEnter the index of the host to ping (leave blank to exit): ")
            if not index:  # Exit the loop if the input is blank
                print("Exiting program.")
                break

            # Convert index to integer and check if it's within the valid range
            index = int(index)
            if index < 0 or index >= len(hosts):
                print("Error: Index out of range. Please enter a valid index.")
                continue

            # Ping the selected host
            ping_host(hosts[index])

        # Handle non-integer input for index
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
