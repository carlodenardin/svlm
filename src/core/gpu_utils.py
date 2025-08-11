import pynvml as nvml

def get_gpu_info_markdown():
    try:
        nvml.nvmlInit()
        handle = nvml.nvmlDeviceGetHandleByIndex(0)
        name = nvml.nvmlDeviceGetName(handle)
        info = nvml.nvmlDeviceGetMemoryInfo(handle)
        total_mem_mib = info.total // (1024 * 1024)
        used_mem_mib = info.used // (1024 * 1024)
        
        return (
            f"### GPU Stats\n"
            f"```\n"
            f"Name: {name}\n"
            f"Memory: {used_mem_mib} MiB / {total_mem_mib} MiB\n"
            f"```"
        )
    except Exception:
        return "### GPU Stats\n```\nGPU information not available.\n```"