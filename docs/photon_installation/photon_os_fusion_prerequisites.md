# Prerequisites for Running Photon OS on Fusion

Resource requirements and recommendations vary depending on several factors, including the host environment (for example, VMware Fusion and VMware vSphere), the distribution file used (ISO or OVA), and the selected installation settings (for example, full or basic installation).

Before you use Photon OS within Fusion, perform the following prerequisite tasks:

1. Verify that you have the following resources:

	<table style="height: 170px;" border="1" width="157" cellspacing="0" cellpadding="10">
	<tbody>
	<tr>
	<td><b>Resource</b></td>
	<td><b>Description</b></td>
	</tr>
	<tr>
	<td>VMware Fusion</td>
	<td>VMware Fusion (v7.0 or higher) must be installed. The latest version is recommended.</td>
	</tr>
	<tr>
	<td>Memory</td>
	<td>2GB of free RAM (recommended)</td>
	</tr>
	<tr>
	<td>Storage</td>
	<td><b>Minimal Photon install</b> : 512MB of free space (minimum); <b>Full Photon install</b> : 4GB of free space (minimum); 8GB recommended.</td>
	</tr>
	<tr>
	<td>Distribution File</td>
	<td>Photon OS ISO or OVA file downloaded from (<a href="https://packages.vmware.com/photon">https://packages.vmware.com/photon/</a>).</td>
	</tr>
	</tbody>
	</table>

	**Note:** The setup instructions in this guide use VMware Fusion Professional version 8.5.8, as per the following screenshot.

	![Fusion version](images/fs-version.png)

2. Decide whether to use the OVA or ISO distribution to set up Photon OS.

    - **OVA import** : Because of the nature of an OVA, you're getting a pre-installed version of Photon OS. You can choose the hardware version you want (OVA with hardware version 13 or 11). The OVA benefits from a simple import process and some kernel tuning for VMware environments. However, because it's a pre-installed version, the set of packages that are installed are predetermined. Any additional packages that you need can be installed using tdnf.
    - **ISO install** : The ISO, on the other hand, allows for a more complete installation or automated installation via kickstart.

    To get Photon OS up and running quickly, use the OVA.
    
1. Download Photon OS. Go to the following URL and download the latest release of Photon OS:

    [https://packages.vmware.com/photon/](https://packages.vmware.com/photon/)
    
    For instructions, see [Downloading Photon OS](Downloading-Photon-OS.md).
