# Mappings of enum names<->values to be inserted into construct's Enum adapter
#

# e_ident[EI_CLASS] in the ELF header
ENUM_EI_CLASS = dict(
    ELFCLASSNONE=0,
    ELFCLASS32=1,
    ELFCLASS64=2
)

# e_ident[EI_DATA] in the ELF header
ENUM_EI_DATA = dict(
    ELFDATANONE=0,
    ELFDATA2LSB=1,
    ELFDATA2MSB=2
)

# e_version in the ELF header
ENUM_E_VERSION = dict(
    EV_NONE=0,
    EV_CURRENT=1
)

# e_type in the ELF header
ENUM_E_TYPE = dict(
    ET_NONE=0,
    ET_REL=1,
    ET_EXEC=2,
    ET_DYN=3,
    ET_CORE=4,
    ET_LOPROC=0xff00,
    ET_HIPROC=0xffff,
    _default_='PROC_SPECIFIC',
)

# e_machine in the ELF header
# (this list is currently somewhat partial...)
ENUM_E_MACHINE = dict(
    EM_NONE=0,
    EM_M32=1,
    EM_SPARC=2,
    EM_386=3,
    EM_68K=4,
    EM_88K=5,
    EM_860=7,
    EM_MIPS=8,
    EM_S370=9,
    EM_MIPS_RS4_BE=10,
    EM_IA_64=50,
    EM_X86_64=62,
    EM_AVR=83,
    _default_='RESERVED',
)

# sh_type in the section header
ENUM_SH_TYPE = dict(
    SHT_NULL=0,
    SHT_PROGBITS=1,
    SHT_SYMTAB=2,
    SHT_STRTAB=3,
    SHT_RELA=4,
    SHT_HASH=5,
    SHT_DYNAMIC=6,
    SHT_NOTE=7,
    SHT_NOBITS=8,
    SHT_REL=9,
    SHT_SHLIB=10,
    SHT_DYNSYM=11,
    SHT_INIT_ARRAY=14,
    SHT_FINI_ARRAY=15,
    SHT_PREINIT_ARRAY=16,
    SHT_GROUP=17,
    SHT_SYMTAB_SHNDX=18,
    SHT_NUM=19,
    SHT_LOOS=0x60000000,
    SHT_HIOS=0x6fffffff,
    SHT_LOPROC=0x70000000,
    SHT_HIPROC=0x7fffffff,
    SHT_LOUSER=0x80000000,
    SHT_HIUSER=0xffffffff,
    SHT_AMD64_UNWIND=0x70000001,
    _default_='RESERVED',
)

