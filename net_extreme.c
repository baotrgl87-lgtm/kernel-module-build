#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("OnePlus15");
MODULE_DESCRIPTION("极致网络优化内核模块");
MODULE_VERSION("1.0");

static int __init net_extreme_init(void)
{
    pr_info("NetExtreme: 加载成功\n");
    return 0;
}

static void __exit net_extreme_exit(void)
{
    pr_info("NetExtreme: 卸载\n");
}

module_init(net_extreme_init);
module_exit(net_extreme_exit);
